import { Injectable } from '@angular/core';
import { HttpErrorResponse, HttpClient } from '@angular/common/http';
import { Observable, throwError, Subject } from 'rxjs';
import { catchError } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class ResourceService {

  DJANGO_SERVER = 'http://127.0.0.1:8000';

  resourceSelectedChanged = new Subject<string>();

  resourceSelected = '';

  constructor (private http: HttpClient) { }

  public upload(formData) {
    return this.http.post(`${ this.DJANGO_SERVER }/api/upload/`, formData, {
      reportProgress: true,
      observe: 'events'
    }).pipe(
      catchError(this.errorMgmt)
    );
  }

  setResourceSelected(resourceSelected: string) {
    this.resourceSelected = resourceSelected;
    this.resourceSelectedChanged.next(this.resourceSelected);
  }

  getSelectedResource() {
    return this.resourceSelected;
  }

  errorMgmt(error: HttpErrorResponse) {
    let errorMessage = '';
    if (error.error instanceof ErrorEvent) {
      // Get client-side error
      errorMessage = error.error.message;
    } else {
      // Get server-side error
      errorMessage = `Error Code: ${ error.status }\nMessage: ${ error.message }`;
    }
    console.log(errorMessage);
    return throwError(errorMessage);
  }
}
