import type { Routes } from '@angular/router';

/** Used only by the explicit local research build configuration. */
export const RESEARCH_PREVIEW_ROUTES: Routes = [
  {
    path: 'forschungsentwurf',
    title: 'Forschungsentwurf · 12 Axes Deutschland',
    loadComponent: () =>
      import('./research-preview/policy-preview').then((module) => module.PolicyPreview),
  },
];
