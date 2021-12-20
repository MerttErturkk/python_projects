# -*- coding: utf-8 -*-
"""   Thu Jun 25 18:36:11 2020   @author: ERTURK
"""

def how_much_of_word(filename,word):
    with open(filename) as text:
        content = text.read()
        a= content.lower().count(word)
        print("the word "+"'"+word+"' " +"appears "+str(a)+" times in given file.")
        
