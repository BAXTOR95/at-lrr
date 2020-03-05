import { Component, OnInit, ViewEncapsulation, EventEmitter, Output } from '@angular/core';
import { FormControl, Validators } from '@angular/forms';
import { Store } from '@ngrx/store';

import * as fromApp from '../../../store/app.reducer';
import * as WorkflowActions from '../store/workflow.actions';

export interface WorkflowValue {
  value: string;
  viewValue: string;
}

export interface WorkflowGroup {
  type: string;
  names: WorkflowValue[];
}

@Component({
  selector: 'app-workflow-select',
  templateUrl: './workflow-select.component.html',
  styleUrls: [ './workflow-select.component.scss' ]
})
export class WorkflowSelectComponent implements OnInit {

  workflowControl = new FormControl('', Validators.required);

  workflowGroups: WorkflowGroup[] = [ {
    type: 'Archivos de Transmision',
    names: [
      { value: 'AT01', viewValue: 'AT01 - Accionistas del Ente Supervisado' },
      { value: 'AT02', viewValue: 'AT02 - Bienes Recibidos en Pago' },
      { value: 'AT03', viewValue: 'AT03 - Contable' },
      { value: 'AT04', viewValue: 'AT04 - Cartera de Creditos' },
      { value: 'AT05', viewValue: 'AT05 - Captaciones' },
      { value: 'AT06', viewValue: 'AT06 - Transacciones Financieras' },
      { value: 'AT07', viewValue: 'AT07 - Garantias Recibidas' },
      { value: 'AT08', viewValue: 'AT08 - Agencias y Oficinas' },
      { value: 'AT09', viewValue: 'AT09 - Compra y Venta de Inversiones en Titulos Valores' },
      { value: 'AT10', viewValue: 'AT10 - Inversiones' },
      { value: 'AT11', viewValue: 'AT11 - Conformacion de las Disponibilidades, Inversiones y Custodios a Terceros' },
      { value: 'AT12', viewValue: 'AT12 - Consumos de Tarjetas' },
      { value: 'AT13', viewValue: 'AT13 - Reclamos' },
      { value: 'AT14', viewValue: 'AT14 - Instrumentos' },
      { value: 'AT15', viewValue: 'AT15 - Notificacion de Transpaso de Acciones' },
      { value: 'AT16', viewValue: 'AT16 - Empresas Accionistas del Ente Supervisado' },
      { value: 'AT17', viewValue: 'AT17 - Agricola Semanal' },
      { value: 'AT18', viewValue: 'AT18 - Variaciones de las tasas de Credito' },
      { value: 'AT19', viewValue: 'AT19 - Transacciones de Pago' },
      { value: 'AT20', viewValue: 'AT20 - Notas al Pie del Balance' },
      { value: 'AT21', viewValue: 'AT21 - Garantes' },
      { value: 'AT23', viewValue: 'AT23 - Personal' },
      { value: 'AT24', viewValue: 'AT24 - Balance General de Publicacion' },
      { value: 'AT25', viewValue: 'AT25 - Estado de Resultados' },
      { value: 'AT26', viewValue: 'AT26 - Fraude Bancario' },
      { value: 'AT27', viewValue: 'AT27 - Composicion Activa-Pasiva de Organismos Oficiales, P. Juridicas y Naturales' },
      { value: 'AT29', viewValue: 'AT29 - Gravamen' },
      { value: 'AT30', viewValue: 'AT30 - Adquisicion y Venta de Bienes Recibidos en Pago' },
      { value: 'AT31', viewValue: 'AT31 - Movimientos de credito y debito de las operaciones Activas y Pasivas' },
      { value: 'AT32', viewValue: 'AT32 - Fondo de Ahorro Obligatorio para la Viviendaa ' },
      { value: 'AT33', viewValue: 'AT33 - Convenio Cambiario' },
      { value: 'AT34', viewValue: 'AT34 - Grupo Junta Directiva del Ente' },
      { value: 'AT35', viewValue: 'AT35 - 100 Mayores Depositantes de personas Naturales y Juridicas' },
      { value: 'AT36', viewValue: 'AT36 - Lineas de Credito de Utilizacion Automatica' },
      { value: 'AT37', viewValue: 'AT37 - Transferencias Electronicas' },
      { value: 'AT38', viewValue: 'AT38 - Impuesto a las Grandes Transacciones Financieras' },
    ]
  },
  ];

  @Output() reportSelected = new EventEmitter<string>();

  constructor(
    private store: Store<fromApp.AppState>,
  ) { }

  ngOnInit() {
    this.onValueChanges();
  }

  onValueChanges(): void {
    this.workflowControl.valueChanges.subscribe(value => this._setValue(value));
  }

  private _setValue(value: string) {
    this.store.dispatch(new WorkflowActions.SelectReport(value));
  }

}
