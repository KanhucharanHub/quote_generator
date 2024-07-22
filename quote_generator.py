import json
import random
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, 
    QLineEdit, QMessageBox, QTextEdit, QHBoxLayout, QComboBox, QSizePolicy
)
from PyQt5.QtGui import QFont

# Load quotes from a JSON file
def load_quotes(filename='quotes.json'):
    with open(filename, 'r') as file:
        quotes = json.load(file)
    return quotes

# Get a random quote from a specific category
def get_random_quote(quotes, category):
    return random.choice(quotes[category]).strip()

# Search for quotes containing a specific keyword
def search_quotes(quotes, keyword):
    results = []
    for category, quote_list in quotes.items():
        for quote in quote_list:
            if keyword.lower() in quote.lower():
                results.append(quote)
    return results

# Save a favorite quote to a JSON file
def save_favorite_quote(quote, filename='favorites.json'):
    try:
        with open(filename, 'r') as file:
            favorites = json.load(file)
    except FileNotFoundError:
        favorites = []

    favorites.append(quote)
    with open(filename, 'w') as file:
        json.dump(favorites, file, indent=4)

# View favorite quotes from a JSON file
def view_favorite_quotes(filename='favorites.json'):
    try:
        with open(filename, 'r') as file:
            favorites = json.load(file)
    except FileNotFoundError:
        favorites = []
    return favorites

# Main application class
class QuoteGeneratorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.quotes = load_quotes()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Quote Generator by Karan')
        
        self.layout = QVBoxLayout()

        # Quote Generator
        self.category_label = QLabel('Select Category:', self)
        self.category_label.setFont(QFont("Arial", 14))
        self.layout.addWidget(self.category_label)

        self.category_input = QComboBox(self)
        self.category_input.addItems(self.quotes.keys())
        self.category_input.setFont(QFont("Arial", 14))
        self.layout.addWidget(self.category_input)

        self.generate_button = QPushButton('Generate Quote', self)
        self.generate_button.setFont(QFont("Arial", 14))
        self.generate_button.setStyleSheet("background-color: #ADD8E6;")
        self.generate_button.clicked.connect(self.display_quote)
        self.layout.addWidget(self.generate_button)

        self.quote_label = QLabel('', self)
        self.quote_label.setFont(QFont("Arial", 14))
        self.quote_label.setWordWrap(True)
        self.quote_label.setStyleSheet("padding: 10px; border: 1px solid #ADD8E6;")
        self.layout.addWidget(self.quote_label)

        # Save to Favorites
        self.save_button = QPushButton('Save to Favorites', self)
        self.save_button.setFont(QFont("Arial", 14))
        self.save_button.setStyleSheet("background-color: #90EE90;")
        self.save_button.clicked.connect(self.save_quote)
        self.layout.addWidget(self.save_button)

        # View Favorites
        self.view_favorites_button = QPushButton('View Favorites', self)
        self.view_favorites_button.setFont(QFont("Arial", 14))
        self.view_favorites_button.setStyleSheet("background-color: #FFD700;")
        self.view_favorites_button.clicked.connect(self.view_favorites)
        self.layout.addWidget(self.view_favorites_button)

        self.favorites_text = QTextEdit(self)
        self.favorites_text.setFont(QFont("Arial", 14))
        self.favorites_text.setReadOnly(True)
        self.favorites_text.setStyleSheet("padding: 10px; border: 1px solid #FFD700;")
        self.layout.addWidget(self.favorites_text)

        # Search Quotes
        self.search_label = QLabel('Enter Keyword to Search:', self)
        self.search_label.setFont(QFont("Arial", 14))
        self.layout.addWidget(self.search_label)

        self.search_input = QLineEdit(self)
        self.search_input.setFont(QFont("Arial", 14))
        self.layout.addWidget(self.search_input)

        self.search_button = QPushButton('Search Quotes', self)
        self.search_button.setFont(QFont("Arial", 14))
        self.search_button.setStyleSheet("background-color: #FFA07A;")
        self.search_button.clicked.connect(self.search_quotes)
        self.layout.addWidget(self.search_button)

        self.search_results = QTextEdit(self)
        self.search_results.setFont(QFont("Arial", 14))
        self.search_results.setReadOnly(True)
        self.search_results.setStyleSheet("padding: 10px; border: 1px solid #FFA07A;")
        self.layout.addWidget(self.search_results)

        self.setLayout(self.layout)
        
        # Set the window width
        self.setFixedWidth(600)

    def display_quote(self):
        category = self.category_input.currentText()
        if category in self.quotes:
            quote = get_random_quote(self.quotes, category)
            self.quote_label.setText(quote)
        else:
            QMessageBox.critical(self, 'Error', 'Category not found.')

    def save_quote(self):
        quote = self.quote_label.text()
        if quote:
            save_favorite_quote(quote)
            QMessageBox.information(self, 'Success', 'Quote saved to favorites.')
        else:
            QMessageBox.critical(self, 'Error', 'No quote to save.')

    def view_favorites(self):
        favorites = view_favorite_quotes()
        if favorites:
            self.favorites_text.setPlainText('\n'.join(favorites))
        else:
            self.favorites_text.setPlainText('No favorite quotes found.')

    def search_quotes(self):
        keyword = self.search_input.text()
        if keyword:
            results = search_quotes(self.quotes, keyword)
            if results:
                self.search_results.setPlainText('\n'.join(results))
            else:
                self.search_results.setPlainText('No quotes found for the keyword.')
        else:
            QMessageBox.critical(self, 'Error', 'Please enter a keyword to search.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = QuoteGeneratorApp()
    ex.show()
    sys.exit(app.exec_())
