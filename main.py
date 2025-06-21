from indexer import create_index, index_data, delete_index
from searcher import full_text_search, filter_by_category

def menu():
    print("\n--- OpenSearch Demo ---")
    print("1. Create Index")
    print("2. Index Sample Data")
    print("3. Full-Text Search")
    print("4. Filter by Category")
    print("5. Delete Index")
    print("0. Exit")

def main():
    while True:
        menu()
        choice = input("Select an option: ")

        if choice == "1":
            create_index()
        elif choice == "2":
            index_data()
        elif choice == "3":
            query = input("Enter search query: ")
            full_text_search(query)
        elif choice == "4":
            category = input("Enter category (e.g., electronics): ")
            filter_by_category(category)
        elif choice == "5":
            delete_index()
        elif choice == "0":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()