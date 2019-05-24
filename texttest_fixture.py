# -*- coding: utf-8 -*-
from __future__ import print_function
import numpy as np
import pandas

from gilded_rose import *

def create_tables():

    items = [Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
             Item(name="+5 Dexterity Vest", sell_in=-10, quality=20),
             Item(name="Aged Brie", sell_in=2, quality=0),
             Item(name="Aged Brie", sell_in=2, quality=50),
             Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
             Item(name="Elixir of the Mongoose", sell_in=-5, quality=7),
             Item(name="Sulfuras, Hand of Ragnaros", sell_in=1, quality=80),
             Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=20),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=20),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=20),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=-5, quality=20),
             Item(name="Conjured Mana Cake", sell_in=3, quality=6),
             Item(name="Conjured Mana Cake", sell_in=-2, quality=6)]

    tables_content = ""
    for day in range(2):

        tables_content += "\n____________________________ day %s ____________________________\n" % day

        # ######################################################################
        # Create table values
        # ######################################################################

        itemsValues = []
        for item in items:
            itemsValues += [[item.name, item.sell_in, item.quality]]

        teams_list = ["name", "sellIn", "quality"]
        data = np.array(itemsValues)
        table = pandas.DataFrame(itemsValues, columns = teams_list)
        tables_content += str(table) + "\n"


        GildedRose(items).update_quality()

    return tables_content

if __name__ == "__main__":
    print(create_tables())