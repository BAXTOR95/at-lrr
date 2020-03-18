import { Injectable } from '@angular/core';
import { Store } from '@ngrx/store';
import { Subject } from 'rxjs';

import { Checker } from './checker.model';
import * as fromApp from '../../../core/core.state';

@Injectable({ providedIn: 'root' })
export class CheckerService {
  checkerChanged = new Subject<Checker[]>();

  // private recipes: Recipe[] = [
  //   new Recipe(
  //     'Red Velvet Ice-Cream Cake',
  //     'This is a tasty cake',
  //     'https://cdn-image.myrecipes.com/sites/default/files/styles/medium_2x/public/1553618121/red-velvet-ice-cream-cake-recipe-sl.jpg',
  //     [
  //       new Ingredient('Butter', 3),
  //       new Ingredient('Granulated Sugar', 2),
  //       new Ingredient('Egg', 3),
  //       new Ingredient('Red Liquid Food Coloring', 1),
  //       new Ingredient('Vanilla Extract', 2),
  //       new Ingredient('Unsweetened Cocoa', 1),
  //       new Ingredient('Baking Soda', 1),
  //       new Ingredient('Salt', 1),
  //       new Ingredient('Buttermilk', 2),
  //       new Ingredient('Vanilla Ice Cream', 5),
  //       new Ingredient('Cold Water', 2),
  //       new Ingredient('Unflavored gelatin', 1),
  //       new Ingredient('Heavy Cream', 2),
  //       new Ingredient('Powdered Sugar', 3),
  //       new Ingredient('Blueberries', 2)
  //     ]
  //   ),
  //   new Recipe(
  //     'Hawaiian Pizza',
  //     'This is a delicious pizza',
  //     'https://cdn.sallysbakingaddiction.com/wp-content/uploads/2014/08/' +
  //     'It-doesnt-get-much-better-than-Homemade-Hawaiian-Pizza.-Tropical-paradise-for-dinner-2.jpg',
  //     [
  //       new Ingredient('Yeast', 3),
  //       new Ingredient('Water', 2),
  //       new Ingredient('Flour', 5),
  //       new Ingredient('Oil', 1),
  //       new Ingredient('Salt', 4),
  //       new Ingredient('Sugar', 1),
  //       new Ingredient('Cornmeal', 1),
  //       new Ingredient('Pizza Sauce', 1),
  //       new Ingredient('Shredded Mozzarella', 2),
  //       new Ingredient('Coocked Ham', 1),
  //       new Ingredient('Pineapple Chuncks', 1),
  //       new Ingredient('Cooked Bacon Slices', 3)
  //     ]
  //   )
  // ];

  private checkers: Checker[] = [];

  constructor(private store: Store<fromApp.AppState>) { }

  // setRecipes(checkers: Checker[]) {
  //   this.recipes = recipes;
  //   this.recipesChanged.next(this.recipes.slice());
  // }

  // getRecipes() {
  //   return this.recipes.slice();
  // }

  // getRecipe(index: number) {
  //   return this.recipes[index];
  // }

  // addIngredientsToShoppingList(ingredients: Ingredient[]) {
  //   // this.slService.addIngredients(ingredients);
  //   this.store.dispatch(new ShoppingListActions.AddIngredients(ingredients));
  // }

  // addRecipe(recipe: Recipe) {
  //   this.recipes.push(recipe);
  //   this.recipesChanged.next(this.recipes.slice());
  // }

  // updateRecipe(index: number, newRecipe: Recipe) {
  //   this.recipes[index] = newRecipe;
  //   this.recipesChanged.next(this.recipes.slice());
  // }

  // deleteRecipe(index: number) {
  //   this.recipes.splice(index, 1);
  //   this.recipesChanged.next(this.recipes.slice());
  // }
}
