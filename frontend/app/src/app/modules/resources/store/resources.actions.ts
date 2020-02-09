import { Action } from '@ngrx/store';

export const SET_RESOURCE = '[Resource] Set Resource';
export const SELECT_RESOURCE = '[Resource] Select Resource';
// export const UPLOAD_RESOURCE = '[Resource] Upload Resource';

export class SetResource implements Action {
  readonly type = SET_RESOURCE;

  constructor(public payload: JSON[]) {}
}

export class SelectResource implements Action {
  readonly type = SELECT_RESOURCE;

  constructor(public payload: string) {}
}

export type ResourceActions =
  | SetResource
  | SelectResource;
