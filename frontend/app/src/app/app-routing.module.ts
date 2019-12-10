import { NgModule } from '@angular/core';
import { Routes, RouterModule, PreloadAllModules } from '@angular/router';

const appRoutes: Routes = [
  { path: '', redirectTo: '/resources', pathMatch: 'full' },
  {
    path: 'resources',
    loadChildren: () =>
      import('./modules/resources/resources.module').then(m => m.ResourcesModule),
  },
  {
    path: 'checker',
    loadChildren: () =>
      import('./modules/checker/checker.module').then(m => m.CheckerModule),
  },
  {
    path: 'auth',
    loadChildren: () => import('./auth/auth.module').then(m => m.AuthModule),
  },
];

@NgModule({
  imports: [
    RouterModule.forRoot(appRoutes, { preloadingStrategy: PreloadAllModules }),
  ],
  exports: [ RouterModule ],
})
export class AppRoutingModule { }
