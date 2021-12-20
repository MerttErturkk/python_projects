# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 23:24:06 2020

@author: ERTURK
"""
"""
Kümelere benzer fakat her elemanın bir "key"i vardır.
"""

sözlük={
        "book":"kitap",
        "table":"masa",
        }

print(sözlük["book"])
sözlük["pencil"]="kalem" # yeni bi eleman ekler
print(sözlük)



dictionary= dict(kitap =" book", masa="table")#ayrıca bu şekilde de belirlenebilr
print (dictionary)

del(sözlük["book"]) ## istenen elemanı siler
print(sözlük)



################# code below will print "python" twice
favorite_languages = {
    "jen":"python",
    "sarah":"c",
    "edward":"ruby",
    "phil":"python",
    }
print("the following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

#### we should convert our .values() into a set to avoid this duplication.

print("--------------")
for language in set(favorite_languages.values()):
    print(language.title())