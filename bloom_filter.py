import math
import mmh3
from random import shuffle
from bitarray import bitarray

# ANSI colors
c = (
    "\u001b[0m",   # End of color
    "\u001b[36m",  # Cyan: present
    "\u001b[33m",  # Yellow: not present
    "\u001b[35m",  # Magenta: false positive
)


class Pybloom:

    def __init__(self, number_of_items=20, probability_of_false_positives=0.5):
        self.number_of_items = number_of_items
        self.probability_of_false_positives = probability_of_false_positives
        self.number_of_bits_in_filter = self.get_number_of_bits()
        self.number_of_hash_functions = self.get_number_of_hash_functions()
        self.filter = self.get_bitarray()

    def get_number_of_bits(self):

        return math.ceil(-(self.number_of_items * math.log(self.probability_of_false_positives))/((math.log(2))**2))

    def get_number_of_hash_functions(self):

        return math.floor(self.number_of_bits_in_filter*math.log(2)/self.number_of_items)

    def get_bitarray(self):
        filter = bitarray(self.number_of_bits_in_filter)
        filter.setall(0)
        return filter

    def add_item(self, item):

        for i in range(self.number_of_hash_functions):
            hash = mmh3.hash(item, i) % self.number_of_bits_in_filter
            self.filter[hash] = 1

    def check_item(self, item):

        for i in range(self.number_of_hash_functions):
            hash = mmh3.hash(item, i) % self.number_of_bits_in_filter
            if self.filter[hash] == 0:
                return 0

        return 1


if __name__ == '__main__':

    obj = Pybloom()
    words_to_add = ['abound', 'abounds', 'abundance', 'abundant', 'accessable',
                    'bloom', 'blossom', 'bolster', 'bonny', 'bonus', 'bonuses',
                    'coherent', 'cohesive', 'colorful', 'comely', 'comfort',
                    'gems', 'generosity', 'generous', 'generously', 'genial']

    for word in words_to_add:
        obj.add_item(word)

    shuffle(words_to_add)
    
    words_to_check = words_to_add[:10] + ['bluff', 'null', 'gloomy', 'facebook', 'twitter']
    shuffle(words_to_check)

    for word in words_to_check:
        if obj.check_item(word):
            if obj.check_item(word):
                if word in words_to_add:
                    print(c[1] + "{} is present".format(word))
                else:
                    print(c[3] + "{} is false positive".format(word))

        else:
            print(c[2] + "{} is not present".format(word))

    print(c[0])


    """for word in words_to_check:
        print("{} is present".format(word)) if obj.check_item(word) else print("{} is not present".format(word))
        print("***")"""\
