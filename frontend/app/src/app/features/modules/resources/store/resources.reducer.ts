import * as ResourceActions from './resources.actions';

export interface State {
  resource: JSON[];
  selectedReport: string;
  selectedResource: string;
}

const initialState: State = {
  resource: [],
  selectedReport: '',
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
        resource: [ ...action.payload ],
      };
    case ResourceActions.SELECT_REPORT:
      return {
        ...state,
        selectedReport: action.payload,
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
