import pytest
from brownie_recipe import adjust_ingredients  # Import the function

def test_adjust_ingredients():
    ingredients = {
        "butter (Tablespoons)": 6,
        "granulated sugar (cup)": 0.5,
        "light brown sugar (Tablespoons)": 6,
        "egg": 1,
        "vanilla extract (Tablespoons)": 0.5,
        "salt (teaspoon)": 0.125,
        "all-purpose flour (Tablespoons)": 5,
        "unsweetened cocoa powder (Tablespoons)": 6,
        "semisweet chocolate chips (cup)": 0.33
    }

    assert adjust_ingredients(ingredients, 20) == {
        "butter (Tablespoons)": 12.0,
        "granulated sugar (cup)": 1.0,
        "light brown sugar (Tablespoons)": 12.0,
        "egg": 2.0,
        "vanilla extract (Tablespoons)": 1.0,
        "salt (teaspoon)": 0.25,
        "all-purpose flour (Tablespoons)": 10.0,
        "unsweetened cocoa powder (Tablespoons)": 12.0,
        "semisweet chocolate chips (cup)": 0.66
    }
    assert adjust_ingredients(ingredients, 5) == {
        "butter (Tablespoons)": 3.0,
        "granulated sugar (cup)": 0.25,
        "light brown sugar (Tablespoons)": 3.0,
        "egg": 0.5,
        "vanilla extract (Tablespoons)": 0.25,
        "salt (teaspoon)": 0.06,
        "all-purpose flour (Tablespoons)": 2.5,
        "unsweetened cocoa powder (Tablespoons)": 3.0,
        "semisweet chocolate chips (cup)": 0.17
    }
    assert adjust_ingredients(ingredients, 0) == {}
    assert adjust_ingredients(ingredients, 15) == {
        "butter (Tablespoons)": 9.0,
        "granulated sugar (cup)": 0.75,
        "light brown sugar (Tablespoons)": 9.0,
        "egg": 1.5,
        "vanilla extract (Tablespoons)": 0.75,
        "salt (teaspoon)": 0.19,
        "all-purpose flour (Tablespoons)": 7.5,
        "unsweetened cocoa powder (Tablespoons)": 9.0,
        "semisweet chocolate chips (cup)": 0.5
    }
    assert adjust_ingredients(ingredients, 2.5) == {
        "butter (Tablespoons)": 1.5,
        "granulated sugar (cup)": 0.12,
        "light brown sugar (Tablespoons)": 1.5,
        "egg": 0.25,
        "vanilla extract (Tablespoons)": 0.12,
        "salt (teaspoon)": 0.03,
        "all-purpose flour (Tablespoons)": 1.25,
        "unsweetened cocoa powder (Tablespoons)": 1.5,
        "semisweet chocolate chips (cup)": 0.08
    }

    # Test for invalid input
    with pytest.raises(TypeError):
        adjust_ingredients("not a dict", 10)
    with pytest.raises(TypeError):
        adjust_ingredients(ingredients, "not a number")
        
if __name__ == "__main__":
    pytest.main()