import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ResourcesReportSelectComponent } from './resources-report-select.component';

describe('ResourcesSelectComponent', () => {
  let component: ResourcesReportSelectComponent;
  let fixture: ComponentFixture<ResourcesReportSelectComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ResourcesReportSelectComponent ]
    })
      .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ResourcesReportSelectComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
