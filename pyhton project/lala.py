import tkinter as tk

class LibraryManagementSystem:
    def __init__(self, master):
        self.master = master
        self.master.title("Library Management System")

        self.books = []

        self.title_label = tk.Label(master, text="Library Management System", font=("Arial", 18))
        self.title_label.pack()

        self.title_entry_label = tk.Label(master, text="Title:")
        self.title_entry_label.pack()
        self.title_entry = tk.Entry(master)
        self.title_entry.pack()

        self.author_entry_label = tk.Label(master, text="Author:")
        self.author_entry_label.pack()
        self.author_entry = tk.Entry(master)
        self.author_entry.pack()

        self.add_button = tk.Button(master, text="Add Book", command=self.add_book)
        self.add_button.pack()

        self.list_label = tk.Label(master, text="Available Books:", font=("Arial", 14))
        self.list_label.pack()

        self.book_listbox = tk.Listbox(master, width=50)
        self.book_listbox.pack()

        self.search_entry_label = tk.Label(master, text="Search by Title:")
        self.search_entry_label.pack()
        self.search_entry = tk.Entry(master)
        self.search_entry.pack()

        self.search_button = tk.Button(master, text="Search", command=self.search_book)
        self.search_button.pack()

    def add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        if title and author:
            self.books.append({"title": title, "author": author})
            self.update_book_list()
            self.title_entry.delete(0, tk.END)
            self.author_entry.delete(0, tk.END)

    def update_book_list(self):
        self.book_listbox.delete(0, tk.END)
        for book in self.books:
            self.book_listbox.insert(tk.END, f"{book['title']} by {book['author']}")

    def search_book(self):
        keyword = self.search_entry.get().lower()
        if keyword:
            search_results = [book for book in self.books if keyword in book['title'].lower()]
            self.book_listbox.delete(0, tk.END)
            if search_results:
                for book in search_results:
                    self.book_listbox.insert(tk.END, f"{book['title']} by {book['author']}")
            else:
                self.book_listbox.insert(tk.END, "No matching books found.")

def main():
    root = tk.Tk()
    app = LibraryManagementSystem(root)
    root.mainloop()

if __name__ == "__main__":
    main()
