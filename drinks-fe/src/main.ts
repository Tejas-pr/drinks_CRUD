import { bootstrapApplication } from '@angular/platform-browser';
import { AppComponent } from './app/app.component';
import { provideHttpClient } from '@angular/common/http';
import { provideRouter } from '@angular/router'; // ✅ Import provideRouter
import { routes } from './app/app.routes';

bootstrapApplication(AppComponent, {
  providers: [
    provideHttpClient(),  // ✅ Correct way to provide HttpClient
    provideRouter(routes) // ✅ Correct way to provide routes
  ]
}).catch(err => console.error(err));
