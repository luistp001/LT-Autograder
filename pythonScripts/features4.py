#LT Autograder. A system that automatically grades short answer essays.
#Copyright (C) 2012 Luis Tandalla

import collections, re
from util import *

def feature4(**kwargs):
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
	score = kwargs['score']
	score2 = kwargs['score2']
	fi2 = kwargs['fi2']
	line_match = None
	answer = []
	matchs = []
	index = -1
	
	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}\w*adapt\w*( \w+){0,4}") )
	ans, line_match = fet(text, pats)
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	ans, index, fi, pats = reset(index, fi)
	pats = [ re.compile(r"(\w+ ){0,4}\w*spread\w*( \w+){0,4}") ]
	ans, line_match = fet(text, pats)
	if ans == '1':
		pats = []
		pats.append( re.compile(r"(\w+ ){0,4}\w*ar (\w+ ){0,3}spread\w*( \w+){0,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*spread (\w+ )*((world)|(u)|(south)|(area))\w*( \w+){0,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*spread (\w+ )*fast\w*( \w+){0,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*fast (\w+ )*spread\w*( \w+){0,4}") )		
		pats.append( re.compile(r"(\w+ ){0,4}\w*spread (\w+ )*rapid\w*( \w+){0,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*rapid\w* (\w+ )*spread\w*( \w+){0,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*spread (\w+ )*quick\w*( \w+){0,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*quick\w* (\w+ )*spread\w*( \w+){0,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*((reptil)|(snake)|(python)) (\w+ )*spread\w*( \w+){0,4}") )
		ans, line_match = fet(text, pats)
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}\w*major threat\w*( \w+){0,4}") )
	ans, line_match = fet(text, pats)
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)


	ans, index, fi, pats = reset(index, fi)
	pats = [ re.compile(r"(\w+ ){0,4}\w*threat\w*( \w+){0,4}") ]
	ans, line_match = fet(text, pats)
	if ans == '1':
		pats = []
		pats.append( re.compile(r"(\w+ ){0,4}\w*pos[es] (\w+ ){0,3}threat\w*( \w+){0,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w* caus (\w+ ){0,2}threat\w*( \w+){0,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*ar a (\w+ ){0,2}threat\w*( \w+){0,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*to be a threat\w*( \w+){0,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*threat (\w+ )*((bio)|(enviro))\w*( \w+){0,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*over ?estim (\w+ )*threat\w*( \w+){0,4}") )	
		ans, line_match = fet(text, pats)
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)


	ans, index, fi, pats = reset(index, fi)
	pats = [ re.compile(r"(\w+ ){0,4}\w*invad\w*( \w+){0,4}") ]
	ans, line_match = fet(text, pats)
	if ans == '1':
		pats = []
		pats.append( re.compile(r"(\w+ ){0,4}\w*invad (\w+ )?area\w*( \w+){0,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*invad the ever ?glad\w*( \w+){0,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*invad (\w+ ){0,2}\w*oth\w*( \w+){0,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*invad (\w+ ){0,2}prope\w*( \w+){0,4}") )
		ans, line_match = fet(text, pats)
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}\w*((prolifer)|(over ?pop)|(increas)|(multipli)|(grow))\w*( \w+){0,4}") )
	ans, line_match = fet(text, pats)
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)


	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}\w*new\w* (\w+ ){0,2}((enviro)|(ec(h )?os)|(area)|(territori)|(clim)|(loc)|(home)|(habitat))\w*( \w+){0,4}") )
	ans, line_match = fet(text, pats)
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)


	ans, index, fi, pats = reset(index, fi)
	pats = [ re.compile(r"(\w+ ){0,4}\w*marin\w*( \w+){0,4}") ]
	ans, line_match = fet(text, pats)
	if ans == '1':
		pats = []
		pats.append( re.compile(r"(\w+ ){0,4}\w*good( \w+){1,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*bad( \w+){1,4}") )
		ans, line_match = fet(text, pats)
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)


	ans, index, fi, pats = reset(index, fi)
	pats = [ re.compile(r"(\w+ ){0,4}\w*((python)|(snake)|(reptil))\w*( \w+){0,4}") ]
	ans, line_match = fet(text, pats)
	if ans == '1':
		pats = []
		pats.append( re.compile(r"(\w+ ){0,4}\w*new( \w+){1,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*chang( \w+){1,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*threat( \w+){1,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*place( \w+){1,4}") )
		ans, line_match = fet(text, pats)
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)


	ans, index, fi, pats = reset(index, fi)
	pats = [ re.compile(r"(\w+ ){0,4}\w*florid\w*( \w+){0,4}") ]
	ans, line_match = fet(text, pats)
	if ans == '1':
		pats = []
		pats.append( re.compile(r"(\w+ ){0,4}\w*snake( \w+){1,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*anim( \w+){1,4}") )
		ans, line_match = fet(text, pats)
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)


	ans, index, fi, pats = reset(index, fi)
	pats = [ re.compile(r"(\w+ ){0,4}\w*invas\w*( \w+){0,4}") ]
	ans, line_match = fet(text, pats)
	if ans == '1':
		pats = []
		pats.append( re.compile(r"(\w+ ){0,4}\w*invas (\w+ )*describ (\w+ ){0,4}snake\w*( \w+){0,4}") )			
		pats.append( re.compile(r"(\w+ ){0,4}\w*invas (\w+ )*area\w*( \w+){0,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*invas (\w+ )*that (\w+ )*\w*no?t belong\w*( \w+){0,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*invas (\w+ )*mean (\w+ ){0,2}threat\w*( \w+){0,4}") )
		ans, line_match = fet(text, pats)
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)


	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}\w*can (\w+ )?surv\w*( \w+){1,4}") )
	ans, line_match = fet(text, pats)
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)


	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}\w*((rapid)|(quick))\w*( \w+){1,4}") )
	ans, line_match = fet(text, pats)
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)


	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}\w*nativ\w*( \w+){0,4}") )
	ans, line_match = fet(text, pats)
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)


	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}\w*no?t origin\w*( \w+){0,4}") )
	ans, line_match = fet(text, pats)
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)


	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}\w*((un)|(no?t ))wel\w*( \w+){0,4}") )
	ans, line_match = fet(text, pats)
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)



	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}\w*(\w+ )*natur (\w+ ){0,2}habitat\w*( \w+){0,4}") )
	ans, line_match = fet(text, pats)
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)



	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}\w*(\w+ )*((habitat)|(territori)|(ec(h )?os))\w*( \w+){0,4}") )
	ans, line_match = fet(text, pats)
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)



	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}\w*balanc\w*( \w+){0,4}") )
	ans, line_match = fet(text, pats)
	answer.append ( int(ans) )
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)



	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}\w*take over (\w+ )?((part)|(bio)|(area)|(enviro))\w*( \w+){0,4}") )
	ans, line_match = fet(text, pats)
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)



	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}\w*mean (\w+ )*take over\w*( \w+){0,4}") )
	ans, line_match = fet(text, pats)
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)



	ans, index, fi, pats = reset(index, fi)	
	pats.append( re.compile(r"(\w+ ){0,4}\w*((kill)|(destro))\w*( \w+){0,4}") )
	ans, line_match = fet(text, pats)
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)



	ans, index, fi, pats = reset(index, fi)	
	pats.append( re.compile(r"(\w+ ){0,4}\w*on purp\w*( \w+){0,4}") )
	ans, line_match = fet(text, pats)
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)



	ans, index, fi, pats = reset(index, fi)	
	pats.append( re.compile(r"(\w+ ){0,4}\w*((dobro)|(inner))\w*( \w+){0,4}") )
	ans, line_match = fet(text, pats)
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	ans, index, fi, pats = reset(index, fi)	
	pats.append( re.compile(r"(\w+ ){0,4}\w*argu\w*( \w+){0,4}") )
	ans, line_match = fet(text, pats)
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	ans, index, fi, pats = reset(index, fi)	
	pats.append( re.compile(r"(\w+ ){0,4}\w*controv\w*( \w+){0,4}") )
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	ans, index, fi, pats = reset(index, fi)	
	pats.append( re.compile(r"(\w+ ){0,4}\w*should be (\w+ ){0,5}intro\w*( \w+){0,4}") )
	ans, line_match = fet(text, pats)
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	ans, index, fi, pats = reset(index, fi)	
	pats.append( re.compile(r"(\w+ ){0,4}\w*python (\w+ ){0,5}intro\w*( \w+){0,4}") )
	ans, line_match = fet(text, pats)
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	ans, index, fi, pats = reset(index, fi)	
	pats.append( re.compile(r"(\w+ ){0,4}\w*anywh\w*( \w+){0,4}") )
	ans, line_match = fet(text, pats)
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	ans, index, fi, pats = reset(index, fi)	
	pats.append( re.compile(r"(\w+ ){0,4}bio\w* (\w+ ){0,3}\w*( \w+){0,4}") )
	ans, line_match = fet(text, pats)
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	ans, index, fi, pats = reset(index, fi)	
	pats.append( re.compile(r"(\w+ ){0,4}\w*((while)|(howe))\w*( \w+){0,4}") )
	ans, line_match = fet(text, pats)
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	ans, index, fi, pats = reset(index, fi)	
	pats.append( re.compile(r"(\w+ ){0,4}\w*unche\w*( \w+){0,4}") )
	ans, line_match = fet(text, pats)
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	ans, index, fi, pats = reset(index, fi)	
	pats.append( re.compile(r"(\w+ ){0,4}\w*popul\w*( \w+){0,4}") )
	ans, line_match = fet(text, pats)
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	ans, index, fi, pats = reset(index, fi)	
	pats.append( re.compile(r"(\w+ ){0,4}\w*nonn\w*( \w+){0,4}") )
	ans, line_match = fet(text, pats)
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	ans, index, fi, pats = reset(index, fi)	
	pats.append( re.compile(r"(\w+ ){0,4}\w*affect\w*( \w+){0,4}") )
	ans, line_match = fet(text, pats)
	answer.append ( int(ans) )
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	ans, index, fi, pats = reset(index, fi)	
	pats.append( re.compile(r"(\w+ ){0,4}\w*((bring)|(brought))\w*( \w+){0,4}") )
	ans, line_match = fet(text, pats)
	answer.append ( int(ans) )
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	ans, index, fi, pats = reset(index, fi)	
	pats.append( re.compile(r"(\w+ ){0,4}\w*gov\w*( \w+){0,4}") )
	ans, line_match = fet(text, pats)
	answer.append ( int(ans) )
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	return answer, fi, fi2
	
	














