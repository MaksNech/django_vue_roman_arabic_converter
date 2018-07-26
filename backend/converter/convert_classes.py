
class RomanToArabic(str):
    def __init__(self, roman):
        roman = self.check_valid(roman)
        keys = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM',
                'I', 'V', 'X', 'L', 'C', 'D', 'M']
        to_arabic = {'IV': '4', 'IX': '9', 'XL': '40', 'XC': '90', 'CD': '400', 'CM': '900',
                     'I': '1', 'V': '5', 'X': '10', 'L': '50', 'C': '100', 'D': '500', 'M': '1000'}
        for key in keys:
            if key in roman:
                roman = roman.replace(key, ' {}'.format(to_arabic.get(key)))
        self.arabic = sum(int(num) for num in roman.split())

    def check_valid(self, roman):
        roman = roman.upper()
        invalid = ['IIII', 'VV', 'IIV', 'XXXX',
                   'IIX', 'VX', 'LL', 'IL', 'VL',
                   'CCCC', 'IC', 'VC', 'DD', 'ID',
                   'VD', 'XD', 'LD', 'MMMM', 'IM',
                   'VM', 'XM', 'LM', 'DM']
        if any(sub in roman for sub in invalid):
            raise ValueError('Invalid roman numeral: {}'.format(roman))
        return roman


class ArabicToRoman(int):
    def __new__(cls, numeral):
        if numeral > 3999:
            raise ValueError(
                'Values over 3999 are not allowed: {}'.format(numeral))
        if numeral <= 0:
            raise ValueError(
                'Zero and negative values are not allowed: {}'.format(numeral))
        return super().__new__(cls, numeral)

    def __init__(self, numeral):
        to_roman = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V',
                    6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X', 20: 'XX',
                    30: 'XXX', 40: 'XL', 50: 'L', 60: 'LX', 70: 'LXX', 80: 'LXXX',
                    90: 'XC', 100: 'C', 200: 'CC', 300: 'CCC', 400: 'CD', 500: 'D',
                    600: 'DC', 700: 'DCC', 800: 'DCCC', 900: 'CM', 1000: 'M',
                    2000: 'MM', 3000: 'MMM'}
        self.roman = ''.join([to_roman.get(num) for num in self][::-1])

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
