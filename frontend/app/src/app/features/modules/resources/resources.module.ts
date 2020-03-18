import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { HttpClientModule } from '@angular/common/http';
// import { DragDropModule } from '@angular/cdk/drag-drop';
// import { MatTabsModule } from '@angular/material/tabs';

import { SharedModule } from '../../../shared/shared.module';
import { FileSizePipe } from '../../../shared/pipes/filesize.pipe';
import { ResourcesComponent } from './resources.component';
import { ResourcesRoutingModule } from './resources-routing.module';
import { ResourcesUploadComponent } from './resources-upload/resources-upload.component';
import { ResourcesSelectComponent } from './resources-select/resources-select.component';
import { ResourcesReportSelectComponent } from './resources-report-select/resources-report-select.component';
import { ResourcesViewComponent } from './resources-view/resources-view.component';


@NgModule({
  declarations: [
    ResourcesComponent,
    ResourcesUploadComponent,
    FileSizePipe,
    ResourcesSelectComponent,
    ResourcesReportSelectComponent,
    ResourcesViewComponent
  ],
  imports: [
    RouterModule,
    ResourcesRoutingModule,
    SharedModule,
    HttpClientModule,
    // DragDropModule,
    // MatTabsModule
  ],
  // schemas: [ CUSTOM_ELEMENTS_SCHEMA ]
})
export class ResourcesModule { }
