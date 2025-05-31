class User:
    def _init_(self, name, email):
        self.name = name
        self.email = email

    def display_info(self):
        return f"Name: {self.name}, Email: {self.email}"


class Instructor(User):
    def _init_(self, name, email, subject_expertise):
        super()._init_(name, email)
        self.subject_expertise = subject_expertise

    def upload_content(self, content):
        print(f"{self.name} uploaded new content: {content}")

    def display_info(self):
        return f"{super().display_info()}, Subject Expertise: {self.subject_expertise}"
