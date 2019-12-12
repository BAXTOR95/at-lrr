import { Component, OnInit, ViewEncapsulation } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { HttpEvent, HttpEventType } from '@angular/common/http';
import { DatePipe } from '@angular/common';
// import { MediaMatcher } from '@angular/cdk/layout';

import { FileValidator } from 'ngx-material-file-input';

import { FileSizePipe } from '../../../shared/pipes/filesize.pipe';
import { UploadService } from '../resources.service';
import { SnackbarService } from '../../../shared/services/snackbar.service';

// import { CdkDragDrop, moveItemInArray, transferArrayItem } from '@angular/cdk/drag-drop';

@Component({
  selector: 'app-resources-upload',
  templateUrl: './resources-upload.component.html',
  styleUrls: [ './resources-upload.component.scss' ],
  encapsulation: ViewEncapsulation.None
})
export class ResourcesUploadComponent implements OnInit {
  form: FormGroup;
  // mobileQuery: MediaQueryList;

  DJANGO_SERVER = 'http://127.0.0.1:8000';
  progress = 0;
  response;
  resourceURL;
  inQuery = false;
  hasStartedUploading = false;
  durationInSeconds = 5;

  file = {
    lastModified: null,
    lastModifiedDate: null,
    name: null,
    size: null,
  };
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

  constructor (
    private formBuilder: FormBuilder,
    private uploadService: UploadService,
    private snackbarService: SnackbarService,
    private datePipe: DatePipe,
    private fileSizePipe: FileSizePipe) {
    // this.mobileQuery = media.matchMedia('(max-width: 665px)');
  }

  ngOnInit() {
    this.form = this.formBuilder.group({
      resource: [
        undefined,
        [ Validators.required, ] ]
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
    const formData = new FormData();
    const value = this.form.get('resource').value._files[ 0 ];
    formData.append('file', value);

    this.file.lastModified = value.lastModified;
    this.file.lastModifiedDate = value.lastModifiedDate;
    this.file.name = value.name;
    this.file.size = value.size;

    this.hasStartedUploading = true;
    this.snackbarService.openSnackBar(
      'Uploading file ' +
      `${ this.file.name } ` + ' | ' +
      `${ this.datePipe.transform(this.file.lastModifiedDate, 'yyyy-MM-dd') }` + ' | ' +
      `${ this.fileSizePipe.transform(this.file.size) }`,
      'OK',
      this.durationInSeconds
    );

    this.uploadService.upload(formData).subscribe((event: HttpEvent<any>) => {
      switch (event.type) {
        case HttpEventType.Sent:
          // this.snackbarService.openSnackBar('Request has been made!', 'Close', this.durationInSeconds);
          // this.response = 'Request has been made!';
          // console.log('Request has been made!');
          break;
        case HttpEventType.ResponseHeader:
          // this.snackbarService.openSnackBar('Response header has been received!', 'Close', this.durationInSeconds);
          // this.response = 'Response header has been received!';
          // console.log('Response header has been received!');
          break;
        case HttpEventType.UploadProgress:
          this.inQuery = false;
          this.progress = Math.round(event.loaded / event.total * 100);
          // console.log(`Uploaded! ${ this.progress }%`);
          break;
        case HttpEventType.Response:
          this.snackbarService.openSnackBar(
            'File successfully uploaded! ' + `${ this.DJANGO_SERVER }${ event.body.file }`,
            'OK',
            this.durationInSeconds
          );
          // this.response = 'File successfully uploaded! ' + `${ this.DJANGO_SERVER }${ event.body.file }`;
          // console.log('File successfully uploaded!', event.body);
          setTimeout(() => {
            this.progress = 0;
            this.hasStartedUploading = false;
          }, 1500);
          break;
      }
    },
      (err) => {
        this.hasStartedUploading = false;
        this.snackbarService.openSnackBar(err, 'Close', this.durationInSeconds);
      });
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
