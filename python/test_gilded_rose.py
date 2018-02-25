# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    ITEM_NAME = 'an_item_name'
    def test_default(self):
        sell_in = 1
        quality = 2
        items = [Item(self.ITEM_NAME, sell_in, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(self.ITEM_NAME, items[0].name)
        self.assertEquals(sell_in - 1, items[0].sell_in)
        self.assertEquals(quality - 1, items[0].quality)

    def test_sell_date_passes_quality_degrade_twice(self):
        sell_in = 0
        quality = 2
        items = [Item(self.ITEM_NAME, sell_in, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(self.ITEM_NAME, items[0].name)
        self.assertEquals(sell_in - 1, items[0].sell_in)
        self.assertEquals(quality - 2, items[0].quality)


if __name__ == '__main__':
    unittest.main()
