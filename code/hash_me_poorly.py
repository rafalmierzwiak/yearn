#!/usr/bin/env python3

from collections import namedtuple

PoorItem = namedtuple('Item', 'key value')


class PoorHash:
    """Poor man's hash.
    Hash is compartmentalized into slots and in these slots items are kept.
    No room left for probing, number of slots fixed at initialisation time,
    hence name of the class.
    """

    def __delitem__(self, key):
        bi, ii = self.__slotindex__(key), self.__itemindex__(key)
        del self.items[bi][ii]

    def __getitem__(self, key):
        bi, ii = self.__slotindex__(key), self.__itemindex__(key)
        return self.items[bi][ii].value

    def __getslot__(self, key):
        return self.items[self.__slotindex__(key)]

    def __init__(self, slots=16):
        self.items = [ [] for _ in range(slots) ]

    def __itemindex__(self, key):
        try:
            index, = (i
                      for i, item in enumerate(self.__getslot__(key))
                      if item.key == key)
            return index

        except ValueError:
            raise KeyError(key) from None

    def __slotindex__(self, key):
        return hash(key) % len(self.items)

    def __len__(self):
        return sum((len(items) for items in self.items if items))

    def __setitem__(self, key, value):
        self.items[self.__slotindex__(key)].append(PoorItem(key, value))


h = PoorHash()

for i in range(1024):
    h[i] = i

print("No of items: {}".format(len(h)))
for i in range(len(h)):
    _ = h[i]

for i in [0, 1, len(h)-2, len(h)-1]:
    print("Item {} is {}".format(i, h[i]))
