# -*- coding: utf-8 -*-
"""   Thu Jun 25 18:26:45 2020   @author: ERTURK
"""

def count_words(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg="Sorry, the file "+filename+ " does not exist."
        print(msg)
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) +
              " words")
        
""" 
You can make list of input files and send it to the function.

"""