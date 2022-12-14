import { Component, OnInit, OnDestroy, ChangeDetectorRef, HostListener, ViewEncapsulation } from '@angular/core';
import { MediaMatcher } from '@angular/cdk/layout';
import { Store } from '@ngrx/store';
import { DomSanitizer } from '@angular/platform-browser';
import { MatIconRegistry } from '@angular/material/icon';
import { TooltipPosition } from '@angular/material/tooltip';
import { FormControl } from '@angular/forms';

import { Subscription, Observable } from 'rxjs';
import { map } from 'rxjs/operators';

import { DataStorageService } from '../../shared/services/data-storage.service';
import { ThemeService } from '../../shared/services/theme.service';
import { AuthService } from '../../core/auth/auth.service';
import * as fromApp from '../../core/core.state';
import * as AuthActions from '../../core/auth/store/auth.actions';
// import * as RecipeActions from '../recipes/store/recipe.actions';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: [ './header.component.scss' ],
  encapsulation: ViewEncapsulation.None
})
export class HeaderComponent implements OnInit, OnDestroy {
  showNavText = false;
  isAuthenticated = false;
  positionOptions: TooltipPosition[] = [ 'after', 'before', 'above', 'below', 'left', 'right' ];
  mobileQuery: MediaQueryList;
  isDarkTheme: Observable<boolean>;
  isDTChecked = false;
  events: string[] = [];
  opened: boolean;
  appropriateClass: string = '';

  private userSub: Subscription;
  private _mobileQueryListener: () => void;

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
    private dataStorageService: DataStorageService,
    private authService: AuthService,
    private store: Store<fromApp.AppState>,
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
    this.userSub = this.store
      .select('auth')
      .pipe(map(authState => authState.user))
      .subscribe(user => {
        this.isAuthenticated = !!user;
      });
    this.isDarkTheme = this.themeService.isDarkTheme;
  }

  onMouseEnter() {
    this.showNavText = !this.showNavText;
    console.log('mouse enter: ' + this.showNavText);
  }

  onMouseLeave() {
    this.showNavText = !this.showNavText;
    console.log('mouse leave: ' + this.showNavText);
  }

  toggleDarkTheme(checked: boolean) {
    this.isDTChecked = checked;
    this.themeService.setDarkTheme(checked);
  }

  onSaveData() {
    // this.dataStorageService.storeRecipes();
    // this.store.dispatch(new RecipeActions.StoreRecipes());
  }

  onFetchData() {
    // this.dataStorageService.fetchRecipes().subscribe();
    // this.store.dispatch(new RecipeActions.FetchRecipes());
  }

  onLogout() {
    this.store.dispatch(new AuthActions.Logout());
  }

  ngOnDestroy() {
    this.userSub.unsubscribe();
    this.mobileQuery.removeEventListener('change', () => {
      this._mobileQueryListener();
    });
  }
}
