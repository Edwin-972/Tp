% Définir les ingrédients des recettes
recette(pizza, [farine, eau, sel, levure, tomate, fromage]).
recette(salade, [laitue, tomate, concombre, vinaigre, huile]).
recette(pates_carbonara, [pates, creme, lardons, fromage, sel, poivre]).
recette(omelette, [oeufs, sel, poivre, fromage, herbes]).
recette(sandwich_jambon_beurre, [pain, beurre, jambon, salade]).

% Règle pour vérifier si une recette est réalisable avec les ingrédients donnés
realisable(Recette, IngredientsUtilisateur) :-
    recette(Recette, IngredientsRecette),
    subset(IngredientsRecette, IngredientsUtilisateur).

% Vérifie si tous les éléments d'une liste sont présents dans une autre liste
subset([], _).
subset([H|T], L) :- member(H, L), subset(T, L).