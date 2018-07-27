
class RomanToArabic(str):
    def __init__(self, numeral):
        roman = self.check_valid(numeral)
        keys = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM',
                'I', 'V', 'X', 'L', 'C', 'D', 'M']
        to_arabic = {'IV': '4', 'IX': '9', 'XL': '40', 'XC': '90', 'CD': '400', 'CM': '900',
                     'I': '1', 'V': '5', 'X': '10', 'L': '50', 'C': '100', 'D': '500', 'M': '1000'}
        for key in keys:
            if key in roman:
                roman = roman.replace(key, ' {}'.format(to_arabic.get(key)))
        self.arabic = sum(int(num) for num in roman.split())

    def check_valid(self, numeral):
        roman = numeral.upper()
        invalid = ['IIII', 'VV', 'IIV', 'XXXX',
                   'IIX', 'VX', 'LL', 'IL', 'VL',
                   'CCCC', 'IC', 'VC', 'DD', 'ID',
                   'VD', 'XD', 'LD', 'MMMM', 'IM',
                   'VM', 'XM', 'LM', 'DM']
        if any(sub in roman for sub in invalid):
            # to force a specified exception to occur.
            raise ValueError('Invalid roman numeral: {}'.format(roman))
        return roman


class ArabicToRoman(int):
    # Creating instance. We customize the instance created and make some validation operations over
    # it before initializer __init__  being called.
    def __new__(cls, numeral):
        if numeral > 3999 or numeral <= 0:
            raise ValueError(
                'Zero, negative values and values over 3999 are not allowed: {}'.format(numeral))
        # create new instance of the class by invoking the superclass’s __new__ method using super
        return super().__new__(cls, numeral)
    # __init__ will be called to initialize instance when we are creating instance.

    def __init__(self, numeral):
        to_roman = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V',
                    6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X', 20: 'XX',
                    30: 'XXX', 40: 'XL', 50: 'L', 60: 'LX', 70: 'LXX', 80: 'LXXX',
                    90: 'XC', 100: 'C', 200: 'CC', 300: 'CCC', 400: 'CD', 500: 'D',
                    600: 'DC', 700: 'DCC', 800: 'DCCC', 900: 'CM', 1000: 'M',
                    2000: 'MM', 3000: 'MMM'}
        self.roman = ''.join([to_roman.get(num) for num in self][::-1])

    # the __iter__() method is called automatically whenever we calls "for" loop in __init__.

    def __iter__(self):
        numeral = self.__str__()
        count = 1
        for digit in numeral[::-1]:
            if digit != '0':
                yield int(digit) * count
            count *= 10


def convert(numeral):
    if isinstance(numeral, int):
        num = ArabicToRoman(numeral)
        return num.roman
    num = RomanToArabic(numeral)
    return num.arabic
