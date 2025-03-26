import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Drink {
  id: number;
  name: string;
  description: string;
}

@Injectable({
  providedIn: 'root'
})
export class DrinkService {

  private apiUrl = 'http://127.0.0.1:8000/drinks/';

  constructor(private http: HttpClient) { }

  getDrinks(): Observable<any> {
    return this.http.get<any>(this.apiUrl);
  }

  getDrinkById(id: string): Observable<any> {
    return this.http.get<any>(`${this.apiUrl}${id}`);
  }
}
