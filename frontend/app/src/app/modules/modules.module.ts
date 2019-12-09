import { NgModule } from '@angular/core';

import { BalanceAccountComponent } from './balance-account/balance-account.component';
import { ViewsComponent } from './views/views.component';
import { WorkflowComponent } from './workflow/workflow.component';

import { CheckerModule } from './checker/checker.module';
import { ResourcesModule } from './resources/resources.module';

@NgModule({
  declarations: [
    BalanceAccountComponent,
    ViewsComponent,
    WorkflowComponent
  ],
  imports: [
    CheckerModule,
    ResourcesModule
  ],
  exports: [
  ],

})
export class ModulesModule { }
