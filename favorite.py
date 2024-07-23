import json
from quote_generator import load_quotes, get_random_quote

def save_favorite_quote(quote, filename='favorites.json'):
    try:
        with open(filename, 'r') as file:
            favorites = json.load(file)
    except FileNotFoundError:
        favorites = []

    favorites.append(quote)
    with open(filename, 'w') as file:
        json.dump(favorites, file, indent=4)

def view_favorite_quotes(filename='favorites.json'):
    try:
        with open(filename, 'r') as file:
            favorites = json.load(file)
    except FileNotFoundError:
        favorites = []
    return favorites

if __name__ == "__main__":
    quotes = load_quotes('quotes.json')
    category = input("Enter a category (Inspirational, Funny, Life, Love): ")
    if category in quotes:
        quote = get_random_quote(quotes, category)
        print("Quote of the Day:")
        print(quote)
        if input("Save this quote to favorites? (y/n): ").lower() == 'y':
            save_favorite_quote(quote)
        if input("View favorite quotes? (y/n): ").lower() == 'y':
            favorites = view_favorite_quotes()
            for favorite in favorites:
                print(favorite)
    else: 
        print("Category not found.")
