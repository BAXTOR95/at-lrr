import { Component, OnInit, ViewEncapsulation, ViewChild, OnDestroy } from '@angular/core';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';
import { MatTableDataSource } from '@angular/material/table';
import { Location } from '@angular/common';
import { Store } from '@ngrx/store';
import { DomSanitizer } from '@angular/platform-browser';
import { Subscription } from 'rxjs';
import { map } from 'rxjs/operators';

import { WorkflowService } from '../workflow.service';

import * as fromApp from '../../../../core/core.state';
import { environment } from 'src/environments/environment';


let ELEMENT_DATA: JSON[] = [];
const jsonData = JSON.parse('{" ": ""}');

@Component({
  selector: 'app-workflow-view',
  templateUrl: './workflow-view.component.html',
  styleUrls: [ './workflow-view.component.scss' ],
})
export class WorkflowViewComponent implements OnInit, OnDestroy {

  displayedColumns = [];

  dataSource: MatTableDataSource<JSON>;
  reportSubscription: Subscription;
  reportPathSubscription: Subscription;
  reportPath: string;
  location: Location;

  @ViewChild(MatPaginator, { static: true }) paginator: MatPaginator;
  @ViewChild(MatSort, { static: true }) sort: MatSort;


  constructor(
    private store: Store<fromApp.AppState>,
    private sanitizer: DomSanitizer,
    private workflowService: WorkflowService,
    location: Location
  ) {
    ELEMENT_DATA = [ jsonData ];
    this.dataSource = new MatTableDataSource(ELEMENT_DATA);
    this.displayedColumns = this.getKeyValues();
    this.location = location;
  }

  ngOnInit() {
    this.displayedColumns = this.getKeyValues();
    this.reportSubscription = this.store
      .select('workflow')
      .pipe(map(workflowState => workflowState.report))
      .subscribe((report: JSON[]) => {
        ELEMENT_DATA = (report.length > 0 ? report : ELEMENT_DATA);
        this.dataSource = new MatTableDataSource(ELEMENT_DATA);
        this.displayedColumns = this.getKeyValues();
        this.dataSource.paginator = this.paginator;
        this.dataSource.sort = this.sort;
      });
    this.reportPathSubscription = this.store
      .select('workflow')
      .pipe(map(workflowState => workflowState.report_path))
      .subscribe((report: string) => {
        this.reportPath = (report ? this.location.normalize(environment.djangoServer + report) : '')
      });
  }

  applyFilter(event: Event) {
    const filterValue = (event.target as HTMLInputElement).value;
    this.dataSource.filter = filterValue.trim().toLowerCase();

    if (this.dataSource.paginator) {
      this.dataSource.paginator.firstPage();
    }
  }

  getKeyValues() {
    // console.log(ELEMENT_DATA);
    // console.log(Object.keys(`keys: ${ ELEMENT_DATA }`));
    const columnsToDisplay = [];
    const values = (Object.keys(ELEMENT_DATA[ 0 ]) as Array<keyof typeof ELEMENT_DATA[ 0 ]>).reduce((accumulator, current) => {
      columnsToDisplay.push(current);
      return columnsToDisplay;
    }, [] as (typeof ELEMENT_DATA[ 0 ][ keyof typeof ELEMENT_DATA[ 0 ] ])[]);

    return values;
  }

  downloadReport(): void {
    this.workflowService.getFile(this.reportPath)
      .subscribe(x => {
        // It is necessary to create a new blob object with mime-type explicitly set
        // otherwise only Chrome works like it should
        const newBlob = new Blob([ x ], { type: 'application/text' });

        // IE doesn't allow using a blob object directly as link href
        // instead it is necessary to use msSaveOrOpenBlob
        if (window.navigator && window.navigator.msSaveOrOpenBlob) {
          window.navigator.msSaveOrOpenBlob(newBlob);
          return;
        }

        // For other browsers:
        // Create a link pointing to the ObjectURL containing the blob.
        const data = window.URL.createObjectURL(newBlob);

        const link = document.createElement('a');
        link.href = data;
        link.download = this.reportPath.substring(this.reportPath.lastIndexOf('\\') + 1);
        // this is necessary as link.click() does not work on the latest firefox
        link.dispatchEvent(new MouseEvent('click', { bubbles: true, cancelable: true, view: window }));

        setTimeout(function () {
          // For Firefox it is necessary to delay revoking the ObjectURL
          window.URL.revokeObjectURL(data);
          link.remove();
        }, 100);
      });
  }

  ngOnDestroy() {
    this.reportSubscription.unsubscribe();
    this.reportPathSubscription.unsubscribe();
  }

}
