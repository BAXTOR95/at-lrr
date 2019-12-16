import { Component, OnInit, ViewEncapsulation, EventEmitter, Output } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { Observable } from 'rxjs';
import { startWith, map } from 'rxjs/operators';

export interface ResourceGroup {
  type: string;
  names: string[];
}

export const _filter = (opt: string[], value: string): string[] => {
  const filterValue = value.toLowerCase();

  return opt.filter(item => item.toLowerCase().indexOf(filterValue) === 0);
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
      'CORPORATIVO NO DIRIGIDA.XLS',
      'PlantillaTMPCorporativoNoDirEnlazado.xlsx',
      'SOBREGIROS_ICG.XLS',
      'TMP_SobregirosConsumer.txt',
      'Rendimientos_Corporativo.xls',
      'Migrated Mortgage',
      'Insumo Gaveta (Agricola, Turismo, Manufactura e Hipotecario)',
      'RPT_STG_Dirigidas_AGRICOLA_CONSUMER.txt',
      'RPT_STG_Dirigidas_AGRICOLA_CORPORATE.txt',
      'RPT_STG_Dirigidas_HIPOTECARIO_CORTO_PLAZO.txt',
      'RPT_STG_Dirigidas_HIPOTECARIO_LARGO_PLAZO.txt',
      'RPT_STG_Dirigidas_MANUFACTURA.txt',
      'RPT_STG_Dirigidas_MICROFINANCIERO.txt',
      'RPT_STG_Dirigidas_TURISMO.txt',
      'CITIBANK  AT-04 MES AÑO.xlsx(IngresoFamModalidadHipo)',
      'MIS Provisiones',
      'Préstamos Sobre Prestaciones - Sudeban.xls',
      'Rendimientos_Corporativo.xls'
    ]
  }, {
    type: 'Automatic',
    names: [
      'AT04CRE(cosmos)',
      'Lnp860',
      'VNP003T',
      'ACCOUNT HISTORY.txt',
      'STMT_ATAR.txt',
      'STMT_CARD_ACCOUNT.txt',
      'STATEMENT COMPLEMENTO 10.000_CANCELACION_CAPITAL_10000.txt',
      'STATEMENT COMPLEMENTO 11.110_CANCELACION_INTER_11110.txt',
      'STATEMENT.txt',
      'BalByAcctTransformada.txt',
      'Reporte_SIIF.txt',
      'clientesconsumer_05.txt',
      'TB_FDN.txt'
    ]
  }, {
    type: 'DTS',
    names: [ 'VZDWAMBS.pven' ]
  }
  ];

  resourceGroupOptions: Observable<ResourceGroup[]>;

  @Output() resourceSelected = new EventEmitter<string>();

  constructor (private _formBuilder: FormBuilder) { }

  ngOnInit() {
    this.resourceGroupOptions = this.resourceForm.get('resourceGroup').valueChanges
      .pipe(
        startWith(''),
        map(value => this._filterGroup(value))
      );
  }

  private _filterGroup(value: string): ResourceGroup[] {
    if (value) {
      this.resourceSelected.emit(value);
      return this.resourceGroups
        .map(group => ({ type: group.type, names: _filter(group.names, value) }))
        .filter(group => group.names.length > 0);
    }

    return this.resourceGroups;
  }

}
