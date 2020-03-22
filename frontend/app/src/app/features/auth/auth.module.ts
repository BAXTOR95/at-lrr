import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { AuthComponent } from './auth/auth.component';
import { AuthRoutingModule } from './auth-routing.module';
import { SharedModule } from '../../shared/shared.module';

@NgModule({
  declarations: [ AuthComponent ],
  imports: [
    CommonModule,
    SharedModule,
    FormsModule,
    AuthRoutingModule,
  ],
})
export class AuthModule { }
