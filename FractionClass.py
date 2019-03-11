


"""
Fraction Class
"""

def gcd(m, n):
    """
    FUnction for calculating greatest common divisor of two integers
    :param m:
    :param n:
    :return:
    """
    while m % n != 0:
        old_m = m
        old_n = n

        m = old_n
        n = old_m % old_n
    return n

print(gcd(30, 15))


class Fraction:

    def __init__(self, top, bottom):

        self.num = top
        self.den = bottom

    def show(self):
        print(self.num, '/', self.den)

    def __str__(self):
        return str(self.num) + '/' + str(self.den)

    def __add__(self, other):
        newnum = self.num*other.den + self.den*other.num
        newden = self.den*other.den
        common = gcd(newnum, newden)
        return Fraction(newnum//common, newden//common)

    def __eq__(self, other):
        """
        Mehtod to create deep equality
        :param other:
        :return:
        """
        firstnum = self.num*other.den
        secondnum = self.den*other.num

        return firstnum == secondnum

    def __mul__(self, other):
        """
        Function to multipy two fractions
        :param other:
        :return:
        """
        new_num = self.num*other.num
        new_den = self.den*other.den
        common = gcd(new_num, new_den)

        return Fraction(new_num//common, new_den//common)

    def __truediv__(self, other):
        """
        True division method
        :param other:
        :return:
        """
        new_num = self.num*other.den
        new_den = self.den*other.num
        common = gcd(new_num, new_den)

        return Fraction(new_num//common, new_den//common)

    def __sub__(self, other):
        newnum = self.num * other.den - self.den * other.num
        newden = self.den * other.den
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)




myfrac = Fraction(3, 5)

myfrac.show()
print(myfrac)

f1 = Fraction(1, 2)
f2 = Fraction(1, 4)
f3 = f1+f2

print(f3)
print(f1 == f2)
print(f1*f2)
print(f1/f2)
print(f2-f1)
