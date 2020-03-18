import browser from 'browser-detect';
import { Component, OnInit, OnDestroy, ChangeDetectorRef, HostListener, ViewEncapsulation } from '@angular/core';
import { Store, select } from '@ngrx/store';
import { Subscription, Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { OverlayContainer } from '@angular/cdk/overlay';
import { TooltipPosition } from '@angular/material/tooltip';

import { AuthService } from '../core/auth/auth.service';
import { ThemeService } from '../shared/services/theme.service';
import { LoggingService } from '../logging.service';
import * as fromApp from '../core/core.state';
import * as AuthActions from '../core/auth/store/auth.actions';

import { environment as env } from '../../environments/environment';

import {
  routeAnimations,
  LocalStorageService,
  selectSettingsStickyHeader,
  selectSettingsLanguage,
  selectEffectiveTheme
} from '../core/core.module';
import {
  actionSettingsChangeAnimationsPageDisabled,
  actionSettingsChangeLanguage
} from '../core/settings/settings.actions';
import { MediaMatcher } from '@angular/cdk/layout';
import { MatIconRegistry } from '@angular/material/icon';
import { DomSanitizer } from '@angular/platform-browser';
import { DataStorageService } from '../shared/services/data-storage.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: [ './app.component.scss' ],
  animations: [ routeAnimations ]
})
export class AppComponent implements OnInit {
  isProd = env.production;
  envName = env.envName;
  version = env.versions.app;
  year = new Date().getFullYear();
  // logo = require('../../assets/img/other/logo_sirdcat.png');
  languages = [ 'en', 'de', 'sk', 'fr', 'es', 'pt-br', 'zh-cn', 'he' ];
  showNavText = false;
  isAuthenticated = false;
  positionOptions: TooltipPosition[] = [ 'after', 'before', 'above', 'below', 'left', 'right' ];
  mobileQuery: MediaQueryList;
  isDarkTheme: Observable<boolean>;
  isDTChecked = false;
  events: string[] = [];
  opened: boolean;
  appropriateClass: string;

  stickyHeader$: Observable<boolean>;
  language$: Observable<string>;
  theme$: Observable<string>;

  private userSub: Subscription;
  private _mobileQueryListener: () => void;

  private static isIEorEdgeOrSafari() {
    return [ 'ie', 'edge', 'safari' ].includes(browser().name);
  }

  @HostListener('window:resize', [ '$event' ])
  getScreenHeight(event?) {
    // console.log(window.innerHeight);
    if (window.innerHeight <= 412) {
      this.appropriateClass = 'bottomRelative';
    } else {
      this.appropriateClass = 'bottomStick';
    }
  }

  constructor(
    private store: Store<fromApp.AppState>,
    private overlayContainer: OverlayContainer,
    private loggingService: LoggingService,
    private storageService: LocalStorageService,
    private dataStorageService: DataStorageService,
    private authService: AuthService,
    private themeService: ThemeService,
    changeDetectorRef: ChangeDetectorRef,
    media: MediaMatcher,
    iconRegistry: MatIconRegistry,
    sanitizer: DomSanitizer,
  ) {
    this.mobileQuery = media.matchMedia('(max-width: 600px)');
    this._mobileQueryListener = () => changeDetectorRef.detectChanges();
    this.mobileQuery.addEventListener('change', () => {
      this._mobileQueryListener();
    });
    this.getScreenHeight();
    iconRegistry.addSvgIcon(
      'check',
      sanitizer.bypassSecurityTrustResourceUrl('assets/img/icons/check-circle-regular.svg'));
    iconRegistry.addSvgIcon(
      'module',
      sanitizer.bypassSecurityTrustResourceUrl('assets/img/icons/cubes-solid.svg'));
    iconRegistry.addSvgIcon(
      'manage',
      sanitizer.bypassSecurityTrustResourceUrl('assets/img/icons/tasks-solid.svg'));
  }

  ngOnInit() {
    this.storageService.testLocalStorage();
    if (AppComponent.isIEorEdgeOrSafari()) {
      this.store.dispatch(
        actionSettingsChangeAnimationsPageDisabled({
          pageAnimationsDisabled: true
        })
      );
    }

    this.store.dispatch(new AuthActions.AutoLogin());
    this.userSub = this.store
      .select('auth')
      .pipe(map(authState => authState.user))
      .subscribe(user => {
        this.isAuthenticated = !!user;
      });
    this.stickyHeader$ = this.store.pipe(select(selectSettingsStickyHeader));
    this.language$ = this.store.pipe(select(selectSettingsLanguage));
    this.theme$ = this.store.pipe(select(selectEffectiveTheme));
  }

  onLogout() {
    this.store.dispatch(new AuthActions.Logout());
  }

  onLanguageSelect({ value: language }) {
    this.store.dispatch(actionSettingsChangeLanguage({ language }));
  }

  ngOnDestroy() {
    this.userSub.unsubscribe();
    this.mobileQuery.removeEventListener('change', () => {
      this._mobileQueryListener();
    });
  }
}
