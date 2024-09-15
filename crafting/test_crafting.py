from crafting.models import *

def test_crafting():
    """
    Test the crafting module. Try the handaxe!
    """

    # Delcare a recipe for a handaxe
    handaxe_recipe = Recipe('handaxe', ['wood', 'wood', 'stone'], 'HandAxe')   
    # Send in correct ingredients
    handaxe = handaxe_recipe.craft(ingredients=['wood', 'wood', 'stone'])
    assert isinstance(handaxe, HandAxe), "Should return handaxe with two wood and one stone"
    # Send in incorrect ingredients
    handaxe = handaxe_recipe.craft(ingredients=['wood', 'stone'])
    assert handaxe == None, "Should not return handaxe with only one wood"
    # Send in correct ingredients in different order
    handaxe = handaxe_recipe.craft(ingredients=['wood', 'stone', 'stone', 'wood'])
    assert isinstance(handaxe, HandAxe), "Should return handaxe with two wood and one stone in different order"