#LT Autograder. A system that automatically grades short answer essays.
#Copyright (C) 2012 Luis Tandalla


import collections, re
from util import *

def feature5(**kwargs):
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

	while ( text.find('irksom') > -1 ):
		text = text.replace('irksom', 'ribosom')
	while ( text.find('rrna') > -1 ):
		text = text.replace('rrna', 'ribosom')
	

	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}\w*until (\w+ )*stop (co\w* )?(\w+ ){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*until (\w+ )*co\w* (\w+ )*stop\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*reach (\w+ )*stop co\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*hit (\w+ )*stop co\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*stop amino\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*stop co\w*on\w*( \w+){0,4}") )
	ans, line_match = fet(text, pats)
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}\w*((thr?ough)|(on))\w* the (\w+ )?((endo\w*)|(\w?er)|(reti\w)|(rrna))\w*( \w+){0,4}") )
	pats.append( re.compile(r"^(\w+ ){0,5}attac\w* (\w+ )?to ((the)|a) r\w?ib\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*((reach)|(deliv)|(go)|(proce)|(travel)|(run)|(transport)|(arriv)|(attac)|(head)|(wai))\w* (\w+ )?to the (\w+ )?((\w?er)|(reti\w*)|(endo\w*)|(rrna))\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*mrna (\w+ ){0,4}(it )?\w*((reach)|(deliv)|(wai)|(arriv)|(transport)|(head)|(attac)|(go)|(travel)|(run)|(proce))\w* (\w+ ){0,3}((\w?er)|(r\w?ib\w*)|(reti\w*)|(endo\w*)|(rrna))\w*( \w+){0,4}") )
	pats.append( re.compile(r"^(\w+ ){0,5}((reach)|(deliv)|(wai)|(go)|(proce)|(travel)|(run)|(transport)|(arriv)|(attac)|(head))\w* to ((the)|a) r\w?ib\w*( \w+){0,4}") )					
	pats.append( re.compile(r"(\w+ ){0,4}\w*through (\w+ ){0,2}cyto\w* (\w+ )*r\w?ib\w*( \w+){0,4}") )							
	pats.append( re.compile(r"(\w+ ){0,4}\w*mrna (\w+ )*to the (\w+ )?((endo\w*)|(\w?er)|(reti\w)|(rrna))\w*( \w+){0,4}") )		
	pats.append( re.compile(r"(\w+ ){0,4}\w*((onne)|(find)|(look for)|(search)|(encount))\w* (\w+ )*((r\w?ib)|(rrna))\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*enter (((the)|a) )?r\w?ib\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*((after)|(onc))\w* (\w+ )*leav\w* (\w+ )*enter\w* (\w+ )*cyto\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*cyto\w* (\w+ ){0,2}r\w?ib\w*( \w+){0,4}") )
	pats.append( re.compile(r"^(\w+ )*leav\w* (\w+ ){0,10}to the r\w?ib\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*mrna (\w+ )*(\. (\w+ )*)?attac\w (\w+ ){0,2}rib\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*mrna (it )?(\w+ ){2}((messag)|(inform)) (\w+ ){0,4}to (\w+ )?ribosom\w*( \w+){0,4}") )
	ans, line_match = fet(text.replace('mrna .', 'mrna'), pats)
	##########wai to the ribsome reach deliv
	#pats.append( re.compile(r"(\w+ ){0,4}\w*to the (\w+ )*rib\w*( \w+){0,4}") )	
	#pats.append( re.compile(r"(\w+ ){0,4}\w*travel (\w+ ){0,5}to (((the)|(a)) )?ribosom\w*( \w+){0,4}") )		
	#pats.append( re.compile(r"(\w+ ){0,4}\w*(\w+ ){0,5} to the reti\w*( \w+){0,4}") )
	#pats.append( re.compile(r"(\w+ ){0,4}\w*(\w+ ){0,5} to the endo\w*( \w+){0,4}") )
	
	if not line_match:
		pats = []		
 		#pats.append( re.compile(r"(\w+ ){0,4}\w*^(\w+ ){0,5}((reach)|(deliv)|(wai)|(go)|(proce)|(travel)|(run)|(transport)|(arriv)|(attac)|(head))\w* (\w+ ){0,5}r\w?ib\w*( \w+){0,4}") )		
		#pats.append( re.compile(r"(\w+ ){0,4}\w*mrna (\w+ ){0,5}((take)|(carri)) (\w+ )*to (\w+ ){0,2}r\w?ib\w*( \w+){0,4}") )		
		#pats.append( re.compile(r"(\w+ ){0,4}\w*mrna (\w+ )*(\. (\w+ )*)?((attac)|(go))\w (\w+ ){0,3}rib\w*( \w+){0,4}") )
				
		ans2, line_match = fet(text.replace('mrna .', 'mrna'), pats)	
		if line_match : print str(score) + '\t' + str(score2) + '\t' + text
		if line_match : print str(score) + '\t' + str(score2) + '\t' + line_match + '\n'

	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}\w*match (\w+ )*compl[ei]ment\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*pair (\w+ )*compl[ei]ment\w*( \w+){0,4}") )			
	pats.append( re.compile(r"(\w+ ){0,4}\w*compl[ei]ment\w* (\w+ )?codon\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*codon\w* (\w+ )*((match)|(pair)|(attac)|(co((rr)|(nn))ect)|(b[oi]nd))\w* (\w+ )*\w*codon\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*trna (\w+ )*((match)|(pair)|(attac)|(connect)|(hook))\w* (\w+ )*mrna\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*mrna (\w+ )*((match)|(pair)|(attac)|(connect)|(hook))\w* (\w+ )*trna\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*trna (\w+ )*((match)|(pair)|(attac)|(connect)|(hook))\w* (\w+ )*\w?rna\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*an[ti]{2} ?c\w* (\w+ ){0,3}codon\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*codon\w* (\w+ ){0,3}an[ti]{2} ?c\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*match (\w+ )*letter\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*mrna (\w+ )*((match)|(pair)|(attac))\w* (\w+ )*\w*codon\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*trna (\w+ )*((match)|(pair)|(attac)|(connect)|(hook))\w* (\w+ )*((\w?rna)|(amino))\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*copi (\w+ )*compl[ei]ment\w*( \w+){0,4}") )			
		
	ans, line_match = fet(text, pats)

	if not line_match:
		pats = []
		#pats.append( re.compile(r"(\w+ ){0,4}\w*corresp\w*( \w+){0,4}") )												
		
	
		ans2, line_match = fet(text, pats)
		if line_match : print str(score) + '\t' + str(score2) + '\t' + str(sum(answer)) + '\t' + str(answer) + '\t' + text
		if line_match : print str(score) + '\t' + str(score2) + '\t' + str(sum(answer)) + '\t' + str(answer) + '\t' + line_match + '\n'

	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}\w*polyp\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*peptid\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*amino\w* (\w+ )*((b[oi]nd)|(join))\w* (\w+ )*protein\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*p site\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*((link)|(chain)) (\w+ )?amino (\w+ ){1,4}protein\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*((link)|(chain)) (\w+ )?amino acid\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*amino acid ((chain)|(strand))\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*amino acid (\w+ ){0,2}tog\w* (\w+ )*protein\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*protein (\w+ )*amino acid (\w+ ){0,2}tog\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*amino acid (\w+ ){0,2}make\w* (\w+ ){0,2}protein\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*amino acid (\w+ )*protein\w* (\w+ )*attac\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*toge\w* (\w+ )?nucleotid sequ\w* (\w+ )?make (\w+ )?protein\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*trna (\w+ ){0,2}bring (\w+ ){0,2}amino acid (\w+ )*make (\w+ ){0,2}protein\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*trna (\w+ ){0,2}retriev amino acid\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*amino acid (\w+ )?join\w*( \w+){0,4}") )
	ans, line_match = fet(text, pats)

	if not line_match:
		pats = []
		
			
		######## chian of maino acid	
		
