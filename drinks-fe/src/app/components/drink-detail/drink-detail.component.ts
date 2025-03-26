import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { DrinkService } from '../../services/drink.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-drink-detail',
  imports: [CommonModule],
  templateUrl: './drink-detail.component.html',
  styleUrl: './drink-detail.component.scss'
})
export class DrinkDetailComponent implements OnInit {
  drink: any;
  nutrition: any[] = [];

  constructor(private route: ActivatedRoute, private drinkService: DrinkService) {}

  ngOnInit() {
    const id = this.route.snapshot.paramMap.get('id');
    if (id) {
      this.drinkService.getDrinkById(id).subscribe(
        (response) => {
          this.drink = response.data;
          this.nutrition = response.nutrition;
        },
        (error) => {
          console.error('Error fetching drink details:', error);
        }
      );
    }
  }
}
