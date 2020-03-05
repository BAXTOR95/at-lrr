import { ActionReducerMap } from '@ngrx/store';

import * as fromAuth from '../auth/store/auth.reducer';
import * as fromResources from '../modules/resources/store/resources.reducer';
import * as fromWorkflow from '../modules/workflow/store/workflow.reducer';

export interface AppState {
  auth: fromAuth.State;
  resources: fromResources.State;
  workflow: fromWorkflow.State;
}

export const appReducer: ActionReducerMap<AppState> = {
  auth: fromAuth.authReducer,
  resources: fromResources.resourceReducer,
  workflow: fromWorkflow.workflowReducer,
};