#		pats.append( re.compile(r"(\w+ ){0,4}\w*amino\w* (\w+ )*b(i|o)nd\w*( \w+){0,4}") )
#		pats.append( re.compile(r"(\w+ ){0,4}\w*tog\w* (\w+ )*repti\w*( \w+){0,4}") )				
#		pats.append( re.compile(r"(\w+ ){0,4}\w*tog\w+ (\w+ )*make (\w+ )*protein\w*( \w+){0,4}") )			
		
		

		ans2, line_match = fet(text, pats)
		if line_match : print str(score) + '\t' + str(score2) + '\t' + str(sum(answer)) + '\t' + str(answer) + '\t' + text
		if line_match : print str(score) + '\t' + str(score2) + '\t' + str(sum(answer)) + '\t' + str(answer) + '\t' + line_match + '\n'

	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)
	

	ans, index, fi, pats = reset(index, fi)
	#pats.append( re.compile(r"(\w+ ){0,4}\w*trna (\w+ )*amino\w*( \w+){0,4}") )
	#pats.append( re.compile(r"(\w+ ){0,4}\w*amino (\w+ )*trna\w*( \w+){0,4}") )
	#pats.append( re.compile(r"(\w+ ){0,4}\w*protein (\w+ )*ad \w*( \w+){0,4}") )
	#pats.append( re.compile(r"(\w+ ){0,4}\w*mrna (\w+ )*attac (\w+ ){0,5}each ?oth\w*( \w+){0,4}") )

	#pats.append( re.compile(r"(\w+ ){0,4}\w*rib\w*( \w+){0,4}") )
	
	ans, line_match = fet(text, pats)

	if not line_match:
		pats = []
		#pats.append( re.compile(r"(\w+ ){0,4}\w*cyto\w* (\w+ )*rib\w*( \w+){0,4}") )
		#pats.append( re.compile(r"(\w+ ){0,4}\w*rib\w*( \w+){0,4}") )
		#pats.append( re.compile(r"(\w+ ){0,4}\w*mrna (\w+ ){0,4}it go\w* (\w+ ){0,3}rib\w*( \w+){0,4}") )
	#	pats.append( re.compile(r"(\w+ ){0,4}\w*.\w*( \w+){0,4}") )
		ans2, line_match = fet(text, pats)
		#if line_match : print str(score) + '\t' + text + '\n'
		#if line_match : print str(score) + '\t' + line_match + '\n'

	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)


	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}\w*trna read the strand of mrna\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*mrna give the inform to the trna\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*mrna (\w+ ){0,2}((\w+ )?and (\w+ ){0,2})?read (\w+ )*r\w?ib\w*( \w+){0,4}") )		
	pats.append( re.compile(r"(\w+ ){0,4}\w*read (\w+ )?three\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*read the (\w+ )?seq\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*mrna is (\w+ )?trans[lc]\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*trans[cl]\w* (\w+ )?mrna\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*mrna to be copi to trna\w*( \w+){0,4}") )
