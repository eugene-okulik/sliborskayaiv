class Books:
    material = 'paper'
    isTextPresent = True

    def __init__(self, name, author, pages, isbn, reserved):
        self.name = name
        self.author = author
        self.pages = pages
        self.ISBN = isbn
        self.reserved = reserved

    def details(self):
        if self.reserved:
            return f"Name: {self.name}, author: {self.author}, pages: {self.pages}, material: {self.material}, reserved"
        else:
            return f"Name: {self.name}, author: {self.author}, pages: {self.pages}, material: {self.material}."


class Workbooks(Books):
    def __init__(self, name, author, pages, isbn, reserved, subject, year, tasks):
        super().__init__(name, author, pages, isbn, reserved)
        self.subject = subject
        self.year = year
        self.tasks = tasks

    def details(self):
        if self.reserved:
            return (f"Name: {self.name}, author: {self.author}, pages: {self.pages}, subject: {self.subject}, "
                    f"year: {self.year}, reserved.")
        else:
            return (f"Name: {self.name}, author: {self.author}, pages: {self.pages}, subject: {self.subject}, "
                    f"year: {self.year}.")


books = [
    Books('Julie_and_Julia', 'Julie Powell', 132,  3423423, False),
    Books('The Help', 'Kathryn Stockett', 256, 5324324, False),
    Books('Idiot', 'Fedor Dostoevski', 345, 45623423, True),
    Books('The Outsider', 'Albert Camus', 543, 576475543, False),
    Books('The Last Samurai', 'Helen DeWitt', 256, 532434, False)
]

workbooks = [
    Workbooks('History', 'Harevski', 156, 432434, True, 'History', 9, True),
    Workbooks('Math', 'Lebedev', 543, 746534, False, 'Math', 8, False),
    Workbooks('Chemistry', 'Lasarev', 345, 87645, False, 'Chemistry', 9, True)
]

for book in books:
    print(book.details())

for workbook in workbooks:
    print(workbook.details())
