class ShapeCalculator:
    def area(self, length=0, width=0):
        if width == 0:
            return 3.14 * length * length  
        else:
            return length * width

if name== "main":
    calculator = ShapeCalculator()

    print("Circle Area:", calculator.area(5))

    print("Rectangle Area:", calculator.area(5, 10))