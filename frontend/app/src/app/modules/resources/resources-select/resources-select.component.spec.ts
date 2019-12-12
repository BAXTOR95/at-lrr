import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ResourcesSelectComponent } from './resources-select.component';

describe('ResourcesSelectComponent', () => {
  let component: ResourcesSelectComponent;
  let fixture: ComponentFixture<ResourcesSelectComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ResourcesSelectComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ResourcesSelectComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
