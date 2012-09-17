#LT Autograder. A system that automatically grades short answer essays.
#Copyright (C) 2012 Luis Tandalla


import collections, re
from util import *

def feature9(**kwargs):
	# This function searches if an essay of a given set has the answers needed 
	# for a high score using regular expressions.

	# 'answer' is the list of having answer or not.
	# 'index' is the index of the current answer that is being looking for.
	# 'pats' is the list of regular expressions used to find an answer.
	# If a match is found for a text, 'line_match' that match
	#  'fi' is the list of answers as vectors of words. 'fi' is updated 
	# in this function.
	# 'fi2' is the dictionary of of words for each match of each answer,
	# 'matchs' is a list of matches for each answer.
	# 'fet' is the function that actually searches for an answer in an 
	# essay given the list of regular expressions and the text of the essay.
	# 'update_ans' updates the list 
	# 'reset' (in some sets used) reset the necessary values to search for a
	# new answer.

	text = kwargs['text']
	fi = kwargs['fi']
	Id = kwargs['Id']
	#print Id 
	score = kwargs['score']
	score2 = kwargs['score2']
	fi2 = kwargs['fi2']
	index = -1

	line_match = None
	answer = []
	matchs = []

	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}shock( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}rhetor question( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}hook( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}((startl)|(surpris)|(interest)|(open)|(rhetor)|(catch)|(uniqu)) statem\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}exclam (\w+ ){0,2}((mark)|(point))\w*( \w+){0,4}") )
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}attent letter( \w+){0,4}") )		
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)




	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"((\w+ )+|^| )in( ?to)? ((([dmsfcli])|(three))\w* ){0,2}((section)|(categ)|(top)|(gro)|(tit)|(hea)|(cha)|(part)|(seg))\w*( \w+){0,4}") )			
	pats.append( re.compile(r"(\w+ ){0,4}sub ?[tghsdca]\w*( \w+){0,4}") )			
	pats.append( re.compile(r"((( \w+){0,4} )|(^))by (\w+ )?((gro)|(sec)|(tit)|(top)|(hea)|(cha)|(dif)|(cate)|(sepa)|(bre)|(spl)|(div))\w*( \w+){0,4}") )			
	pats.append( re.compile(r"(\w+ ){0,4}side head\w* (\w+ ){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}differ ((cate)|(sec)|(head)|(top)|(gro)|(tit)|(cha)|(seg)|(part))\w* (\w+ ){0,4}") )			
	pats.append( re.compile(r"(\w+ ){0,4}\w*((tit)|(head))\w* (\w+ ){0,2}each\w*( \w+){0,4}") )
	pats.append( re.compile(r"((( \w+){0,4} )|(^))with ((gro)|(sec)|(tit)|(top)|(hea)|(cha)|(dif)|(cate)|(sepa)|(bre)|(spl)|(div))\w*( \w+){0,4}") )			
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)	


	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}talk about space junk( \w+){0,4}") )			
	pats.append( re.compile(r"(\w+ ){0,4}what (\w+ )?space junk( \w+){0,4}") )			
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	pats = []
	if not line_match:						
		#pats.append( re.compile(r"(\w+ )*what (\w+ )space junk( \w+)*") )			
#		pats.append( re.compile(r"(\w+ ){0,1}tit\w*( \w+){0}") )			
	#	pats.append( re.compile(r"(\w+ ){0,2}differ (\w+ ){0,4}") )			
#		pats.append( re.compile(r"((\w+ )+|^| )in( ?to)? ((([dmsfcli])|(three))\w* ){0,2}((section)|(categ)|(top)|(gro)|(tit)|(hea)|(cha)|(part)|(seg))\w*( \w+)*") )			
		#pats.append( re.compile(r"( \w+)* by (\w+ )?((gro)|(sec)|(tit)|(top)|(hea)|(cha)|(dif)|(cate)|(sepa)|(bre)|(spl)|(div))\w*( \w+)*") )			
#		pats.append( re.compile(r" by (\w+ ){0,5}") )			
		#pats.append( re.compile(r"((\w+ )+|^| )in( ?to)? ([dmsfcli]\w* )?categ\w*( \w+)*") )			
		pass

	ans, line_match = fet(text, pats)					
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

#	if ans == '0' and label[index] == '1' : print '%d\tFALSE NEGATIVE\t%s\n' % (Id, text	)
#	if ans == '1' and label[index] == '0': print 'FALSE POSITIVE\t%s' % (line_match)	
	#if ans == '1' and label[index] == '0': print 'FALSE POSITIVE\t' + text + '\n'	
	#if ans == '1' and label[index] == '0' and score == 0 and score2 == 0: print 'FALSE POSITIVE\t%s\n%s\n%d\t%d\n' % (text, line_match, score, score2 )
	#if ans == '1' and label[index] == '0' and score == 0 and score2 == 0: print 'FALSE POSITIVE\t%s' % ( line_match )
	#if ans == '1' and label[index] == '1': print 'TRUE POSITIVE\t%s\n%s\n%d\t%d\n' % (text, line_match, score, score2 )
#	if ans == '1' and label[index] == '1': print 'TRUE POSITIVE\t%s' % (line_match )

	


	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}crash cours( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}colli\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*then (\w+ ){0,4}crash( \w+){0,4}") )	
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)	

	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}littl bit but a big deal( \w+){0,4}") )			
	pats.append( re.compile(r"( \w+){0,4} ((small)|(tin)|(lit))\w* (\w+ )*danger( \w+){0,4}") )			
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)	

	ans, index, fi, pats = reset(index, fi)
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}solu\w*( \w+){0,4}") )		
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)
	
	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}begin (\w+ )*middl (\w+ )*end( \w+){0,4}") )			
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	ans, index, fi, pats = reset(index, fi)
	#pats.append( re.compile(r"(\w+ )*begin (\w+ )*middl (\w+ )*end( \w+)*") )			
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)
		



	

	if answer == [0] and score > 1 and score2 > 1: print '%d\t%d\t%d\t%s\n' %(Id, score, score2, text)




#	print '%d\t%d\t%d\t%s' %(Id, score, score2, text)

	return answer, fi, fi2