#	pats.append( re.compile(r"(\w+ ){0,4}\w*ran read\w*( \w+){0,4}") )

#	pats.append( re.compile(r"(\w+ ){0,4}\w*mrna broken down into strands\w*( \w+){0,4}") )
#	pats.append( re.compile(r"(\w+ ){0,4}\w*when the mrna leav the nucleu it find a portion of na and us an enzym to unzip it\w*( \w+){0,4}") )
	
	ans, line_match = fet(text, pats)

	if not line_match:
		pats = []
		
		#pats.append( re.compile(r"(\w+ ){0,4}\w*mrna is (\w+ )?read\w*( \w+){0,4}") )

		#pats.append( re.compile(r"(\w+ ){0,4}\w*co\w*on\w* ((is)|(ar)) (\w+ )?read \w*( \w+){0,4}") )
		
		
		
		
		

		ans2, line_match = fet(text, pats)
		if score > 0:
			if line_match : print str(score) + '\t' + str(score2) + '\t' + str(sum(answer)) + '\t' + str(answer) + '\t' + text
			if line_match : print str(score) + '\t' + str(score2) + '\t' + str(sum(answer)) + '\t' + str(answer) + '\t' + line_match + '\n'

	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}\w*through (\w+ ){0,2}nuclear pore\w*( \w+){0,4}") )

	
	ans, line_match = fet(text, pats)

	if not line_match:
		pats = []
		#pats.append( re.compile(r"(\w+ ){0,4}\w*rib\w*( \w+){0,4}") )
		#pats.append( re.compile(r"(\w+ ){0,4}\w*mrna (\w+ ){0,4}it go\w* (\w+ ){0,3}rib\w*( \w+){0,4}") )
	#	pats.append( re.compile(r"(\w+ ){0,4}\w*.\w*( \w+){0,4}") )
		ans2, line_match = fet(text, pats)
		if line_match : print str(score) + '\t' + str(score2) + '\t' + str(sum(answer)) + '\t' + str(answer) + '\t' + text
		if line_match : print str(score) + '\t' + str(score2) + '\t' + str(sum(answer)) + '\t' + str(answer) + '\t' + line_match + '\n'

	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	
	#if line_match and score == 3: print str(score) + '\t' + str(answer) + '\t' + text
	#if score == 1 and score2 == 1 and sum(answer) < 1: 
	#if (score == 1 and sum(answer) < 1) or ( score == 2 and sum(answer) < 3) or ( score == 3 and sum(answer) < 4): 

#	if (score == 3 and sum(answer) < 4): 
#		print str(Id) + '\t' + str(score) + '\t' + str(score2) + '\t' +str(answer) + '\t' + text +'\n'
#		for m in matchs:
#			print m
#		print '\n'

	
	return answer, fi, fi2










