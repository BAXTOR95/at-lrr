import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { WorkflowSelectComponent } from './workflow-select.component';

describe('WorkflowSelectComponent', () => {
  let component: WorkflowSelectComponent;
  let fixture: ComponentFixture<WorkflowSelectComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ WorkflowSelectComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(WorkflowSelectComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
