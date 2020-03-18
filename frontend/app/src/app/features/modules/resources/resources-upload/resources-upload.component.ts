import { Component, OnInit, ViewEncapsulation, OnDestroy } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { HttpEvent, HttpEventType } from '@angular/common/http';
import { DatePipe } from '@angular/common';
import { Store } from '@ngrx/store';
import { Subscription } from 'rxjs';
import { map } from 'rxjs/operators';
// import { MediaMatcher } from '@angular/cdk/layout';

import { FileValidator } from 'ngx-material-file-input';

import * as fromApp from '../../../../core/core.state';
import * as ResourceActions from '../store/resources.actions';

import { FileSizePipe } from '../../../../shared/pipes/filesize.pipe';
import { ResourceService } from '../resources.service';
import { NotificationService } from '../../../../core/notifications/notification.service';
import { SnackbarService } from '../../../../shared/services/snackbar.service';
import { environment } from 'src/environments/environment';

// import { CdkDragDrop, moveItemInArray, transferArrayItem } from '@angular/cdk/drag-drop';

interface Response {
  'id': number;
  'resource_name': string;
  'file': string;
  'user': string;
  'data': object;
}

interface File {
  'lastModified': number;
  'lastModifiedDate': Date;
  'name': string;
  'size': number;
  'type': string;
  'webkitRelativePath': string;
}

@Component({
  selector: 'app-resources-upload',
  templateUrl: './resources-upload.component.html',
  styleUrls: [ './resources-upload.component.scss' ],
})
export class ResourcesUploadComponent implements OnInit, OnDestroy {
  form: FormGroup;
  subscriptionResource: Subscription;
  subscriptionReport: Subscription;
  // mobileQuery: MediaQueryList;

  DJANGO_SERVER = environment.djangoServer;
  progress = 0;
  resourceURL;
  inQuery = false;
  hasStartedUploading = false;
  durationInSeconds = 5;
  resource = '';
  report = '';


  // files = [
  //   'Blade Runner',
  //   'Cool Hand Luke',
  //   'Heat',
  //   'Juice',
  //   'The Far Side of the World',
  //   'Morituri',
  //   'Napoleon Dynamite',
  //   'Pulp Fiction'
  // ];
  // filesList = [
  //   'The Far Side of the World',
  //   'Morituri',
  //   'Napoleon Dynamite',
  //   'Pulp Fiction',
  //   'Blade Runner',
  //   'Cool Hand Luke',
  //   'Heat',
  //   'Juice'
  // ];
  // filesSelected = [];

  constructor(
    private formBuilder: FormBuilder,
    private resourceService: ResourceService,
    private notificationService: NotificationService,
    private snackbarService: SnackbarService,
    private datePipe: DatePipe,
    private fileSizePipe: FileSizePipe,
    private store: Store<fromApp.AppState>,
  ) {
    // this.mobileQuery = media.matchMedia('(max-width: 665px)');
  }

  ngOnInit() {
    this.form = this.formBuilder.group({
      resource: [
        undefined,
        [ Validators.required, ] ]
    });
    this.subscriptionResource = this.store
      .select('resources')
      .pipe(map(resourcesState => resourcesState.selectedResource))
      .subscribe((selectedResource: string) => {
        this.resource = selectedResource;
      });
    this.subscriptionReport = this.store
      .select('resources')
      .pipe(map(resourcesState => resourcesState.selectedReport))
      .subscribe((selectedReport: string) => {
        this.report = selectedReport;
      });
  }

  onChange(event) {
    if (event.target.files.length > 0) {
      const file = event.target.files[ 0 ];
      this.form.get('resource').setValue(file);
    }
  }

