import { Injectable } from '@angular/core';
import { HttpClient } from "@angular/common/http"

@Injectable({
  providedIn: 'root'
})
export class TemperatureForCountryService {

	private url: string | undefined
	constructor(private http: HttpClient) { }
	getTemperatures(end_date: string | null, country: string){
		this.url = "http://127.0.0.1:5000/api/countries"
		return this.http.get(`${this.url}?end_date=${end_date}&country=${country}`)
	}
}
