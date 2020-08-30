import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class TarjetaService {
  myApUrl = 'http://127.0.0.1:8000/';
  myApiUrl = 'api/events/';

  constructor(private http: HttpClient) { }
}
