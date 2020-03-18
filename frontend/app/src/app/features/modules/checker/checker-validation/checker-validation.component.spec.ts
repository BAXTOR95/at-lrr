import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CheckerValidationComponent } from './checker-validation.component';

describe('CheckerValidationComponent', () => {
  let component: CheckerValidationComponent;
  let fixture: ComponentFixture<CheckerValidationComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CheckerValidationComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CheckerValidationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
