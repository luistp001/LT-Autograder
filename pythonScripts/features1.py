#LT Autograder. A system that automatically grades short answer essays.
#Copyright (C) 2012 Luis Tandalla

import collections, re
from util import *

def feature1(**kwargs):
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
	
	index = 0
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}\w*(how )?((much)|(mani)) (\w+ ){0,4}((vinegar)|(finger)|(liquid))\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*how much (\w+ ){1,2}((put)|(fill))\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*((vinegar)|(finger)) (\w+ ){0,4}measur\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*((aunt)|(man)|(a?mount)|(measur)|(volum)|(quantiti)) (\w+ ){0,3}((vinegar)|(finger)|(liquid))\w*( \w+){0,4}") )
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)


	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}\w*((size)|(volum)) (\w+ ){0,5}((contain)|(cup))\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*how ((big)|(larg)|(wide)) (\w+ ){0,3}((contain)|(cup))\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*measur (\w+ ){0,2}contain\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*contain (\w+ ){0,4}size\w*( \w+){0,4}") )
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append ( re.compile(r"(\w+ ){0,4}\w*((sort)|(type)|(kind)) (\w+ ){0,3}((contain)|(cup))\w*( \w+){0,4}") )
	###type or size my contain
	pats.append ( re.compile(r"(\w+ ){0,4}\w*materi of the contain\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*what (\w+ ){0,3}contain\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*((describ)|(specif\w*)) (\w+ ){0,3}contain\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*contain (\w+ ){0,3} ((us)|(need))\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*contain ar made of\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*us as (a )?contain\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*know (\w+ )?about (\w+ ){1,3}contain\w*( \w+){0,4}") )
	#pats.append ( re.compile(r"what ar (\w +){0,3}contain") )
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append ( re.compile(r"(\w+ ){0,4}\w*((kind)|(type)) of (the\w* (\w+ )?)?(differ (\w+ )?)?(\w+ )?((materi)|(marbl)|(sampl)|(object)|(substanc))\w*( \w+){0,4}")  )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*materi type\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*speci materi\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*((what)|(which)) (\w+ ){0,3}((sampl)|(materi)|(item)|(substanc)|(object)) ((ar)|(is)|(were)|(wa))\w*( \w+){0,4}"))
	pats.append ( re.compile(r"(\w+ ){0,4}\w*know (\w+ ){0,3}((sampl)|(materi)|(item)|(substanc)|(object)) ((ar)|(is)|(were)|(wa))?\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*know (\w+ ){0,3}what (\w+ ){1,3}((materi)|(sampl)) ((ar)|(is)|(were)|(wa))?\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*((know)|(need)) the materi\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*list of ((materi)|(suppli)|(object))\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*what materi\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*what (\w+ ){1,2}materi (\w+ ){0,3}((sampl)|(item)|(substanc)|(object))\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*what ((were)|(ar)|(is)|(wa)) the (\w+ )?(\w+ )?((sampl)|(item)|(substanc)|(object))\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*name (\w+ ){1,3}((sampl)|(item)|(element)|(substanc)|(object))?\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*((materi)|(sampl)|(object)) (\w+ ){0,5}((us)|(need))\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*mean\w* by (\w+ ){0,3} sampl\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*((explain)|(give)|(told)|(tell)|(describ)|(list)|(stat)|(nam)|(identifi)|(specifi)|(writ)|(includ))\w* (\w+ ){0,4}((sampl)|(substanc)|(materi)|(object))\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*sampl ((nam)|(typ))\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*told the sampl\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*know which sampl\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*word sampl\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*specifi (\w+ ){0,3}sampl\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*know (\w+ ){1,15}and (\w+ ){1,3}sampl\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*materi (\w+ ){0,3}((describ)|(list)|(stat)|(name)|(identifi)|(specifi)|(written)|(includ))\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*sampl of what\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*what do we us for (the )?sampl\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*us (\w+ )?same materi\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*type of rock\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*kind of stone\w*( \w+){0,4}") )
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)


	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append ( re.compile(r"(\w+ ){0,4}\w*size (of (\w+ ){0,2})?(\w+ ){0,3}((materi)|(marbl)|(sampl))\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*how ((big)|(larg)|) (\w+ ){0,3}((materi)|(sampl)|(object)|(piec))\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*how much (\w+ ){0,2}materi\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*((sampl)|(materi)|(substanc)) (\w+ ){0,4}size\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*how larg a sampl\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*small or piec\w*( \w+){0,4}") )
	#pats.append ( re.compile(r"amount of each sampl") )
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append ( re.compile(r"(\w+ ){0,4}\w*((type)|(kind)|(brand)) of vinegar\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*((concentr)|( \w?h)|(acid)) (\w+ ){0,5}vinegar\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*vinegar (\w+ )?((concentr)|(acid))\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*know (\w+ )?vinegar (\w+ )?((us)|(need))\w*( \w+){0,4}") )
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	#pats.append ( re.compile(r"amount of distilled water to rinse" ) )
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append ( re.compile(r"(\w+ ){0,4}\w*where (\w+ ){1,3}((leav)|(put)|(store)|(sit)|(keep)|(store)|(pour)) (\w+ ){0,3}((experi)|(materi)|(sampl)|(contain)|(cup))\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*where (\w+ ){0,2}place (\w+ ){0,2}((sampl))\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*what (\w+ ){0,2}place (\w+ ){0,2}sampl\w*( \w+){0,4}") )
	#pats.append ( re.compile(r"where (\w+ ){0,2}place (\w+ ){0,2}contain") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*where (\w+ ){0,3}the (\w+ ){0,3}((materi)|(sampl)|(contain)) (\w+ ){0,3}((leav)|(put)|(store)|(sit)|(keep))\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*where the ((sampl)|(contain)) ar( \w+){1,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*where thei left the contain\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*where (\w+ )?((sampl)|(contain))? (\w+ )?((stai)|(dr(i|y)))\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*where. (\w+ ){0,3}leav these contain\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*where ((ar)|(were)) (\w+ )?((sampl)|(contain))\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*where (\w+ ){0,3}dr(i|y)\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*where do thei go\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*where to let the(se)? ((sampl)|(contain))\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*area ([a-z]+ ){0,4}to( \w+){1,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*how to store\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*refri\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*((locat)|(site)) (\w+ ){1,2}((contain)|(sampl))\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*outsid\w*( \w+){0,4}") )
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append ( re.compile(r"(\w+ ){0,4}\w*surfac ar\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*shape (\w+ ){0,3}sampl\w*( \w+){0,4}") )
	ans, line_match = fet(text, pats)
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append ( re.compile(r"(\w+ ){0,4}\w*how? long (\w+ ){1,7}(([a-z]?rin?[a-z])|(wash))\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*time (\w+ ){0,2}rin?s\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*rins (\w+ ){0,1}how long\w*( \w+){0,4}" ))
	pats.append ( re.compile(r"(\w+ ){0,4}\w*time for rin?s\w*( \w+){0,4}" ))
	ans, line_match = fet(text, pats)
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append ( re.compile(r"(\w+ ){0,4}\w*room temp( \w+){1,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*what temp\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*and the temp\w*( \w+){0,4}") )
	#pats.append ( re.compile(r"what ([a-z]+ ){0,1}condit") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*room temperatur\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*temperatur (\w+ ){3,3}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*temp((eratur)|( \.)) of the ((room)|(surround))\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*temperatur in the( \w+){1,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*temperatur at which( \w+){1,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*kind of ((temperatur)|(environ))\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*includ (\w+ ){0,2}temp\w*( \w+){0,4}") )
		
	ans, line_match = fet(text, pats)		
	ans, line_match = fet(text, pats)
	if ans == '1':
		if text.find('temperatur of the vinegar') > 0:
			ans = '0'	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append ( re.compile(r"(\w+ ){0,4}\w*how to ((rins)|(dr(i|y)))\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*how to ((\w+ ){0,3}(sampl ))?(\w+ ){0,3}((dr(i|y))|(rin))\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*how to (\w+ ){0,2}((dr(i|y))|(rins))\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*how (\w+ )?sampl (\w+ ){1,2}wash\w*( \w+){0,4}") )
	ans, line_match = fet(text, pats)
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append ( re.compile(r"(\w+ ){0,4}\w*((close)|(cover)) (\w+ ){0,2}((sampl)|(contain))\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*((sampl)|(contain)) (\w+ ){0,2}cover\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*top (\w+ ){0,2}contain\w*( \w+){0,4}") )
	ans, line_match = fet(text, pats)
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append ( re.compile(r"(\w+ ){0,4}\w*((fulli)|(complet)) submerg\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*whole (\w+ ){0,5}submerg?\w*( \w+){0,4}") )
	ans, line_match = fet(text, pats)
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append ( re.compile(r"(\w+ ){0,4}\w*heat\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*dark\w*( \w+){0,4}") )
	pats.append ( re.compile(r"(\w+ ){0,4}\w*type of climat\w*( \w+){0,4}") )
	ans, line_match = fet(text, pats)
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	return answer, fi, fi2
