# Recipe Manager Application

# Data structures to store recipes and logs
recipes = {}
logs = []

# Utility functions

def save_to_file():
    """Save the recipes and logs to a text file."""
    with open('recipes.txt', 'w') as file:
        for name, details in recipes.items():
            ingredients = ','.join(details['ingredients'])
            steps = ','.join(details['steps'])
            file.write(f"{name};{ingredients};{steps};{details['prep_time']}\n")
        file.write("LOGS\n")
        for log in logs:
            file.write(log + "\n")

def load_from_file():
    """Load recipes and logs from a text file."""
    try:
        with open('recipes.txt', 'r') as file:
            lines = file.readlines()
            reading_logs = False
            for line in lines:
                line = line.strip()
                if line == "LOGS":
                    reading_logs = True
                elif reading_logs:
                    logs.append(line)
                else:
                    name, ingredients, steps, prep_time = line.split(';')
                    recipes[name] = {
                        'ingredients': ingredients.split(','),
                        'steps': steps.split(','),
                        'prep_time': prep_time
                    }
    except FileNotFoundError:
        pass

# Main functional components

def add_recipe():
    """Add a recipe to the manager."""
    name = input("Enter the recipe name: ")
    ingredients = input("Enter the ingredients (comma-separated): ").split(',')
    steps = input("Enter the steps (comma-separated): ").split(',')
    prep_time = input("Enter the preparation time: ")
    recipes[name] = {
        'ingredients': ingredients,
        'steps': steps,
        'prep_time': prep_time
    }
    logs.append(f"Added recipe {name}")

def view_recipes():
    """View all recipes."""
    for name, details in recipes.items():
        print(f"\nRecipe: {name}")
        print("Ingredients:", ', '.join(details['ingredients']))
        print("Steps:", ' -> '.join(details['steps']))
        print(f"Preparation Time: {details['prep_time']}")

def edit_recipe():
    """Edit a recipe."""
    name = input("Enter the recipe name to edit: ")
    if name in recipes:
        print("1. Edit Ingredients")
        print("2. Edit Steps")
        print("3. Edit Preparation Time")
        choice = input("Choose what you'd like to edit: ")
        if choice == '1':
            ingredients = input("Enter the new ingredients (comma-separated): ").split(',')
            recipes[name]['ingredients'] = ingredients
        elif choice == '2':
            steps = input("Enter the new steps (comma-separated): ").split(',')
            recipes[name]['steps'] = steps
        elif choice == '3':
            prep_time = input("Enter the new preparation time: ")
            recipes[name]['prep_time'] = prep_time
        logs.append(f"Edited recipe {name}")
    else:
        print("Recipe not found!")

def delete_recipe():
    """Delete a recipe."""
    name = input("Enter the recipe name to delete: ")
    if name in recipes:
        del recipes[name]
        logs.append(f"Deleted recipe {name}")
    else:
        print("Recipe not found!")

def search_recipe():
    """Search for a recipe by name or ingredient."""
    term = input("Enter the search term: ")
    found = False
    for name, details in recipes.items():
        if term.lower() in name.lower() or term.lower() in ' '.join(details['ingredients']).lower():
            print(f"\nRecipe: {name}")
            print("Ingredients:", ', '.join(details['ingredients']))
            print("Steps:", ' -> '.join(details['steps']))
            print(f"Preparation Time: {details['prep_time']}")
            found = True
    if not found:
        print("No matching recipes found!")

def view_logs():
    """View logs."""
    for log in logs:
        print(log)

# Main program

def main():
    load_from_file()  # Load recipes and logs from file at the start
    while True:
        print("\nRecipe Manager Menu:")
        print("1. Add Recipe")
        print("2. View Recipes")
        print("3. Edit Recipe")
        print("4. Delete Recipe")
        print("5. Search Recipe")
        print("6. View Logs")
        print("7. Save and Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_recipe()
        elif choice == '2':
            view_recipes()
        elif choice == '3':
            edit_recipe()
        elif choice == '4':
            delete_recipe()
        elif choice == '5':
            search_recipe()
        elif choice == '6':
            view_logs()
        elif choice == '7':
            save_to_file()  # Save recipes and logs to file before exiting
            break
        else:
            print("Invalid choice! Please choose again.")

if __name__ == "__main__":
    main()
