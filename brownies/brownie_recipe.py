def adjust_ingredients(ingredients, guests):
    """Adjusts ingredient amounts based on the number of guests.

    Args:
        ingredients: A dictionary where keys are ingredient names (strings) and
            values are their amounts (numbers).
        guests: The number of guests to feed.

    Returns:
        A new dictionary with adjusted ingredient amounts, rounded to two
        decimal places. Returns an empty dictionary if guests is zero or negative.
        Raises a TypeError if ingredients is not a dictionary or guests is not a number.
    """
    if not isinstance(ingredients, dict):
        raise TypeError("ingredients must be a dictionary")
    if not isinstance(guests, (int, float)):
        raise TypeError("guests must be a number")
    if guests <= 0:
        return {}

    base_servings = 10
    factor = guests / base_servings
    adjusted_ingredients = {}
    for ingredient, amount in ingredients.items():
        adjusted_amount = round(amount * factor, 2)
        adjusted_ingredients[ingredient] = adjusted_amount
    return adjusted_ingredients


def brownie_program():
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

    steps = [
        "Prepare an 8x4 or 9x5 loaf baking pan with parchment paper. Preheat oven to 350°F.",
        "Melt butter and mix with sugars until paste-like consistency.",
        "Whisk in egg and vanilla extract.",
        "Add flour, cocoa powder, and salt, then mix until combined.",
        "Stir in chocolate chips.",
        "Pour batter into pan, spread evenly, and bake for 26-36 minutes.",
        "Check with a toothpick. If it has a few wet crumbs but no batter, it's done.",
        "Let the brownies cool completely before slicing."
    ]

    while True:
        print("\nWelcome to the Brownies Recipe Program!")
        print("1. How many guests do you plan to feed?")
        print("2. Continue from a step")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == "1":
            try:
                guests = int(input("Enter the number of guests: "))
                if guests <= 0:
                    raise ValueError("Number of guests must be positive.")
                adjusted_ingredients = adjust_ingredients(ingredients, guests)
                print("\nAdjusted Ingredients:")
                for item, amount in adjusted_ingredients.items():
                    print(f"{item}: {amount}")
            except ValueError as e:
                print(f"Invalid input: {e}")
        
        elif choice == "2":
            try:
                step_number = int(input(f"What step were you on? (1-{len(steps)}): "))
                if not (1 <= step_number <= len(steps)):
                    raise ValueError("Invalid step number. Please enter a valid step.")
                print(f"\nStep {step_number}: {steps[step_number - 1]}")
            except ValueError as e:
                print(f"Invalid input: {e}")

        elif choice == "3":
            print("Goodbye! Enjoy your brownies!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    brownie_program()