import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { WorkflowGenerateComponent } from './workflow-generate.component';

describe('WorkflowGenerateComponent', () => {
  let component: WorkflowGenerateComponent;
  let fixture: ComponentFixture<WorkflowGenerateComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ WorkflowGenerateComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(WorkflowGenerateComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
