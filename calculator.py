# -*- coding: utf-8 -*-

from re import split

class StringCalculator:
    def add(self, values):
        delimiters, values = self._extract_delimiters(values)
        numbers = map(lambda x: int(x or 0), split(delimiters, values))
        filtered_numbers = self._filter(list(numbers))

        return sum(filtered_numbers)

    def _extract_delimiters(self, values):
        if values.startswith('//'):
            delimiters, values = values.split('\n', 1)
            return delimiters[2:].replace('][', ']|[') + '|,|\n', values
        return ',|\n', values

    def _filter(self, numbers):
        negative_numbers = list(filter(lambda x: x < 0, numbers))
        if len(negative_numbers) > 0:
            raise ValueError('negatives not allowed: ' + ', '.join(map(str, negative_numbers)))

        return filter(lambda x: x <= 1000, numbers)