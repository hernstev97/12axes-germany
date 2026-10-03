import { Routes } from '@angular/router';

export const routes: Routes = [
  {
    path: '',
    pathMatch: 'full',
    title: '12 Axes Deutschland',
    loadComponent: () => import('./pages/home/home').then((module) => module.Home),
  },
  {
    path: 'projekt',
    title: 'Projektstand · 12 Axes Deutschland',
    loadComponent: () => import('./pages/project/project').then((module) => module.Project),
  },
  {
    path: '**',
    title: 'Seite nicht gefunden · 12 Axes Deutschland',
    loadComponent: () => import('./pages/not-found/not-found').then((module) => module.NotFound),
  },
];
