import { Routes } from '@angular/router';
import { RESEARCH_PREVIEW_ROUTES } from './research-preview.routes';

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
    path: 'methodik',
    title: 'Methodik und Grenzen · 12 Axes Deutschland',
    loadComponent: () =>
      import('./pages/methodology/methodology').then((module) => module.MethodologyPage),
  },
  ...RESEARCH_PREVIEW_ROUTES,
  {
    path: '**',
    title: 'Seite nicht gefunden · 12 Axes Deutschland',
    loadComponent: () => import('./pages/not-found/not-found').then((module) => module.NotFound),
  },
];
