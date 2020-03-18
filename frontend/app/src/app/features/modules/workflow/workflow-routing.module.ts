import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { WorkflowComponent } from './workflow.component';
import { AuthGuard } from '../../../core/auth/auth.guard';

const workflowRoutes: Routes = [
  {
    path: '',
    component: WorkflowComponent,
    canActivate: [ AuthGuard ],
    children: [
      { path: '', component: WorkflowComponent },
    ],
  },
];

@NgModule({
  imports: [ RouterModule.forChild(workflowRoutes) ],
  exports: [ RouterModule ],
})
export class WorkflowRoutingModule { }
