import { NgModule } from '@angular/core';
import { Routes, RouterModule, PreloadAllModules } from '@angular/router';

const appRoutes: Routes = [
  { path: '', redirectTo: '/resources', pathMatch: 'full' },
  {
    path: 'resources',
    loadChildren: () =>
      import( './modules/resources/resources.module' ).then( m => m.ResourcesModule ),
  },
  // {
  //   path: 'shopping-list',
  //   loadChildren: () =>
  //     import('./shopping-list/shopping-list.module').then(
  //       m => m.ShoppingListModule,
  //     ),
  // },
  {
    path: 'auth',
    loadChildren: () => import( './auth/auth.module' ).then( m => m.AuthModule ),
  },
];

@NgModule( {
  imports: [
    RouterModule.forRoot( appRoutes, { preloadingStrategy: PreloadAllModules } ),
  ],
  exports: [ RouterModule ],
} )
export class AppRoutingModule { }