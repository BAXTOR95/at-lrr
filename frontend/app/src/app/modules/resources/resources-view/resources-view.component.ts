import { Component, OnInit, ViewEncapsulation, ViewChild, OnDestroy } from '@angular/core';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';
import { MatTableDataSource } from '@angular/material/table';
import { Store } from '@ngrx/store';
import { Subscription } from 'rxjs';
import { map } from 'rxjs/operators';

// import {ResourceService} from '../resources.service';
import * as fromApp from '../../../store/app.reducer';


let ELEMENT_DATA: JSON[] = [];

@Component({
  selector: 'app-resources-view',
  templateUrl: './resources-view.component.html',
  styleUrls: [ './resources-view.component.scss' ],
  encapsulation: ViewEncapsulation.None
})
export class ResourcesViewComponent implements OnInit, OnDestroy {

  displayedColumns = [];

  dataSource: MatTableDataSource<JSON>;
  subscription: Subscription;

  @ViewChild(MatPaginator, { static: true }) paginator: MatPaginator;
  @ViewChild(MatSort, { static: true }) sort: MatSort;

  constructor(
    private store: Store<fromApp.AppState>,
  ) {
    ELEMENT_DATA.push(JSON.parse('{" ": ""}'));
    this.dataSource = new MatTableDataSource(ELEMENT_DATA);
    this.displayedColumns = this.getKeyValues();
  }

  ngOnInit() {
    this.displayedColumns = this.getKeyValues();
    this.subscription = this.store
      .select('resources')
      .pipe(map(resourcesState => resourcesState.resource))
      .subscribe((resource: JSON[]) => {
        ELEMENT_DATA = (resource.length > 0 ? resource : ELEMENT_DATA);
        this.dataSource = new MatTableDataSource(ELEMENT_DATA);
        this.displayedColumns = this.getKeyValues();
        this.dataSource.paginator = this.paginator;
        this.dataSource.sort = this.sort;
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

  ngOnDestroy() {
    this.subscription.unsubscribe();
  }

}
