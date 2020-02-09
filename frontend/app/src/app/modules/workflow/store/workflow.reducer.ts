import * as WorkflowActions from './workflow.actions';

export interface State {
  report: JSON[];
  selectedReport: string;
}

const initialState: State = {
  report: [],
  selectedReport: '',
};

export function workflowReducer(
  state = initialState,
  action: WorkflowActions.WorkflowActions,
) {
  switch (action.type) {
    case WorkflowActions.SET_REPORT:
      return {
        ...state,
        report: [ ...action.payload ],
      };
    case WorkflowActions.SELECT_REPORT:
      return {
        ...state,
        selectedReport: action.payload,
      };
    default:
      return state;
  }
}
