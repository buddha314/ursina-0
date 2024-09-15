from crafting.models import *

def test_crafting():
    """
    Test the crafting module. Try the handaxe!
    """

    ingredients = ['wood', 'wood', 'stone']
    handaxe_recipe = Recipe('handaxe', ['wood', 'wood', 'stone'], 'handaxe')   
    handaxe = handaxe_recipe.craft(ingredients=['wood', 'wood', 'stone'])
    assert handaxe == 'handaxe', "Should return handaxe with two wood and one stone"
    handaxe = handaxe_recipe.craft(ingredients=['wood', 'stone'])
    assert handaxe == 'handaxe', "Should not return handaxe with only one stone"