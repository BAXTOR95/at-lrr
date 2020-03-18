import { Injectable } from '@angular/core';
import { HttpErrorResponse, HttpClient } from '@angular/common/http';
import { Observable, throwError, Subject } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class WorkflowService {

  DJANGO_SERVER = environment.djangoServer;

  reportSelectedChanged = new Subject<string>();

  reportSelected = '';

  reportData: JSON[];

  constructor(private http: HttpClient) { }

  public start_workflow(formData) {
    return this.http.post(`${ this.DJANGO_SERVER }/api/workflow/workflow/report/`, formData, {
      reportProgress: true,
      observe: 'events'
    }).pipe(
      catchError(this.errorMgmt)
    );
  }

  setReportSelected(reportSelected: string) {
    this.reportSelected = reportSelected;
    this.reportSelectedChanged.next(this.reportSelected);
  }

  getSelectedResource() {
    return this.reportSelected;
  }

  setResourceData(jsonData: string) {
    this.reportData = JSON.parse(jsonData);
  }

  getResourceData() {
    return this.reportData;
  }

  getFile(fileUrl: string): Observable<Blob> {
    const uri = fileUrl;
    return this.http.get(uri, { responseType: 'blob' });
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
