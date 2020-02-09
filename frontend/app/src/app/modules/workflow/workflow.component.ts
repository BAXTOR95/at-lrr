import { Component, OnInit } from '@angular/core';
import { MediaMatcher } from '@angular/cdk/layout';

@Component({
  selector: 'app-workflow',
  templateUrl: './workflow.component.html',
  styleUrls: [ './workflow.component.scss' ]
})
export class WorkflowComponent implements OnInit {
  mobileQuery: MediaQueryList;

  constructor(media: MediaMatcher) {
    this.mobileQuery = media.matchMedia('(max-width: 730px)');
  }

  ngOnInit() {
  }

}
