import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { CountriesMapModule } from 'countries-map';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { MapComponent } from './map/map.component';
import { NavbarComponent } from './navbar/navbar.component';
import { AboutPageComponent } from './about-page/about-page.component';
import { InformationPageComponent } from './information-page/information-page.component';
import { MainPageComponent } from './main-page/main-page.component';
import { FooterComponent } from './footer/footer.component';

@NgModule({
  declarations: [
    AppComponent,
    MapComponent,
    NavbarComponent,
    AboutPageComponent,
    InformationPageComponent,
    MainPageComponent,
    FooterComponent
  ],
  imports: [
    BrowserModule,
	CountriesMapModule,
	HttpClientModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
