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

        tables_content += "\n____________________________"
        tables_content += " day %s " % day
        tables_content += "____________________________\n"

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

    # ##########################################################################
    # Import contents to compare
    # ##########################################################################

    # create content to test
    test = create_tables()
    lines_test = test.split("\n")
    nbr_test = len(lines_test)

    # import text from GoldenMaster file to verify
    f = open("golden_master.txt","r")
    gold = f.read()
    lines_gold = gold.split("\n")
    nbr_gold = len(lines_gold)
    f.close()

    # ##########################################################################
    # Find errors
    # ##########################################################################

    # enumerate errors
    errors = []

    if nbr_test != nbr_gold:
        print("The number of line is not the same")

    else:
        for line in range(nbr_test):
            lt = lines_test[line]
            lg = lines_gold[line]

            if  lt != lg :
                errors += [(line, lt, lg)]


    # ##########################################################################
    # Display  errors
    # ##########################################################################

    nbr_error = len(errors)

    print("##########################################")
    print("############### %s error(s) ############### " % nbr_error)
    print("##########################################")
    print("")

    for info in errors:
        n_line = info[0]
        current_line = info[1]
        desired_line = info[2]

        print("############## error line %s ##############" % n_line)
        print("current: %s" % current_line)
        print("desired: %s" % desired_line)
        print("\n")