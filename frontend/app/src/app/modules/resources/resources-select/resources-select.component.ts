import {Component, OnInit, ViewEncapsulation, EventEmitter, Output} from '@angular/core';
import {FormBuilder, FormGroup, FormControl, Validators} from '@angular/forms';
import {Store} from '@ngrx/store';
import {Observable} from 'rxjs';
import {startWith, map} from 'rxjs/operators';

// import {ResourceService} from '../resources.service';
import * as fromApp from '../../../store/app.reducer';
import * as ResourceActions from '../store/resources.actions';


export interface ResourceValue {
  value: string;
  viewValue: string;
}

export interface ResourceGroup {
  type: string;
  names: ResourceValue[];
}

// export const _filter = (opt: ResourceValue[], value: string): ResourceValue[] => {
//   const filterValue = value.toLowerCase();

//   return opt.filter(item => item.value.toLowerCase().indexOf(filterValue) === 0);
// };

@Component({
  selector: 'app-resources-select',
  templateUrl: './resources-select.component.html',
  styleUrls: ['./resources-select.component.scss'],
  encapsulation: ViewEncapsulation.None
})
export class ResourcesSelectComponent implements OnInit {

  resourceControl = new FormControl('', Validators.required);

  resourceGroups: ResourceGroup[] = [{
    type: 'Manual',
    names: [
      {value: 'CND', viewValue: 'CORPORATIVO NO DIRIGIDA.XLS'},
      {value: 'SC', viewValue: 'TMP_SobregirosConsumer.txt'},
      {value: 'RICG', viewValue: 'Rendimientos_Corporativo.xls'},
      {value: 'MM', viewValue: 'Migrated Mortgage'},
      {value: 'GICG', viewValue: 'Insumo Gaveta (Agricola, Turismo, Manufactura e Hipotecario)'},
      {value: 'MISP', viewValue: 'MIS Provisiones'},
      {value: 'PPRRHH', viewValue: 'Préstamos Sobre Prestaciones - Sudeban.xls'},
      // {value: '', viewValue: 'PlantillaTMPCorporativoNoDirEnlazado.xlsx'},
      // {value: '', viewValue: 'SOBREGIROS_ICG.XLS'},
      // 'RPT_STG_Dirigidas_AGRICOLA_CONSUMER.txt',
      // 'RPT_STG_Dirigidas_AGRICOLA_CORPORATE.txt',
      // 'RPT_STG_Dirigidas_HIPOTECARIO_CORTO_PLAZO.txt',
      // 'RPT_STG_Dirigidas_HIPOTECARIO_LARGO_PLAZO.txt',
      // 'RPT_STG_Dirigidas_MANUFACTURA.txt',
      // 'RPT_STG_Dirigidas_MICROFINANCIERO.txt',
      // 'RPT_STG_Dirigidas_TURISMO.txt',
      // {value: '', viewValue: 'CITIBANK  AT-04 MES AÑO.xlsx(IngresoFamModalidadHipo)'},
    ]
  }, {
    type: 'Automatic',
    names: [
      {value: 'CD', viewValue: 'RPT_STG_Dirigidas'},
      {value: 'AT04CRE', viewValue: 'AT04CRE(cosmos)'},
      {value: 'LNP860', viewValue: 'Lnp860'},
      {value: 'VNP003T', viewValue: 'VNP003T'},
      {value: 'AH', viewValue: 'ACCOUNT HISTORY.txt'},
      {value: 'BBAT', viewValue: 'BalByAcctTransformada.txt'},
      {value: 'SIIF', viewValue: 'Reporte_SIIF.txt'},
      {value: 'FDN', viewValue: 'TB_FDN.txt'},
      {value: 'AT07', viewValue: 'AT07.txt'},
      // 'clientesconsumer_05.txt',
    ]
  }
  ];

  @Output() resourceSelected = new EventEmitter<string>();

  constructor(
    // private resourceService: ResourceService,
    private store: Store<fromApp.AppState>,
  ) {}

  ngOnInit() {
    this.onValueChanges();
  }

  onValueChanges(): void {
    this.resourceControl.valueChanges.subscribe(value => this._setValue(value));
  }

  private _setValue(value: string) {
    this.store.dispatch(new ResourceActions.SelectResource(value));
    // console.log(value);
  }

  // private _search(nameKey: string, resourceGroup: ResourceGroup[]) {
  //   for (const group of resourceGroup) {
  //     for (const name of group.names) {
  //       if (name.viewValue === nameKey) {
  //         return name;
  //       }
  //     }
  //   }
  // }

  // private _filterGroup(value: string): ResourceGroup[] {
  //   if (value) {
  //     const result = this._search(value, this.resourceGroups);
  //     this.resourceSelected.emit(result.value);
  //     this.resourceService.setResourceSelected(result.value);
  //     this.store.dispatch(new ResourceActions.SelectResource(result.value));
  //     return this.resourceGroups
  //       .map(group => ({type: group.type, names: _filter(group.names, value)}))
  //       .filter(group => group.names.length > 0);
  //   }

  //   return this.resourceGroups;
  // }

}
