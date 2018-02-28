# -*- coding: utf-8 -*-

from re import split

class StringCalculator:
    def add(self, values):
        delimiters, values = self.__extract_delimiters(values)
        numbers = list(map(lambda x: int(x or 0), split(delimiters, values)))

        negative_numbers = list(filter(lambda x: x < 0, numbers))
        if len(negative_numbers) > 0:
            raise ValueError('negatives not allowed: ' + ', '.join(map(str, negative_numbers)))

        numbers_smaller_than_1000 = filter(lambda x: x <= 1000, numbers)

        return sum(numbers_smaller_than_1000)

    def __extract_delimiters(self, values):
        if values.startswith('//'):
            delimiters, values = values.split('\n', 1)
            return (delimiters[2:].replace('][', ']|[') + '|,|\n', values)
        return (',|\n', values)