from optparse import OptionParser

def print_name(options = None): 
    if options.name:
        print(options.name)
    else:
        print('hello, person! \nHow are ya?')


if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option('-n','--name',dest = 'name',
                      help='username to be printed out')
    (options,args) = parser.parse_args()
    print_name(options)
    
    
    #python print_name.py -n mert
    