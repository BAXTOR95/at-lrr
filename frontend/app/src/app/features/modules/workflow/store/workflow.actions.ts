import { Action } from '@ngrx/store';

export const SET_REPORT = '[Workflow] Set Report';
export const SET_REPORT_PATH = '[Workflow] Set Report Path';
export const SELECT_REPORT = '[Workflow] Select Report';
export const GENERATE_REPORT = '[Workflow] Generate Report';

export class SetReport implements Action {
  readonly type = SET_REPORT;

  constructor(public payload: JSON[]) { }
}

export class SetReportPath implements Action {
  readonly type = SET_REPORT_PATH;

  constructor(public payload: string) { }
}

export class SelectReport implements Action {
  readonly type = SELECT_REPORT;

  constructor(public payload: string) { }
}

export class GenerateReport implements Action {
  readonly type = GENERATE_REPORT;

  constructor() { }
}

export type WorkflowActions =
  | SetReport
  | SetReportPath
  | SelectReport
  | GenerateReport;
