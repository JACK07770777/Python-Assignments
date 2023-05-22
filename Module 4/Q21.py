# How To Define A Class In Python? What Is Self ? Give An Example Of A  Python Class ?
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_make(self):
        return self.make

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_info(self):
        return f"{self.year} {self.make} {self.model}"