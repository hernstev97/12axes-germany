import { ChangeDetectionStrategy, Component } from '@angular/core';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-methodology-page',
  standalone: true,
  imports: [RouterLink],
  templateUrl: './methodology.html',
  styleUrl: './methodology.scss',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class MethodologyPage {}