  submitFile() {
    this.inQuery = true;
    // this.resource = this.resourceService.getSelectedResource();

    if (this.resource.length !== 0) {
      const formData = new FormData();
      const files = this.form.get('resource').value._files;
      const value = this.form.get('resource').value._files[ 0 ];

      const filesDetail: File[] = [];
      let fileSize = 0.00;
      let fileName = '';
      let fileDate: Date;

      const fileCounts = files.length;
      const multipleFiles = (fileCounts > 1);

      for (const file of files) {
        formData.append('file', file);
        filesDetail.push(value);
      }
      formData.append('report_name', this.report);
      formData.append('resource_name', this.resource);

      for (const file of filesDetail) {
        fileSize += file.size;
        fileName += (multipleFiles ? file.name + ', ' : file.name);
        if (!multipleFiles) { fileDate = file.lastModifiedDate; }
      }

      this.hasStartedUploading = true;
      this.notificationService.info(
        `Uploading (${ fileCounts }) file ${ (multipleFiles ? 's' : '') }` +
        `${ fileName } ` + ' | ' +
        (multipleFiles ? '' : `${ this.datePipe.transform(fileDate, 'yyyy-MM-dd') }` + ' | ') +
        `${ this.fileSizePipe.transform(fileSize) }`
      );
      // this.snackbarService.openSnackBar(
      //   `Uploading (${ fileCounts }) file ${ (multipleFiles ? 's' : '') }` +
      //   `${ fileName } ` + ' | ' +
      //   (multipleFiles ? '' : `${ this.datePipe.transform(fileDate, 'yyyy-MM-dd') }` + ' | ') +
      //   `${ this.fileSizePipe.transform(fileSize) }`,
      //   'OK',
      //   this.durationInSeconds
      // );

      this.resourceService.upload(formData).subscribe((event: HttpEvent<any>) => {
        switch (event.type) {
          // case HttpEventType.Sent:
          //   this.snackbarService.openSnackBar('Request has been made!', 'Close', this.durationInSeconds);
          //   this.response = 'Request has been made!';
          //   console.log('Request has been made!');
          //   break;
          // case HttpEventType.ResponseHeader:
          //   this.snackbarService.openSnackBar('Response header has been received!', 'Close', this.durationInSeconds);
          //   this.response = 'Response header has been received!';
          //   console.log('Response header has been received!');
          //   break;
          case HttpEventType.UploadProgress:
            this.inQuery = false;
            this.progress = Math.round(event.loaded / event.total * 100);

            this.inQuery = (this.progress === 100 ? true : false);
            // console.log(`Uploaded! ${ this.progress }%`);
            break;
          case HttpEventType.Response:
            this.inQuery = false;
            this.notificationService.success('File successfully uploaded! ' + `${ this.DJANGO_SERVER }${ event.body.file }`);
            // this.snackbarService.openSnackBar(
            //   'File successfully uploaded! ' + `${ this.DJANGO_SERVER }${ event.body.file }`,
            //   'OK',
            //   this.durationInSeconds
            // );
            this.resourceService.setResourceData(event.body.data);
            this.store.dispatch(new ResourceActions.SetResource(JSON.parse(event.body.data)));
            // this.response = 'File successfully uploaded! ' + `${ this.DJANGO_SERVER }${ event.body.file }`;
            console.log('File successfully uploaded!', event.body);
            setTimeout(() => {
              this.progress = 0;
              this.hasStartedUploading = false;
            }, 1500);
            break;
        }
      },
        (err) => {
          this.hasStartedUploading = false;
          throw new Error(err);
          // this.snackbarService.openSnackBar(err, 'Close', this.durationInSeconds);
        });
    } else {
      this.notificationService.warn('Please select a resource');
      // this.snackbarService.openSnackBar('Please select a resource', 'OK', this.durationInSeconds);
    }
  }

  ngOnDestroy() {
    this.subscriptionResource.unsubscribe();
  }

  // drop(event: CdkDragDrop<string[]>) {
  //   moveItemInArray(this.files, event.previousIndex, event.currentIndex);
  // }

  // onDrop(event: CdkDragDrop<string[]>) {
  //   if (event.previousContainer === event.container) {
  //     moveItemInArray(event.container.data, event.previousIndex, event.currentIndex);
  //   } else {
  //     transferArrayItem(event.previousContainer.data,
  //       event.container.data,
  //       event.previousIndex,
  //       event.currentIndex);
  //   }
  // }
}
