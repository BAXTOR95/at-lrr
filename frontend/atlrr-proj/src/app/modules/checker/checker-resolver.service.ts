import { Injectable } from '@angular/core';
import {
  Resolve,
  ActivatedRouteSnapshot,
  RouterStateSnapshot,
} from '@angular/router';
import { Store } from '@ngrx/store';
import { Actions, ofType } from '@ngrx/effects';
import { take, map, switchMap } from 'rxjs/operators';
import { of } from 'rxjs';

import { Checker } from './checker.model';
import { CheckerService } from './checker.service';
import * as fromApp from '../../store/app.reducer';

@Injectable({ providedIn: 'root' })
export class CheckerResolverService implements Resolve<Checker[]> {
  constructor(
    private store: Store<fromApp.AppState>,
    private actions$: Actions,
    private checkerService: CheckerService,
  ) {}

  resolve(route: ActivatedRouteSnapshot, state: RouterStateSnapshot) {
    // return this.dataStorageService.fetchRecipes();
    // return this.store.select('checker').pipe(
    //   take(1),
    //   map(checkerState => {
    //     return checkerState.recipes;
    //   }),
    //   switchMap(recipes => {
    //     if (recipes.length === 0) {
    //       this.store.dispatch(new CheckerActions.FetchChecker());
    //       this.store.dispatch(new CheckerActions.FetchChecker());
    //       return this.actions$.pipe(
    //         ofType(CheckerActions.SET_CHECKER),
    //         take(1),
    //       );
    //     } else {
    //       return of(checker);
    //     }
    //   }),
    // );
    return null;
  }
}
