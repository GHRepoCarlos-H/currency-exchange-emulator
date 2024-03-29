class Currency:
    currencies = {
        'USD': 1.0,
        'EUR': 0.85,
        'GBP': 0.73,
        'JPY': 110.33,
    }

    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def __repr__(self):
        return f" {self.value:.2f} {self.unit}"
    
    def __str__(self):
        return self.__repr__()
    
    def __add__(self, other):
        if isinstance(other, Currency):
            return Currency(self.value + other.to(self.unit).value, self.unit)
        elif isinstance(other, (int, float)):
            return Currency(self.value + other, self.unit)
        else:
            raise TypeError("Unsupported operand type +")
        
    def __iadd__(self, other):
        return self.__add__(other)

    def __radd__(self, other):
        if isinstance(other, (int, float)):
            return Currency(other + self.to('USD').value, 'USD')
        else:
            raise TypeError('Unsupported operand type +')
    
    def __sub__(self, other):
        if isinstance(other, Currency):
            return Currency(self.value - other.to(self.unit).value, self.unit)
        elif isinstance(other, (int, float)):
            return Currency(self.value - other, self.unit)
        else:
            raise TypeError("Unsupported operand -")
        
    def __isub__(self, other):
        return self.__sub__(other)
    
    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            return Currency(other - self.to('USD').value, 'USD')
        else:
            raise TypeError("Unsupported oprand type -")
    
    def to(self, target_unit):
        if self.unit == target_unit:
            return self
        else:
            converted_value = self.value / self.currencies[self.unit] * self.currencies[target_unit]
            return Currency(converted_value, target_unit)
        
v1 = Currency(23.43, "EUR")
v2 = Currency(19.97, "USD")
print(v1 + v2)
print(v2 + v1)
print(v1 + 3)
print(3 + v1)
print(v1 - 3)
print(30 - v2)
    