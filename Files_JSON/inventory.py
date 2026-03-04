import json

# Task 1 — Read the inventory
def read_books(): # defining function
    with open('inventory.json', 'r') as file: # Open files in read mode with auto close
        inventory = json.load(file) # To load JSON File to Dictionary and assigned to variable 'inventory'
    return inventory # return data

books = read_books() # calling read_books functions to get data from file
print("Total no. of books: ", len(books)) # print total no. of books

# Task 2 — Update and save
def save_books(data):  # defining function
    with open('inventory.json', 'w') as file: # Open files in write mode with auto close
        json.dump(data, file, indent=4) # To write Dictionay to JSON File with 4 spaces indentation

new_book = {"title": "Atomic Habits", "author": "James Clear", "price": 14.99, "in_stock": True} # Assign a new JSON book information
books.append(new_book) # Add the new_book value to existing books
save_books(books) # calling save_books function to save the data

# Task 3 — Display the inventory
books = read_books() # calling read_books functions to get data from file

for book in books: # looping the all books data
    print(f"Title: {book["title"]} | Author: {book["author"]} | Price: ${book["price"]}") # Prints each book informaton by accessing key