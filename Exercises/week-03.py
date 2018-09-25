# pylint: disable=E0213

class Fraction():

    def common_den(a,b,a1,b1):
        x = 1
        common_den = 0
        while x != 0:
            if (min(b,b1)*x % (max(b,b1)) != 0):
                x += 1
            else:
                common_den = x*min(b,b1)
                x = 0
        return common_den

    def __init__(self, a,b):
        self.a = a
        self.b = b
    
    def __str__(self):
        return str(self.a) + '/' + str(self.b)

    def inv_fraction(self):
        return 'The fraction inverted is: ' + str(self.b) + '/' + str(self.a)
    
    def add_fractions(self, other):
        com_den = Fraction.common_den(self.a,self.b,other.a,other.b)
        return 'The result of adding the fractions is = ' + str(int((self.a*com_den/self.b) + (other.a*com_den/other.b))) + '/' + str(com_den)

    def sub_fractions(self, other):
        com_den = Fraction.common_den(self.a,self.b,other.a,other.b)
        if int((self.a*com_den/self.b) - (other.a*com_den/other.b)) == 0:
            return 'The result of subtracting the fractions is = ' + 0
        else:
            return 'The result of subtracting the fractions is = ' + str(int((self.a*com_den/self.b) - (other.a*com_den/other.b))) + '/' + str(com_den)

    def multi_fractions(self, other):
        return 'The result of multiplying the fractions is = ' + str(self.a * other.a) + '/' + str(self.b *other.b)
    
fraction1 = Fraction(1,2)
fraction2 = Fraction(2,3)

print(fraction1)
print('Fraction 1 is = ', fraction1)
print('Fraction 2 is = ', fraction2)
print(fraction1.add_fractions(fraction2))
print(fraction1.sub_fractions(fraction2))
print(fraction1.multi_fractions(fraction2))
print(fraction1.inv_fraction())
