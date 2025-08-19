from datetime import datetime


class FourDigitYearConverter:
    regex = '[0-9]{4}'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return '%04d' % value


class MyFloatConverter:
    regex = '[+-]?(\d*\.)?\d+'

    def to_python(self, value):
        return float(value)

    def to_url(self, value):
        return str(value)

class MyDateConverter:
    regex = '\d{2}-\d{2}-\d{4}'

    def to_python(self, value):
        return datetime.strptime(value, '%d-%m-%Y')

    def to_url(self, value : datetime):
        return value.strftime('%d-%m-%Y')

class SplitConverter:
    regex = '[a-zA-z]+,[a-zA-Z]+'
    def to_python(self, value:str):
        return value.split(',')

    def to_url(self, value):
        return ','.join(value)

class UpperConvertor:
    regex = '\w+'
    def to_python(self, value:str):
        return value.upper()

    def to_url(self, value:str):
        return value.lower()
