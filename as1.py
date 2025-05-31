class Member:
    def _init_(self, name, membership_id):
        self.name = name
        self.membership_id = membership_id

    def _str_(self):
        return f"Member: {self.name}, ID: {self.membership_id}"


class StudentMember(Member):
    def _init_(self, name, membership_id):
        
        super()._init_(name, membership_id)
        self.borrowed_books = 0

    def add_book(self):
                self.borrowed_books += 1
                print(f"{self.name} has borrowed a book. Total books borrowed: {self.borrowed_books}")

    def return_book(self):
       
        if self.borrowed_books > 0:
            self.borrowed_books -= 1
            print(f"{self.name} has returned a book. Total books borrowed: {self.borrowed_books}")
        else:
            print(f"{self.name} has no books to return.")

    def display_borrowing_status(self):
        
        print(f"{self.name} has {self.borrowed_books} book(s) borrowed")