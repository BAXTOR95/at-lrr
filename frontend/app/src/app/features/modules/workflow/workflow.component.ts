import { Component, OnInit } from '@angular/core';
import { MediaMatcher } from '@angular/cdk/layout';

import { ROUTE_ANIMATIONS_ELEMENTS } from '../../../core/core.module';

@Component({
  selector: 'app-workflow',
  templateUrl: './workflow.component.html',
  styleUrls: [ './workflow.component.scss' ]
})
export class WorkflowComponent implements OnInit {
  mobileQuery: MediaQueryList;
  routeAnimationsElements = ROUTE_ANIMATIONS_ELEMENTS;

  constructor(media: MediaMatcher) {
    this.mobileQuery = media.matchMedia('(max-width: 801px)');
  }

  ngOnInit() {
  }

}
