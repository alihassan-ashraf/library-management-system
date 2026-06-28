import streamlit as st


class LibraryManagementSystem:

    def add_book(self, books, book_id, title, author):
        book = {
            "Book ID": book_id,
            "Title": title,
            "Author": author,
            "Status": "Available"
        }

        books.append(book)

    def search_book(self, books, search_id):
        for book in books:
            if book["Book ID"] == search_id:
                return book
        return None

    def delete_book(self, books, search_id):
        for book in books:
            if book["Book ID"] == search_id:
                books.remove(book)
                return True
        return False

    def issue_book(self, books, search_id):
        book = self.search_book(books, search_id)

        if book is not None:
            if book["Status"] == "Available":
                book["Status"] = "Issued"
                return "issued"
            else:
                return "already issued"

        return "not found"

    def return_book(self, books, search_id):
        book = self.search_book(books, search_id)

        if book is not None:
            if book["Status"] == "Issued":
                book["Status"] = "Available"
                return "returned"
            else:
                return "already available"

        return "not found"


library = LibraryManagementSystem()

st.set_page_config(page_title="Library Management System", page_icon="📚")

st.title("📚 Library Management System")
st.write("A simple Python Streamlit app to manage library book records.")

if "books" not in st.session_state:
    st.session_state.books = []

menu = st.sidebar.selectbox(
    "Select Option",
    [
        "Add Book",
        "View All Books",
        "Search Book",
        "Delete Book",
        "Issue Book",
        "Return Book",
        "Total Books"
    ]
)

if menu == "Add Book":
    st.subheader("Add New Book")

    book_id = st.text_input("Enter Book ID")
    title = st.text_input("Enter Book Title")
    author = st.text_input("Enter Author Name")

    if st.button("Add Book"):
        if book_id == "" or title == "" or author == "":
            st.warning("Please fill all fields.")
        else:
            existing_book = library.search_book(st.session_state.books, book_id)

            if existing_book is not None:
                st.error("Book ID already exists.")
            else:
                library.add_book(st.session_state.books, book_id, title, author)
                st.success("Book added successfully!")

elif menu == "View All Books":
    st.subheader("All Books")

    if len(st.session_state.books) == 0:
        st.info("No books available.")
    else:
        st.table(st.session_state.books)

elif menu == "Search Book":
    st.subheader("Search Book")

    search_id = st.text_input("Enter Book ID to Search")

    if st.button("Search"):
        book = library.search_book(st.session_state.books, search_id)

        if book is not None:
            st.success("Book found!")
            st.write("Book ID:", book["Book ID"])
            st.write("Title:", book["Title"])
            st.write("Author:", book["Author"])
            st.write("Status:", book["Status"])
        else:
            st.error("Book not found.")

elif menu == "Delete Book":
    st.subheader("Delete Book")

    search_id = st.text_input("Enter Book ID to Delete")

    if st.button("Delete"):
        deleted = library.delete_book(st.session_state.books, search_id)

        if deleted:
            st.success("Book deleted successfully!")
        else:
            st.error("Book not found.")

elif menu == "Issue Book":
    st.subheader("Issue Book")

    search_id = st.text_input("Enter Book ID to Issue")

    if st.button("Issue"):
        result = library.issue_book(st.session_state.books, search_id)

        if result == "issued":
            st.success("Book issued successfully!")
        elif result == "already issued":
            st.warning("Book is already issued.")
        else:
            st.error("Book not found.")

elif menu == "Return Book":
    st.subheader("Return Book")

    search_id = st.text_input("Enter Book ID to Return")

    if st.button("Return"):
        result = library.return_book(st.session_state.books, search_id)

        if result == "returned":
            st.success("Book returned successfully!")
        elif result == "already available":
            st.warning("Book is already available.")
        else:
            st.error("Book not found.")

elif menu == "Total Books":
    st.subheader("Library Summary")

    total_books = len(st.session_state.books)
    available_books = 0
    issued_books = 0

    for book in st.session_state.books:
        if book["Status"] == "Available":
            available_books += 1
        elif book["Status"] == "Issued":
            issued_books += 1

    st.write("Total Books:", total_books)
    st.write("Available Books:", available_books)
    st.write("Issued Books:", issued_books)
