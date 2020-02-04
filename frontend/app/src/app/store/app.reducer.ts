import {ActionReducerMap} from '@ngrx/store';

import * as fromAuth from '../auth/store/auth.reducer';
import * as fromResources from '../modules/resources/store/resources.reducer';

export interface AppState {
  auth: fromAuth.State;
  resources: fromResources.State;
}

export const appReducer: ActionReducerMap<AppState> = {
  auth: fromAuth.authReducer,
  resources: fromResources.resourceReducer,
};
