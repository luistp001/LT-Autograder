#LT Autograder. A system that automatically grades short answer essays.
#Copyright (C) 2012 Luis Tandalla

import re, time, sys, time
from correct2 import * #correct2 is the file of the auto spell corrector

def cleantext(text, cr, SET):
	#Given the essay, the object spell corrector and the set, it returns
	#the cleaned essay (mispelled words corrected, all words in lower case
	#letters, non alphanumeric characters, and digits eliminated
	#depending on the set)

	text=text.lower()
	text = text.replace('mr .', 'mr')
	textn = ""
	for let in text:
		if let.isalpha():		textn = textn + let
		elif let == '.':		textn = textn + " . "
		elif SET == '10' and let.isdigit():	#Keep digits for set 10
			textn = textn + let
		else:					textn = textn + ' '
	text = textn

	while text.find('  ') >= 0:		text = text.replace('  ', ' ')
	sentences = text.split()

	text = cr.correct(sentences[0]) #Correct the first word of an essay
	wordn = ""
	for i in range(len(sentences)-1):
		word = sentences[i+1]
		wordp = sentences[i]
		if i + 2 < len(sentences):	wordn = sentences[ i + 2 ]
		else: wordn = ""
		cword = cr.correct(word, wordp, wordn) #Correct mispelled words
		text = text + " " + cword

	return text #Return cleaned essay

def process1( nameFileIn, nameFileOut, test):
 #Clean all the essays from the file 'nameFileIn'
 #and writes the new cleaned essay in the file 'nameFileOut'.
 #Test is needed to know if the file is a training file or
 #a test file
 
 print 'Correcting Mispelled Words'
 Set = range(1,11)	
 reader = open( nameFileIn, 'r' )
 fi = open( nameFileOut, 'w' )

 for row in reader: 
	line = row.split('\t')
	fi.write( "%s\t%s\t" % ( line[0] , line[1] ) )
	if not test: fi.write( "%s\t%s\t" % ( line[2] , line[3] ) )
	fi.write( line[len(line) -1] )
	break

 lines = []

 for row in reader:
	lines.append( row.split('\t') )

 for SET in Set:
	print "SET:\t%d" % SET
	cr = correct2(SET)	# Initialization of spell corrector
	SET = str(SET)
	
	now = 0
	for line in lines:				
		if not line[1] == SET : continue
		fi.write( "%s\t%s\t" % ( line[0] , line[1] ) )
		if not test: fi.write( "%s\t%s\t" % ( line[2] , line[3] ) )
		now += 1
		if now % 30 == 0: print  line[0] 
		text =  cleantext(line[ len(line) -1 ], cr, SET) # It corrects the essay
		text = text.replace( '  ', ' ')
		fi.write( text + '\n')

	
