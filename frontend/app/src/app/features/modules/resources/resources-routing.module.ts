import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { ResourcesComponent } from './resources.component';
import { ResourcesUploadComponent } from './resources-upload/resources-upload.component';
import { AuthGuard } from '../../../core/auth/auth.guard';
// import { ResourcesResolverService } from './resources-resolver.service';

const resourcesRoutes: Routes = [
  {
    path: '',
    component: ResourcesComponent,
    canActivate: [ AuthGuard ],
    children: [
      { path: '', component: ResourcesComponent },
      // {
      //   path: '/approval',
      //   component: CheckerApprovalComponent,
      //   resolve: [CheckerResolverService],
      // },
      // {
      //   path: '/validation',
      //   component: CheckerValidationComponent,
      //   resolve: [CheckerResolverService],
      // },
    ],
  },
];

@NgModule({
  imports: [ RouterModule.forChild(resourcesRoutes) ],
  exports: [ RouterModule ],
})
export class ResourcesRoutingModule { }
