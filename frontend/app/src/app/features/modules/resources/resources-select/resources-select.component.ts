import { Component, OnInit, ViewEncapsulation, EventEmitter, Output } from '@angular/core';
import { FormControl, Validators } from '@angular/forms';
import { Store } from '@ngrx/store';
import { Subscription } from 'rxjs';
import { map } from 'rxjs/operators';

// import {ResourceService} from '../resources.service';
import * as fromApp from '../../../../core/core.state';
import * as ResourceActions from '../store/resources.actions';


export interface ResourceValue {
  value: string;
  viewValue: string;
}

export interface ResourceGroup {
  type: string;
  names: ResourceValue[];
}

export const _filter = (opt: ResourceGroup[], type: string): ResourceGroup[] => {
  const filterValue = type.toUpperCase();

  return opt.filter(item => item.type.toUpperCase().indexOf(filterValue) === 0);
};

@Component({
  selector: 'app-resources-select',
  templateUrl: './resources-select.component.html',
  styleUrls: [ './resources-select.component.scss' ],
})
export class ResourcesSelectComponent implements OnInit {

  resourceControl = new FormControl('', Validators.required);
  subscription: Subscription;
  selectedReport: string;
  selectedResource: string;

  resourceGroups: ResourceGroup[] = [ {
    type: 'AT04',
    names: [
      { value: 'CND', viewValue: 'Corporativo No Dirigida ICG' },
      { value: 'SC', viewValue: 'Sobregiros Consumer' },
      { value: 'RICG', viewValue: 'Rendimientos Corporativo' },
      { value: 'MM', viewValue: 'Migrated Mortgage' },
      { value: 'GICG', viewValue: 'Insumo Gaveta (Agricola, Turismo, Manufactura e Hipotecario)' },
      { value: 'MISP', viewValue: 'MIS Provisiones' },
      { value: 'PPRRHH', viewValue: 'Préstamos Sobre Prestaciones RRHH - Sudeban' },
      { value: 'CD', viewValue: 'Carteras Dirigidas' },
      { value: 'AT04', viewValue: 'AT04 Ultima Transmision' },
      { value: 'AT04CRE', viewValue: 'AT04CRE(cosmos)' },
      { value: 'LNP860', viewValue: 'Lnp860' },
      { value: 'VNP003T', viewValue: 'VNP003T' },
      { value: 'AH', viewValue: 'Account History' },
      { value: 'BBAT', viewValue: 'BalByAcct Transformada' },
      { value: 'SIIF', viewValue: 'Reporte SIIF' },
      { value: 'FDN', viewValue: 'Fechas de Nacimiento' },
      { value: 'AT07', viewValue: 'AT07 Actual' },
      { value: 'CC', viewValue: 'Clientes Consumer' },
      { value: 'CFGESIIFCITI', viewValue: 'Tabla CFGESIIFCITI (Equivalencias Actividad Cliente)' },
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
  }, ];

  resourceGroupsShow: ResourceGroup[];

  constructor(
    // private resourceService: ResourceService,
    private store: Store<fromApp.AppState>,
  ) { }

  ngOnInit() {
    this.onValueChanges();
    this.subscription = this.store
      .select('resources')
      .pipe(map(resourcesState => resourcesState.selectedReport))
      .subscribe((selectedReport: string) => {
        this.selectedReport = selectedReport;
        this.resourceGroupsShow = (this.selectedReport ? this._filterGroup(selectedReport) : []);
      });
  }

  onValueChanges(): void {
    this.resourceControl.valueChanges.subscribe(value => this._setValueResource(value));
  }

  private _setValueResource(value: string) {
    this.selectedResource = value;
    this.store.dispatch(new ResourceActions.SelectResource(value));
    console.log(value);
  }

  private _filterGroup(value: string): ResourceGroup[] {
    if (value) {
      return _filter(this.resourceGroups, value)
    }

    return this.resourceGroups;
  }

}
