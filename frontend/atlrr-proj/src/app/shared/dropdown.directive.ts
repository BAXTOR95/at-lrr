import { ElementRef } from '@angular/core';
import { Directive, HostListener, HostBinding } from '@angular/core';

@Directive({
  selector: '[appDropdown]',
})
export class DropdownDirective {
  private isOpen = false;

  @HostBinding('class.show') get opened() {
    return this.isOpen;
  }

  @HostListener('click') toggleOpen() {
    this.isOpen = !this.isOpen;
    if (this.isOpen) {
      this.elRef.nativeElement
        .querySelector('.dropdown-menu')
        .classList.add('show');
    } else {
      this.elRef.nativeElement
        .querySelector('.dropdown-menu')
        .classList.remove('show');
    }
  }
  @HostListener('document:click', ['$event']) close(event: Event) {
    const inside: boolean = this.elRef.nativeElement.contains(event.target);
    if (!inside) {
      this.isOpen = false;
      this.elRef.nativeElement
        .querySelector('.dropdown-menu')
        .classList.remove('show');
    }
  }

  constructor(private elRef: ElementRef) {}
}
