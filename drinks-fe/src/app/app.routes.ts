import { Routes } from '@angular/router';
import { DrinkListComponent } from './components/drink-list/drink-list.component';
import { DrinkDetailComponent } from './components/drink-detail/drink-detail.component';

export const routes: Routes = [
    { path: '', component: DrinkListComponent },
    { path: 'drink/:id', component: DrinkDetailComponent }
];
