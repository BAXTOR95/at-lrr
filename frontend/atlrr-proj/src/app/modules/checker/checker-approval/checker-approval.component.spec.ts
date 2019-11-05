import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CheckerApprovalComponent } from './checker-approval.component';

describe('CheckerApprovalComponent', () => {
  let component: CheckerApprovalComponent;
  let fixture: ComponentFixture<CheckerApprovalComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CheckerApprovalComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CheckerApprovalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
