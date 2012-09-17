#LT Autograder. A system that automatically grades short answer essays.
#Copyright (C) 2012 Luis Tandalla

import re
from PorterStemmer import PorterStemmer

def cleantext(text, ps):
	text = text.replace('mr .', 'mr')
	text = text.replace('u . s .', 'us')
	sentences = text.split()

	text = ps.stem(sentences[0])
	for i in range(len(sentences)-1):
		word = sentences[i+1]
		if word == 'thoughtful': text = text + " " + word 
		else: text = text + " " + ps.stem( word )
	return text

def process2( nameFileIn, nameFileOut):
 ps = PorterStemmer() # It initializes stemmer
 reader = open(nameFileIn, 'r' )
 fi = open( nameFileOut , "w")


 for row in reader:
	line = row.split('\t')
	for i in range(len(line)-1):
		fi.write( line[i] + '\t' )
		
	
	text =  cleantext( line[len(line) - 1] , ps)
	fi.write( text + '\n')
	
