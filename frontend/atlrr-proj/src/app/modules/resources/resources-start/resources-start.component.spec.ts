import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ResourcesStartComponent } from './resources-start.component';

describe('ResourcesStartComponent', () => {
  let component: ResourcesStartComponent;
  let fixture: ComponentFixture<ResourcesStartComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ResourcesStartComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ResourcesStartComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
