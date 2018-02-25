# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

AGED_BRIE = "Aged Brie"
SULFURAS = "Sulfuras, Hand of Ragnaros"
BACKSTAGE_PASS = "Backstage passes to a TAFKAL80ETC concert"

class GildedRoseTest(unittest.TestCase):
    ITEM_NAME = 'an_item_name'
    def test_default(self):
        sell_in = 1
        quality = 2
        items = [Item(self.ITEM_NAME, sell_in, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(self.ITEM_NAME, items[0].name)
        self.assertEqual(sell_in - 1, items[0].sell_in)
        self.assertEqual(quality - 1, items[0].quality)

    def test_sell_date_passes_quality_degrade_twice(self):
        sell_in = 0
        quality = 2
        items = [Item(self.ITEM_NAME, sell_in, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(sell_in - 1, items[0].sell_in)
        self.assertEqual(quality - 2, items[0].quality)

    def test_quality_is_never_negative(self):
        sell_in = 0
        quality = 0
        items = [Item(self.ITEM_NAME, sell_in, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(sell_in - 1, items[0].sell_in)
        self.assertEqual(quality, items[0].quality)

    def test_aged_brie_increase_quality(self):
        sell_in = 1
        quality = 2
        items = [Item(AGED_BRIE, sell_in, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(sell_in - 1, items[0].sell_in)
        self.assertEqual(quality + 1, items[0].quality)

    def test_quality_not_more_than_50(self):
        sell_in = 2
        quality = 50
        items = [Item(AGED_BRIE, sell_in, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(sell_in - 1, items[0].sell_in)
        self.assertEqual(quality, items[0].quality)

    def test_sulfuras_never_has_to_be_sold_nor_decrease_in_quality(self):
        sell_in = 2
        quality = 10
        items = [Item(SULFURAS, sell_in, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(sell_in, items[0].sell_in)
        self.assertEqual(quality, items[0].quality)

    def test_backstage_increase_quality(self):
        sell_in = 12
        quality = 10
        items = [Item(BACKSTAGE_PASS, sell_in, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(sell_in - 1, items[0].sell_in)
        self.assertEqual(quality + 1, items[0].quality)

    def test_backstage_increase_quality_by_2(self):
        for sell_in in range(6, 11):
            quality = 1
            items = [Item(BACKSTAGE_PASS, sell_in, quality)]
            gilded_rose = GildedRose(items)
            gilded_rose.update_quality()
            self.assertEqual(sell_in - 1, items[0].sell_in)
            self.assertEqual(quality + 2, items[0].quality)

    def test_backstage_increase_quality_by_3(self):
        for sell_in in range(1, 5):
            quality = 1
            items = [Item(BACKSTAGE_PASS, sell_in, quality)]
            gilded_rose = GildedRose(items)
            gilded_rose.update_quality()
            self.assertEqual(sell_in - 1, items[0].sell_in)
            self.assertEqual(quality + 3, items[0].quality)

    def test_backstage_quality_drops_after_concert(self):
        sell_in = 0
        quality = 1
        items = [Item(BACKSTAGE_PASS, sell_in, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(sell_in - 1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

if __name__ == '__main__':
    unittest.main()
