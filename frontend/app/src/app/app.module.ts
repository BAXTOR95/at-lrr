import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NgModule } from '@angular/core';

import { AppComponent } from './app/app.component';
import { SharedModule } from './shared/shared.module';
import { ModulesModule } from './features/modules/modules.module';
import { AppRoutingModule } from './app-routing.module';
import { CoreModule } from './core/core.module';
import * as fromApp from './core/core.state';
import { AuthEffects } from './core/auth/store/auth.effects';
import { environment } from '../environments/environment';

@NgModule({
  declarations: [ AppComponent, ],
  imports: [
    SharedModule,
    ModulesModule,
    BrowserModule,
    BrowserAnimationsModule,
    AppRoutingModule,
    CoreModule,
  ],
  entryComponents: [ AppComponent ],
  bootstrap: [ AppComponent ]
})
export class AppModule { }
