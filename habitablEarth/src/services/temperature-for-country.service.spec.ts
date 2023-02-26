import { TestBed } from '@angular/core/testing';

import { TemperatureForCountryService } from './temperature-for-country.service';

describe('TemperatureForCountryService', () => {
  let service: TemperatureForCountryService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(TemperatureForCountryService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
