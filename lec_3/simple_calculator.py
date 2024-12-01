class SimpleCalculator:
    @staticmethod
    def add(a, b):
        return a+b
    
    @staticmethod
    def subtract(a, b):
        return a-b
    
    @staticmethod
    def multiply(a, b):
        return a*b
    
    @staticmethod
    def divide(a, b):
        return a/b
    

   
print(SimpleCalculator.add(7,4))
print(SimpleCalculator.subtract(7,4))
print(SimpleCalculator.multiply(7,4))
print(SimpleCalculator.divide(7,4))