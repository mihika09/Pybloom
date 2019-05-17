# Pybloom
Implementation of an in-memory bloom filter using bitarray and murmurhash3 algorithm.

## Functions

- Add a word
- Check if a word is present or not

## How to use

Create an object of the Pybloom class and provide the following values:

- number_of_items --- expected number of items to be added (default: 20)
- probability_of_false_positives --- expected probability of getting a flase positive (default: 0.5)

```
obj = Pybloom(number_of_items=1000, probability_of_false_positives=0.0001)
```

##### To add an item

```
obj.add_item(item_to_be_added)
```

##### To check an item

```
obj.check_item(item_to_be_checked)
```
