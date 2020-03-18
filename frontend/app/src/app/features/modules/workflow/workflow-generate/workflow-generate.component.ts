import { Component, OnInit, ViewEncapsulation, OnDestroy } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { HttpEvent, HttpEventType } from '@angular/common/http';
import { DatePipe } from '@angular/common';
import { Store } from '@ngrx/store';
import { Subscription } from 'rxjs';
import { map } from 'rxjs/operators';
import { MatDatepickerInputEvent } from '@angular/material/datepicker';

import * as fromApp from '../../../../core/core.state';
import * as WorkflowActions from '../store/workflow.actions';

import { WorkflowService } from '../workflow.service';
import { NotificationService } from '../../../../core/notifications/notification.service';
import { SnackbarService } from '../../../../shared/services/snackbar.service';


interface Response {
  'id': number;
  'report_path': string;
  'report_name': string;
  'description': string;
  'message': string;
  'last_processing_date': Date;
  'data': object;
  'user': string;
}

@Component({
  selector: 'app-workflow-generate',
  templateUrl: './workflow-generate.component.html',
  styleUrls: [ './workflow-generate.component.scss' ]
})
export class WorkflowGenerateComponent implements OnInit, OnDestroy {
  subscription: Subscription;

  DJANGO_SERVER = 'http://127.0.0.1:8000';
  report = '';
  bookDate = new Date();
  durationInSeconds = 5;
  progress = 0;
  inQuery = false;
  workStarted = false;

  constructor(
    private formBuilder: FormBuilder,
    private workflowService: WorkflowService,
    private notificationService: NotificationService,
    private snackbarService: SnackbarService,
    private datePipe: DatePipe,
    private store: Store<fromApp.AppState>,
  ) { }

  ngOnInit() {
    this.subscription = this.store
      .select('workflow')
      .pipe(map(workflowState => workflowState.selectedReport))
      .subscribe((selectedReport: string) => {
        this.report = selectedReport;
      });
  }

  addDate(event: MatDatepickerInputEvent<Date>) {
    this.bookDate = event.value;
  }

  startWorkflow() {
    this.inQuery = true;

    if (this.report.length !== 0) {
      const formData = new FormData();
      const dateStr = this.datePipe.transform(this.bookDate, 'yyyy-MM-dd');

      formData.append('report_name', this.report);
      formData.append('book_date', dateStr);

      this.workStarted = true;
      this.notificationService.info(`Starting Construction of Report (${ this.report }) on ` +
        `${ dateStr }`);
      // this.snackbarService.openSnackBar(
      //   `Starting Construction of Report (${ this.report }) on ` +
      //   `${ dateStr }`,
      //   'OK',
      //   this.durationInSeconds
      // );

      this.workflowService.start_workflow(formData).subscribe((event: HttpEvent<any>) => {
        switch (event.type) {
          case HttpEventType.Response:
            this.progress = 100;
            this.notificationService.success(`${ event.body.report_name }` + ' Report successfully generated! ');
            // this.snackbarService.openSnackBar(
            //   `${ event.body.report_name }` + ' Report successfully generated! ',
            //   'OK',
            //   this.durationInSeconds
            // );
            this.workflowService.setResourceData(event.body.data);
            this.store.dispatch(new WorkflowActions.SetReport(JSON.parse(event.body.data)));
            this.store.dispatch(new WorkflowActions.SetReportPath(event.body.report_path));
            console.log('Report successfully created!', event.body);
            setTimeout(() => {
              this.progress = 0;
              this.workStarted = false;
            }, 1500);
            break;
        }
      },
        (err) => {
          this.workStarted = false;
          throw new Error(err);
          // this.snackbarService.openSnackBar(err, 'Close', this.durationInSeconds);
        });
    } else {
      this.notificationService.warn('Please select a report');
      // this.snackbarService.openSnackBar('Please select a report', 'OK', this.durationInSeconds);
    }
  }

  ngOnDestroy() {
    this.subscription.unsubscribe();
  }
}
