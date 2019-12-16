import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { CommonModule, DatePipe } from '@angular/common';

import { MaterialDesignModule } from './material-design/material-design.module';

import { FileSizePipe } from '../shared/pipes/filesize.pipe';

import { AlertComponent } from './alert/alert.component';
import { LoadingSpinnerComponent } from './loading-spinner/loading-spinner.component';
import { PlaceholderDirective } from './placeholder/placeholder.directive';
import { DropdownDirective } from './dropdown.directive';


@NgModule({
  declarations: [
    AlertComponent,
    LoadingSpinnerComponent,
    PlaceholderDirective,
    DropdownDirective,
  ],
  imports: [
    CommonModule,
    MaterialDesignModule,
  ],
  exports: [
    CommonModule,
    AlertComponent,
    LoadingSpinnerComponent,
    PlaceholderDirective,
    DropdownDirective,
    MaterialDesignModule,
  ],
  entryComponents: [ AlertComponent, ],
  schemas: [ CUSTOM_ELEMENTS_SCHEMA ],
  providers: [
    DatePipe,
    FileSizePipe,
  ]
})
export class SharedModule { }
