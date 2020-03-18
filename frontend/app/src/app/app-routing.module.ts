import { NgModule } from '@angular/core';
import { Routes, RouterModule, PreloadAllModules } from '@angular/router';

const appRoutes: Routes = [
  {
    path: 'resources',
    loadChildren: () =>
      import('./features/modules/resources/resources.module').then(m => m.ResourcesModule),
  },
  {
    path: 'workflow',
    loadChildren: () =>
      import('./features/modules/workflow/workflow.module').then(m => m.WorkflowModule),
  },
  {
    path: 'checker',
    loadChildren: () =>
      import('./features/modules/checker/checker.module').then(m => m.CheckerModule),
  },
  {
    path: 'auth',
    loadChildren: () => import('./features/auth/auth.module').then(m => m.AuthModule),
  },
  {
    path: 'settings',
    loadChildren: () =>
      import('./features/settings/settings.module').then(m => m.SettingsModule)
  },
  {
    path: '',
    redirectTo: 'resources',
    pathMatch: 'full'
  },
  {
    path: '**',
    redirectTo: 'resources'
  }
];

@NgModule({
  imports: [
    RouterModule.forRoot(appRoutes, {
      useHash: false,
      scrollPositionRestoration: 'enabled',
      preloadingStrategy: PreloadAllModules
    }),
  ],
  exports: [ RouterModule ],
})
export class AppRoutingModule { }
