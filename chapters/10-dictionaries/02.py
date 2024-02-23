books = [
    {
        "title": "Title Number One",
        "page_count": 123,
        "authors": ["Author 1", "Author 2"]
    },
    {
        "title": "Title Number Two",
        "page_count": 123,
        "authors": ["Author 3", "Author 4"]
    },
    {
        "title": "Title Number Three",
        "page_count": 123,
        "authors": ["Author 5"]
    }
]

for book in books:
    title = book["title"]
    authors = ", ".join(book["authors"])
    print("%s: %s" % (title, authors))
