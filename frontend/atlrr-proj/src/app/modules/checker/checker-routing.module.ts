import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { CheckerComponent } from './checker.component';
import { CheckerStartComponent } from './checker-start/checker-start.component';
import { CheckerApprovalComponent } from './checker-approval/checker-approval.component';
import { CheckerValidationComponent } from './checker-validation/checker-validation.component';
import { AuthGuard } from '../../auth/auth.guard';
import { CheckerResolverService } from './checker-resolver.service';

const checkerRoutes: Routes = [
  {
    path: '',
    component: CheckerComponent,
    canActivate: [AuthGuard],
    children: [
      { path: '', component: CheckerStartComponent },
      {
        path: '/approval',
        component: CheckerApprovalComponent,
        resolve: [CheckerResolverService],
      },
      {
        path: '/validation',
        component: CheckerValidationComponent,
        resolve: [CheckerResolverService],
      },
    ],
  },
];

@NgModule({
  imports: [RouterModule.forChild(checkerRoutes)],
  exports: [RouterModule],
})
export class CheckerRoutingModule {}
