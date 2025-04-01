import json 
import os 

data_file = 'library.txt'

# 📂 Function to load the library from the file
# Reads the library data from 'library.txt' if it exists; otherwise, returns an empty list
def load_library():
    if os.path.exists(data_file):
        with open(data_file, 'r') as file:
            return json.load(file)
    return []  

# 💾 Function to save the library to the file
# Writes the current library data to 'library.txt' in JSON format
def save_library(library):
    with open(data_file, 'w') as file:
        json.dump(library, file, indent=4)  
        
# 📚 Function to add a new book to the library
def add_book(library):
    title = input("📖 Enter the title of the book: ").strip().lower()  # Convert to lowercase
    author = input("✍️ Enter the author of the book: ").strip()
    year = input("📅 Enter the year of the book: ").strip()
    genre = input("🎭 Enter the genre of the book: ").strip()
    read = input("✅ Have you read the book? (yes/no): ").strip().lower() == 'yes'

    for book in library:
        if book['title'].lower() == title:
            print(f"⚠️ Book '{title}' already exists in the library!")
            return  

    new_book = {
        'title': title,   
        'author': author,
        'year': year,
        'genre': genre,
        'read': read
    }
    library.append(new_book)
    save_library(library)
    print(f'✅ Book "{title}" added successfully.')  

# 🗑️ Function to remove a book from the library
def remove_book(library):
    title = input("🗂️  Enter the title of the book to remove: ").strip().lower()
    initial_length = len(library)
    updated_library = [book for book in library if book['title'].lower() != title]
    
    if len(updated_library) < initial_length:
        save_library(updated_library)
        print(f'🗑️  Book "{title}" removed successfully! ✅')
    else:
        print(f'⚠️  Book "{title}" not found in the library! ❌')
    
    library.clear()  
    library.extend(updated_library)  

# 🔍 Function to search for books
def search_library(library):
    library = load_library()  

    search_term = input("🔎 Enter book title or author name to search: ").lower()
    results = [book for book in library if search_term in book['title'].lower() or search_term in book['author'].lower()]

    if results:
        for book in results:
            status = "✅ Read" if book['read'] else "📖 Unread"
            print(f"📚 {book['title']} by {book['author']} - 📅 {book['year']} - 🎭 {book['genre']} - {status}")
    else:
        print(f"❌ No books found matching '{search_term}'.")

# 📜 Function to display all books
def display_all_books(library):
    if library:
        for book in library:
            status = "✅ Read" if book['read'] else "📖 Unread"
            print(f"📚 {book['title']} by {book['author']} - 📅 {book['year']} - 🎭 {book['genre']} - {status}") 
    else:
        print("📂 The library is empty!")

# 📊 Function to display statistics about the library
def display_statistics(library):
    total_books = len(library)
    read_books = len([book for book in library if book['read']])
    percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0

    print(f"📚 Total books: {total_books}")
    print(f"📖 Percentage read: {percentage_read:.2f}%") 

# 🏠 Main function to display the menu and handle user input
def main():
    library = load_library()
    user = input("\n👤 Enter your name: ")
    print(f"🎉 Welcome to the Library Manager, '{user}' 📖") 
    while True:
        print("\n📌 Menu\n")
        print("1️⃣  📖  Add a book")
        print("2️⃣  🗑️  Remove a book")
        print("3️⃣  🔍  Search the library")
        print("4️⃣  📚  Display all books")
        print("5️⃣  📊  Display statistics")
        print("6️⃣  ❌  Exit")    

        choice = input("\n🎯 Enter your choice: ") 
        if choice == '1':
            add_book(library)
        elif choice == '2':
            remove_book(library)   
        elif choice == '3':
            search_library(library)
        elif choice == '4':
            display_all_books(library)
        elif choice == '5':
            display_statistics(library)    
        elif choice == '6':
            print("\n👋 Exiting... Have a great day! 🚀\n")
            break
        else:
            print("\n⚠️ Invalid choice. Please try again! ❌")

if __name__ == '__main__':
    main()
