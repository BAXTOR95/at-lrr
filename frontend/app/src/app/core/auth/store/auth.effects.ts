import { Actions, ofType, Effect } from '@ngrx/effects';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { switchMap, catchError, map, tap } from 'rxjs/operators';
import { of } from 'rxjs';

import { environment } from 'src/environments/environment';
import * as AuthActions from './auth.actions';
import { User } from '../user.model';
import { AuthService } from './../auth.service';
import { LocalStorageService } from '../../local-storage/local-storage.service';

export interface AuthResponseData {
  token: string;
  created: string;
  expiresIn: number;
  soeid: string;
  email: string;
  name: string;
  is_active?: boolean;
  is_staff?: boolean;
  is_superuser?: boolean;
}

export const USER_KEY = 'userData';

const handleError = (errorRes: HttpErrorResponse) => {
  let errorMessage = 'An unknown error occured!';

  console.log('errorRes', errorRes);

  if (!errorRes.error) {
    return of(new AuthActions.AuthenticateFail(errorMessage));
  }

  const errorObj = Object.values(errorRes.error);

  switch (errorRes.status) {
    case 0:
      errorMessage = 'There seems to be problems with the API call! ' +
        errorRes.message;
      break;
    case 400:
      errorMessage = errorRes.statusText + ': ' +
        errorObj[ '0' ][ 0 ];
      break;
  }
  return of(new AuthActions.AuthenticateFail(errorMessage));
};


@Injectable()
export class AuthEffects {
  DJANGO_SERVER = environment.djangoServer;

  @Effect()
  authSignup = this.actions$.pipe(
    ofType(AuthActions.SIGNUP_START),
    switchMap((signupAction: AuthActions.SignupStart) => {
      return this.http
        .post<AuthResponseData>(`${ this.DJANGO_SERVER }/api/user/create/`, {
          soeid: signupAction.payload.soeid,
          email: signupAction.payload.email,
          password: signupAction.payload.password,
          name: signupAction.payload.name,
        })
        .pipe(
          tap(resData => {
            this.authService.setLogoutTimer(+resData.expiresIn * 1000);
          }),
          map(resData => {
            return this.handleAuthentication(
              +resData.expiresIn,
              resData.soeid,
              resData.email,
              resData.name,
              resData.token
            );
          }),
          catchError(errorRes => {
            return handleError(errorRes);
          })
        );
    })
  );

  @Effect()
  authLogin = this.actions$.pipe(
    ofType(AuthActions.LOGIN_START),
    switchMap((authData: AuthActions.LoginStart) => {
      return this.http
        .post<AuthResponseData>(`${ this.DJANGO_SERVER }/api/user/token/`, {
          soeid: authData.payload.soeid,
          password: authData.payload.password,
        })
        .pipe(
          tap(resData => {
            this.authService.setLogoutTimer(+resData.expiresIn * 1000);
          }),
          map(resData => {
            return this.handleAuthentication(
              +resData.expiresIn,
              resData.soeid,
              resData.email,
              resData.name,
              resData.token
            );
          }),
          catchError(errorRes => {
            return handleError(errorRes);
          })
        );
    })
  );

  @Effect({ dispatch: false })
  authRedirect = this.actions$.pipe(
    ofType(AuthActions.AUTHENTICATE_SUCCESS),
    tap((authSuccessAction: AuthActions.AuthenticateSuccess) => {
      if (authSuccessAction.payload.redirect) {
        this.router.navigate([ '/' ]);
      }
    })
  );

  @Effect()
  autoLogin = this.actions$.pipe(
    ofType(AuthActions.AUTO_LOGIN),
    map(() => {
      const userData: {
        soeid: string;
        email: string;
        name: string;
        _token: string;
        _tokenExpirationDate: string;
      } = JSON.parse(this.localStorageService.getItem(USER_KEY));
      if (!userData) {
        return { type: 'DUMMY' };
      }

      const loadedUser = new User(
        userData.soeid,
        userData.email,
        userData.name,
        userData._token,
        new Date(userData._tokenExpirationDate)
      );

      if (loadedUser.token) {
        // this.user.next(loadedUser);
        const expirationDuration =
          new Date(userData._tokenExpirationDate).getTime() -
          new Date().getTime();
        this.authService.setLogoutTimer(expirationDuration);

        return new AuthActions.AuthenticateSuccess({
          soeid: loadedUser.soeid,
          email: loadedUser.email,
          name: loadedUser.name,
          token: loadedUser.token,
          expirationDate: new Date(userData._tokenExpirationDate),
          redirect: false
        });
        // const expirationDuration =
        //   new Date(userData._tokenExpirationDate).getTime() -
        //   new Date().getTime();
        // this.autoLogout(expirationDuration);
      }
      return { type: 'DUMMY' };
    })
  );

  @Effect({ dispatch: false })
  authLogout = this.actions$.pipe(
    ofType(AuthActions.LOGOUT),
    tap(() => {
      this.authService.clearLogoutTimer();
      this.localStorageService.removeItem(USER_KEY);
      this.router.navigate([ '/auth' ]);
    })
  );

  handleAuthentication = (
    expiresIn: number,
    soeid: string,
    email: string,
    name: string,
    token: string
  ) => {
    const expirationDate = new Date(new Date().getTime() + expiresIn * 1000);
    const user = new User(soeid, email, name, token, expirationDate);
    this.localStorageService.setItem(USER_KEY, JSON.stringify(user))
    return new AuthActions.AuthenticateSuccess({
      soeid,
      email,
      name,
      token,
      expirationDate,
      redirect: true
    });
  };

  constructor(
    private actions$: Actions,
    private http: HttpClient,
    private router: Router,
    private authService: AuthService,
    private localStorageService: LocalStorageService,
  ) { }
}
