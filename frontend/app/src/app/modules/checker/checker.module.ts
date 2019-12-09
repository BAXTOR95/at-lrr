import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { ReactiveFormsModule } from '@angular/forms';

import { CheckerComponent } from './checker.component';
import { CheckerStartComponent } from './checker-start/checker-start.component';
import { CheckerApprovalComponent } from './checker-approval/checker-approval.component';
import { CheckerValidationComponent } from './checker-validation/checker-validation.component';
import { CheckerRoutingModule } from './checker-routing.module';
import { SharedModule } from '../../shared/shared.module';

@NgModule({
  declarations: [
    CheckerApprovalComponent,
    CheckerValidationComponent,
    CheckerStartComponent,
    CheckerComponent
  ],
  imports: [
    RouterModule,
    ReactiveFormsModule,
    CheckerRoutingModule,
    SharedModule,
  ],
})
export class CheckerModule { }
