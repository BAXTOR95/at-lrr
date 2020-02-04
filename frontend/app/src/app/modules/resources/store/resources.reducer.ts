import * as ResourceActions from './resources.actions';

export interface State {
  resource: JSON[];
}

const initialState: State = {
  resource: [],
};

export function resourceReducer(
  state = initialState,
  action: ResourceActions.ResourceActions,
) {
  switch (action.type) {
    case ResourceActions.SET_RESOURCE:
      return {
        ...state,
        resource: [...action.payload],
      };
    default:
      return state;
  }
}
