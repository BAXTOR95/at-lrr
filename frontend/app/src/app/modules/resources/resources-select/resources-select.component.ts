import { Component, OnInit, ViewEncapsulation, EventEmitter, Output } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { Observable } from 'rxjs';
import { startWith, map } from 'rxjs/operators';

import { ResourceService } from '../resources.service';


export interface ResourceValue {
  value: string;
  viewValue: string;
}

export interface ResourceGroup {
  type: string;
  names: ResourceValue[];
}


export const _filter = (opt: ResourceValue[], value: string): ResourceValue[] => {
  const filterValue = value.toLowerCase();

  return opt.filter(item => item.value.toLowerCase().indexOf(filterValue) === 0);
};



@Component({
  selector: 'app-resources-select',
  templateUrl: './resources-select.component.html',
  styleUrls: [ './resources-select.component.scss' ],
  encapsulation: ViewEncapsulation.None
})
export class ResourcesSelectComponent implements OnInit {

  resourceForm: FormGroup = this._formBuilder.group({
    resourceGroup: '',
  });

  resourceGroups: ResourceGroup[] = [ {
    type: 'Manual',
    names: [
      { value: 'CND', viewValue: 'CORPORATIVO NO DIRIGIDA.XLS' },
      // {value: '', viewValue: 'PlantillaTMPCorporativoNoDirEnlazado.xlsx'},
      // {value: '', viewValue: 'SOBREGIROS_ICG.XLS'},
      { value: 'SC', viewValue: 'TMP_SobregirosConsumer.txt' },
      { value: 'RICG', viewValue: 'Rendimientos_Corporativo.xls' },
      { value: 'MM', viewValue: 'Migrated Mortgage' },
      { value: 'GICG', viewValue: 'Insumo Gaveta (Agricola, Turismo, Manufactura e Hipotecario)' },
      { value: 'CD', viewValue: 'RPT_STG_Dirigidas' },
      // 'RPT_STG_Dirigidas_AGRICOLA_CONSUMER.txt',
      // 'RPT_STG_Dirigidas_AGRICOLA_CORPORATE.txt',
      // 'RPT_STG_Dirigidas_HIPOTECARIO_CORTO_PLAZO.txt',
      // 'RPT_STG_Dirigidas_HIPOTECARIO_LARGO_PLAZO.txt',
      // 'RPT_STG_Dirigidas_MANUFACTURA.txt',
      // 'RPT_STG_Dirigidas_MICROFINANCIERO.txt',
      // 'RPT_STG_Dirigidas_TURISMO.txt',
      // {value: '', viewValue: 'CITIBANK  AT-04 MES AÑO.xlsx(IngresoFamModalidadHipo)'},
      { value: 'MISP', viewValue: 'MIS Provisiones' },
      { value: 'PPRRHH', viewValue: 'Préstamos Sobre Prestaciones - Sudeban.xls' },
    ]
  }, {
    type: 'Automatic',
    names: [
      { value: 'AT04CRE', viewValue: 'AT04CRE(cosmos)' },
      { value: 'LNP860', viewValue: 'Lnp860' },
      { value: 'VNP003T', viewValue: 'VNP003T' },
      { value: 'AH', viewValue: 'ACCOUNT HISTORY.txt' },
      { value: 'BBAT', viewValue: 'BalByAcctTransformada.txt' },
      { value: 'SIIF', viewValue: 'Reporte_SIIF.txt' },
      // 'clientesconsumer_05.txt',
      { value: 'FDN', viewValue: 'TB_FDN.txt' },
      { value: 'AT07', viewValue: 'AT07.txt' },
    ]
  }
  ];

  resourceGroupOptions: Observable<ResourceGroup[]>;

  @Output() resourceSelected = new EventEmitter<string>();

  constructor (
    private _formBuilder: FormBuilder,
    private resourceService: ResourceService) { }

  ngOnInit() {
    this.resourceGroupOptions = this.resourceForm.get('resourceGroup').valueChanges
      .pipe(
        startWith(''),
        map(value => this._filterGroup(value))
      );
  }

  private _filterGroup(value: ResourceValue): ResourceGroup[] {
    if (value) {
      this.resourceSelected.emit(value.value);
      this.resourceService.setResourceSelected(value.value);
      return this.resourceGroups
        .map(group => ({ type: group.type, names: _filter(group.names, value.viewValue) }))
        .filter(group => group.names.length > 0);
    }

    return this.resourceGroups;
  }

}
