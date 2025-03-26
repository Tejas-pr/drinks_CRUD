import { Component } from '@angular/core';
import { Drink, DrinkService } from '../../services/drink.service';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';


@Component({
  selector: 'app-drink-list',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './drink-list.component.html',
  styleUrl: './drink-list.component.scss'
})
export class DrinkListComponent {
  drinks: Drink[] = []

  constructor(private drinkService: DrinkService) {}

  ngOnInit() {
    this.drinkService.getDrinks().subscribe(
      (response) => {
        console.log('API Response:', response); // Debugging
        this.drinks = response.drinks; // ✅ Extract array from object
      },
      (error) => {
        console.error('Error fetching drinks:', error);
      }
    );
  }
  
  
}
