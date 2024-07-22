import json
from quote_generator import load_quotes, get_random_quote

def search_quotes(quotes, keyword):
    results = []
    for category, quote_list in quotes.items():
        for quote in quote_list:
            if keyword.lower() in quote.lower():
                results.append(quote)
    return results

if __name__ == "__main__":
    quotes = load_quotes('quotes.json')
    keyword = input("Enter a keyword to search for quotes: ")
    results = search_quotes(quotes, keyword)
    if results:
        print("Search Results:")
        for result in results:
            print(result)
    else:
        print("No quotes found for the keyword.")
