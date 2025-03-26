import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { DrinkService } from '../../services/drink.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-drink-detail',
  imports: [CommonModule],
  templateUrl: './drink-detail.component.html',
})
export class DrinkDetailComponent implements OnInit {
  drink: any;

  constructor(private route: ActivatedRoute, private drinkService: DrinkService) {}

  ngOnInit() {
    const id = this.route.snapshot.paramMap.get('id');
    if (id) {
      this.drinkService.getDrinkById(id).subscribe(
        (response) => {
          this.drink = response.data;
        },
        (error) => {
          console.error('Error fetching drink details:', error);
        }
      );
    }
  }
}
