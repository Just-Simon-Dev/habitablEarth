import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { MainPageComponent } from './main-page/main-page.component';
import { AboutPageComponent } from './about-page/about-page.component';
import { InformationPageComponent } from './information-page/information-page.component';

const routes: Routes = [
	{path: '', component: MainPageComponent},
	{path: 'about', component: AboutPageComponent},
	{path: 'information', component: InformationPageComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
