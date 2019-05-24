# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):

        for item in self.items:

            # ###################
            # set class item
            # ###################

            # tree of class
            # Item < Simple_Item < Perishable_Item < VerryPerishable_Item
            #                    < TakeValue_Item  < Event_Item
            #                    < Legendary_Item

            if item.name == "Sulfuras, Hand of Ragnaros":
                item.__class__ = Legendary_Item

            elif item.name == "Aged Brie":
                item.__class__ = TakeValue_Item

            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                item.__class__ = Event_Item

            elif item.name == "Conjured Mana Cake":
                item.__class__ = VerryPerishable_Item

            else:
                item.__class__ = Perishable_Item

            # ###################
            # update item
            # ###################

            # update quality
            if item.name != "Backstage passes to a TAFKAL80ETC concert":
                item.update_quality()
            else:
                item.update_quality([-1,10,5])

            # update sell_in
            item.update_sell_in()


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class Simple_Item(Item):

    def update_quality(self):
        pass

    def update_sell_in(self):

        # sell_in -1
        self.sell_in -= 1


class Perishable_Item(Simple_Item):

    def update_quality(self):

        # quality -1 if sell_in >= 0
        if self.sell_in >= 0 :
            self.quality -= 1

        # quality -2 if sell_in < 0
        else:
            self.quality -=2

        # quality always > 0
        if self.quality < 0:
            self.quality = 0

class VerryPerishable_Item(Perishable_Item):

    def update_quality(self):
        Perishable_Item.update_quality(self)
        Perishable_Item.update_quality(self)

class TakeValue_Item(Simple_Item):

    def update_quality(self, steps = [-1]):

        for step in steps:

            # normal case (unknown step)
            # -1 <=> unknown step
            if step == -1 :
                self.quality += 1

            # special case
            else:
                if self.sell_in <= step :
                    self.quality += 1

        # quality always < 50
        if self.quality > 50:
            self.quality = 50

class Event_Item(TakeValue_Item):

    def update_quality(self, steps = [-1]):

        if self.sell_in > 0:
            TakeValue_Item.update_quality(self, steps)
        else:
            self.quality = 0

class Legendary_Item(Simple_Item):

    def update_sell_in(self):
        pass
