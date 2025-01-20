# Définition des recettes et de leurs ingrédients
recettes = {
    "pizza": ["farine", "eau", "sel", "levure", "tomate", "fromage"],
    "salade": ["laitue", "tomate", "concombre", "vinaigre", "huile"],
    "pates_carbonara": ["pates", "creme", "lardons", "fromage", "sel", "poivre"],
    "omelette": ["oeufs", "sel", "poivre", "fromage", "herbes"],
    "sandwich_jambon_beurre": ["pain", "beurre", "jambon", "salade"]
}

# Fonction qui renvoie les recettes réalisables avec les ingrédients fournis
def trouver_recettes(ingredients_utilisateur):
    recettes_possibles = []
    for recette, ingredients in recettes.items():
        if all(ingredient in ingredients_utilisateur for ingredient in ingredients):
            recettes_possibles.append(recette)
    return recettes_possibles

# Exemple d'appel
ingredients_utilisateur = ["pain", "beurre", "jambon", "salade"]
recettes_suggerees = trouver_recettes(ingredients_utilisateur)
print("Recettes possibles:", recettes_suggerees)
