import { Component, OnInit } from '@angular/core';
import { Store } from '@ngrx/store';
import { Observable } from 'rxjs';
import { ViewEncapsulation } from '@angular/compiler/src/core';

import { AuthService } from './auth/auth.service';
import { ThemeService } from './shared/services/theme.service';
import { LoggingService } from './logging.service';
import * as fromApp from './store/app.reducer';
import * as AuthActions from './auth/store/auth.actions';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: [ './app.component.css' ],
  encapsulation: ViewEncapsulation.None
})
export class AppComponent implements OnInit {
  isDarkTheme: Observable<boolean>;

  constructor(
    private store: Store<fromApp.AppState>,
    private loggingService: LoggingService,
    private themeService: ThemeService,
  ) {
    this.isDarkTheme = new Observable<boolean>();
  }

  ngOnInit() {
    this.store.dispatch(new AuthActions.AutoLogin());
    this.loggingService.printLog('Hello from AppComponent ngOnInit!');
    this.isDarkTheme = this.themeService.isDarkTheme;
  }
}
