# GildedRose Refactoring Kata Python

This dipository tries to answer the Gilded Rose Refactoring Kata with python. 
The exercice is summarized here :(https://github.com/emilybache/GildedRose-Refactoring-Kata)

##Concerning the tests

The Text-Based approval testing proposed initially has been used.
So at first, 'texttest_fixture.py' has been rewritten to create the Golden Master file and the associated comparison functions.

##Concerning refactoring

At the start of this exercise, item attribute updates are done directly within the class GildedRose.
In order to make the code more readable, it seems more appropriate to create an update_quality method specific to the class Item.
Since the Item class cannot be directly edited (exercise guideline), the exercise therefore consisted mainly in creating heiress class of Item each with the update_quality method corresponding to the instructions.

