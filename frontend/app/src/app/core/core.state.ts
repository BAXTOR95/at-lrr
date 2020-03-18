import {
  ActionReducerMap,
  MetaReducer,
  createFeatureSelector
} from '@ngrx/store';
import { routerReducer, RouterReducerState } from '@ngrx/router-store';

import { environment } from '../../environments/environment';

import { initStateFromLocalStorage } from './meta-reducers/init-state-from-local-storage.reducer';
import { debug } from './meta-reducers/debug.reducer';
import { AuthState } from './auth/auth.models';
import { RouterStateUrl } from './router/router.state';
import { settingsReducer } from './settings/settings.reducer';
import { SettingsState } from './settings/settings.model';
import * as fromAuth from './auth/store/auth.reducer';
import * as fromResources from '../features/modules/resources/store/resources.reducer';
import * as fromWorkflow from '../features/modules/workflow/store/workflow.reducer';

export interface AppState {
  auth: fromAuth.AuthState;
  resources: fromResources.State;
  workflow: fromWorkflow.State;
}

export const appReducer: ActionReducerMap<AppState> = {
  auth: fromAuth.authReducer,
  resources: fromResources.resourceReducer,
  workflow: fromWorkflow.workflowReducer,
  settings: settingsReducer,
  router: routerReducer
};

export const metaReducers: MetaReducer<AppState>[] = [
  initStateFromLocalStorage
];

if (!environment.production) {
  if (!environment.test) {
    metaReducers.unshift(debug);
  }
}

export const selectAuthState = createFeatureSelector<AppState, AuthState>(
  'auth'
);

export const selectSettingsState = createFeatureSelector<
  AppState,
  SettingsState
>('settings');

export const selectRouterState = createFeatureSelector<
  AppState,
  RouterReducerState<RouterStateUrl>
>('router');

export interface AppState {
  auth: fromAuth.AuthState;
  resources: fromResources.State;
  workflow: fromWorkflow.State;
  settings: SettingsState;
  router: RouterReducerState<RouterStateUrl>;
}
