import { Component, OnInit } from '@angular/core';
import { MediaMatcher } from '@angular/cdk/layout';

@Component({
  selector: 'app-resources',
  templateUrl: './resources.component.html',
  styleUrls: [ './resources.component.scss' ]
})
export class ResourcesComponent implements OnInit {
  mobileQuery: MediaQueryList;

  constructor (media: MediaMatcher) {
    this.mobileQuery = media.matchMedia('(max-width: 665px)');
  }

  ngOnInit() {
  }

}
