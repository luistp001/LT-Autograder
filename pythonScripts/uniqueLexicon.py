#LT Autograder. A system that automatically grades short answer essays.
#Copyright (C) 2012 Luis Tandalla

import re

# This scripts finds the words with only lower cases in the file 'ae2.txt'
# and saves these words in the file 'ae.txt'

fileOut = open( 'ae2.txt', 'w' )
reader = file('ae.txt').read()
lexicon1 = re.findall( r'(\w+)\n', str(reader))
lexicon2 = []
for word in lexicon1:
    wordl = word.lower()
    if not wordl in lexicon2: 
    	lexicon2.append ( wordl )
      	fileOut.write( wordl + '\n')
