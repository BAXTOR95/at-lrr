import {Component, OnInit, ViewEncapsulation, ViewChild, OnDestroy} from '@angular/core';
import {MatPaginator} from '@angular/material/paginator';
import {MatSort} from '@angular/material/sort';
import {MatTableDataSource} from '@angular/material/table';
import {Store} from '@ngrx/store';
import {Subscription} from 'rxjs';
import {map} from 'rxjs/operators';

import {ReporteSiif} from '../resources.model';
import {ResourceService} from '../resources.service';
import * as fromApp from '../../../store/app.reducer';

// const ELEMENT_DATA: ReporteSiif[] = [
//   {
//     BranchId: 2,
//     Acct: '9017996301',
//     OpenDate: new Date('18/7/2014'),
//     DaysPastDue: 0,
//     RecordDate: new Date('30/11/2019'),
//     MaturityDate: new Date('18/7/2019'),
//     CreditLimit: 0.00,
//     Rate: '0.24',
//     NumPmtsPastDue: null,
//     AmountPmtPastDue: null,
//     Amt30DPD: null,
//     Amt60DPD: null,
//     Amt90DPD: null,
//     Amt120DPD: null,
//     Amt150DPD: null,
//     Amt180DPD: null,
//     Amt210DPD: null,
//     LoanStatus: 'CAS',
//     SaldoCastigado: 0.85,
//     CloseDate: new Date('31/3/2017'),
//     BlockCodeId1: null,
//     BlockReason1: null,
//     BlockCode1Date: new Date(),
//     PrincipalBalance: 0.00,
//     TypeId: 13,
//     Gender: 'M',
//     FullName: 'CARLOS R PEINADO H',
//     ActivityId: 601,
//     OccupationId: 3,
//     ProfessionId: 4,
//     RelId: null,
//     DivisionTypeId: 'L',
//     Agro: 0,
//     Micro: 0,
//     FondoEstadal: 0,
//     Rewrite: 0,
//     CtaLocal: '8190310400',
//     Cid: 'V9417991',
//     Situacion_Credito: null,
//     SaldoCapital: null,
//     SaldoRendimientos: 0,
//     Mora: 0,
//     ClaseRiesgo: null,
//     CantCuotasVencidas: null,
//     EstadoCredito: 3,
//     OldAcct: null,
//     OrigOpenDate: new Date(),
//     OrigCreditLimit: null,
//     OrigTypeId: null,
//     Staff: 0,
//     Purchases: null,
//     FeePaid: null,
//     Address: 'uao',
//     DireccionO: null,
//     DireccionB: null,
//     Int_Efectivamente_Cobrado: 0.00,
//     Porcentaje_Comision_Flat: 0.00,
//     Monto_Comision_Flat: '0',
//     Periodicidad_Pago_Especial_Capital: '0',
//     Fecha_Cambio_Status: new Date(),
//     Fecha_Reg_Venc_Lit_cast: new Date('31/5/2017'),
//     Fecha_Exigibilidad_pago_ult_cuota: new Date('18/8/2014'),
//     Fecha_Fin_Periodo_gracia_Pago_interes: new Date('1/1/1900'),
//     Capital_Trasferido: null,
//     Fecha_cambio_Capital_Transferido: new Date(),
//     Tipo_Vivienda: 0,
//     Provision: null,
//     SaldoProvision: null
//   },
// ];


let ELEMENT_DATA: JSON[] = [];

@Component({
  selector: 'app-resources-view',
  templateUrl: './resources-view.component.html',
  styleUrls: ['./resources-view.component.scss'],
  encapsulation: ViewEncapsulation.None
})
export class ResourcesViewComponent implements OnInit, OnDestroy {

  displayedColumns = [];

  dataSource: MatTableDataSource<JSON>;
  subscription: Subscription;

  @ViewChild(MatPaginator, {static: true}) paginator: MatPaginator;
  @ViewChild(MatSort, {static: true}) sort: MatSort;

  constructor(
    private resourceService: ResourceService,
    private store: Store<fromApp.AppState>,
  ) {}

  ngOnInit() {
    ELEMENT_DATA.push(JSON.parse('{"field1": "", "field2": ""}'));
    this.displayedColumns = this.getKeyValues();
    this.subscription = this.store
      .select('resources')
      .pipe(map(resourcesState => resourcesState.resource))
      .subscribe((resource: JSON[]) => {
        ELEMENT_DATA = (resource.length > 0 ? resource : ELEMENT_DATA);
        this.dataSource = new MatTableDataSource(ELEMENT_DATA);
        this.displayedColumns = this.getKeyValues();
      });
    this.dataSource.paginator = this.paginator;
    this.dataSource.sort = this.sort;
  }

  applyFilter(filterValue: string) {
    this.dataSource.filter = filterValue.trim().toLowerCase();

    if (this.dataSource.paginator) {
      this.dataSource.paginator.firstPage();
    }
  }

  getKeyValues() {
    console.log(ELEMENT_DATA);
    console.log(Object.keys(`keys: ${ELEMENT_DATA}`));
    const columnsToDisplay = [];
    const values = (Object.keys(ELEMENT_DATA[0]) as Array<keyof typeof ELEMENT_DATA[0]>).reduce((accumulator, current) => {
      columnsToDisplay.push(current);
      return columnsToDisplay;
    }, [] as (typeof ELEMENT_DATA[0][keyof typeof ELEMENT_DATA[0]])[]);

    return values;
  }

  ngOnDestroy() {
    this.subscription.unsubscribe();
  }

}
