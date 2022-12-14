import { Injectable } from '@angular/core';
import { HttpErrorResponse, HttpClient } from '@angular/common/http';
import { Observable, throwError, Subject } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class ResourceService {

  DJANGO_SERVER = environment.djangoServer;

  resourceSelectedChanged = new Subject<string>();

  resourceSelected = '';

  resourceData: JSON[];

  constructor(private http: HttpClient) { }

  public upload(formData) {
    return this.http.post(`${ this.DJANGO_SERVER }/api/upload/file/resource/`, formData, {
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

  setResourceData(jsonData: string) {
    this.resourceData = JSON.parse(jsonData);
  }

  getResourceData() {
    return this.resourceData;
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
