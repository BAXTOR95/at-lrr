import * as ResourceActions from './resources.actions';

export interface State {
  resource: JSON[];
  selectedResource: string;
}

const initialState: State = {
  resource: [],
  selectedResource: '',
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
    case ResourceActions.SELECT_RESOURCE:
      return {
        ...state,
        selectedResource: action.payload,
      };
    default:
      return state;
  }
}
