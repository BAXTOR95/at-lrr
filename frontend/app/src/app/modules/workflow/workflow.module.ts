import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { HttpClientModule } from '@angular/common/http';

import { SharedModule } from '../../shared/shared.module';
import { WorkflowSelectComponent } from './workflow-select/workflow-select.component';
import { WorkflowGenerateComponent } from './workflow-generate/workflow-generate.component';
import { WorkflowViewComponent } from './workflow-view/workflow-view.component';
import { WorkflowComponent } from './workflow.component';
import { WorkflowRoutingModule } from './workflow-routing.module';

@NgModule({
  declarations: [
    WorkflowComponent,
    WorkflowSelectComponent,
    WorkflowGenerateComponent,
    WorkflowViewComponent
  ],
  imports: [
    SharedModule,
    RouterModule,
    HttpClientModule,
    WorkflowRoutingModule,
  ],
  exports: [],
  providers: [],
})
export class WorkflowModule { }
