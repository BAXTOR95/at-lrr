import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { UploadService } from '../resources.service';

@Component({
  selector: 'app-resources-start',
  templateUrl: './resources-start.component.html',
  styleUrls: ['./resources-start.component.css']
})
export class ResourcesStartComponent implements OnInit {

  DJANGO_SERVER = 'http://127.0.0.1:8000';
  form: FormGroup;
  response;
  resourceURL;

  constructor(private formBuilder: FormBuilder, private uploadService: UploadService) { }

  ngOnInit() {
    this.form = this.formBuilder.group({
      resource: ['']
    });
  }

  onChange(event) {
    if (event.target.files.length > 0) {
      const file = event.target.files[0];
      this.form.get('resource').setValue(file);
    }
  }

  onSubmit() {
    const formData = new FormData();
    formData.append('file', this.form.get('resource').value);

    this.uploadService.upload(formData).subscribe(
      (res) => {
        this.response = res;
        this.resourceURL = `${this.DJANGO_SERVER}${res.file}`;
        console.log(res);
        console.log(this.resourceURL);
      },
      (err) => {
        console.log(err);
      }
    );
  }

}
