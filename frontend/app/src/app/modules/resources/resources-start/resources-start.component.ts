import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { HttpEvent, HttpEventType } from '@angular/common/http';

import { FileValidator } from 'ngx-material-file-input';

import { UploadService } from '../resources.service';

// import { CdkDragDrop, moveItemInArray, transferArrayItem } from '@angular/cdk/drag-drop';

@Component({
  selector: 'app-resources-start',
  templateUrl: './resources-start.component.html',
  styleUrls: [ './resources-start.component.css' ]
})
export class ResourcesStartComponent implements OnInit {

  DJANGO_SERVER = 'http://127.0.0.1:8000';
  form: FormGroup;
  progress = 0;
  response;
  resourceURL;

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

  constructor (private formBuilder: FormBuilder, private uploadService: UploadService) { }

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

  onSubmit() {
    const formData = new FormData();
    console.log(this.form.get('resource').value._files[ 0 ]);
    formData.append('file', this.form.get('resource').value._files[ 0 ]);

    this.uploadService.upload(formData).subscribe(
      // (res) => {
      //   this.response = res;
      //   this.resourceURL = `${ this.DJANGO_SERVER }${ res }`;
      //   console.log('response', res);
      //   console.log(this.resourceURL);
      // },
      // (err) => {
      //   console.log(err);
      // }
    );
  }

  // uploadFile(event) {
  //   const file = (event.target as HTMLInputElement).files[ 0 ];
  //   this.form.patchValue({
  //     resource: file
  //   });
  //   this.form.get('resource').updateValueAndValidity();
  // }

  submitFile() {
    const formData = new FormData();
    const value = this.form.get('resource').value._files[ 0 ];
    formData.append('file', value);

    this.file.lastModified = value.lastModified;
    this.file.lastModifiedDate = value.lastModifiedDate;
    this.file.name = value.name;
    this.file.size = value.size;

    this.uploadService.upload(formData).subscribe((event: HttpEvent<any>) => {
      switch (event.type) {
        case HttpEventType.Sent:
          this.response = 'Request has been made!';
          // console.log('Request has been made!');
          break;
        case HttpEventType.ResponseHeader:
          this.response = 'Response header has been received!';
          // console.log('Response header has been received!');
          break;
        case HttpEventType.UploadProgress:
          this.progress = Math.round(event.loaded / event.total * 100);
          // console.log(`Uploaded! ${ this.progress }%`);
          break;
        case HttpEventType.Response:
          this.response = 'File successfully uploaded! ' + `${ this.DJANGO_SERVER }${ event.body.file }`;
          // console.log('File successfully uploaded!', event.body);
          setTimeout(() => {
            this.progress = 0;
          }, 1500);
          break;
      }
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
