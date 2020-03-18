import { Component, OnInit } from '@angular/core';
import { MediaMatcher } from '@angular/cdk/layout';

import { ROUTE_ANIMATIONS_ELEMENTS } from '../../../core/core.module';

@Component({
  selector: 'app-resources',
  templateUrl: './resources.component.html',
  styleUrls: [ './resources.component.scss' ]
})
export class ResourcesComponent implements OnInit {
  mobileQuery: MediaQueryList;
  mediumQuery: MediaQueryList;
  routeAnimationsElements = ROUTE_ANIMATIONS_ELEMENTS;

  constructor(media: MediaMatcher) {
    this.mobileQuery = media.matchMedia('(max-width: 750px)');
    this.mediumQuery = media.matchMedia('(max-width: 1135px)');
  }

  ngOnInit() {
  }

}
