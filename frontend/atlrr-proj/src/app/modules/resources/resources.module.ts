import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';

import { ResourcesComponent } from './resources.component';
import { ResourcesRoutingModule } from './resources-routing.module';
import { SharedModule } from '../../shared/shared.module';

@NgModule({
  declarations: [
    ResourcesComponent
  ],
  imports: [
    RouterModule,
    ReactiveFormsModule,
    ResourcesRoutingModule,
    SharedModule,
    HttpClientModule
  ],
})
export class ResourcesModule {}
