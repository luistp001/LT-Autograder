#LT Autograder. A system that automatically grades short answer essays.
#Copyright (C) 2012 Luis Tandalla

import collections, re
from util import *

def feature2(**kwargs):
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
	pats.append( re.compile(r"(\w+ ){0,4}\w*b (\w+ ){1,4}the most\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*stretch the most\w*( \w+){0,4}\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*the most stretch\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*the most ductil\w*( \w+){0,4}") )

	pats.append( re.compile(r"(\w+ ){0,4}\w*b (\w+ ){0,4}stretch (\w+ )?(the )?((most)|(f(a|u)rthe)|(longest)|(best))\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*plastic stretch (\w+ )?(the )?((most)|(f(a|u)rthest)|(longest))\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*stretch (\w+ )?(the )?((most)|(f(a|u)rthest)|(longest)|(greatest)) (\w+ ){0,4}b\w*( \w+){0,4}") )

	pats.append( re.compile(r"(\w+ ){0,4}\w*the stretchiest (\w+ ){1,5}b\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*the most (\w+ ){1,3}b\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*stretchi \w*( \w+){0,4}") )
	
	pats.append( re.compile(r"(\w+ ){0,4}\w*b (\w+ ){1,3}the stretch\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*b (\w+ ){1,2}\w+est\w*( \w+){0,4}") )

	pats.append( re.compile(r"(\w+ ){0,4}\w*b (\w+ )?stretch ((more)|(longer))\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*b plastic wa longer\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*b (\w+ ){1,2}more stretch\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*b is the stretch\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*b (\w+ ){2}high\w* stre\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*flexibl\w*( \w+){0,4}") )


	ans, line_match = fet(text, pats)
	#ans = '0'
	if ans == '1':
		if text.find( ' d stretch the most') > 0:			ans = '0'
		if text.find( ' a stretch the most') > 0:			ans = '0'
		if text.find( ' c stretch the most') > 0:			ans = '0'

	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}\w*type a is (\w+ )?stronger\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*plastic a wa the least stretchi\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*a (\w+ )?the str[ao]ngest\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*a (\w+ ){0,3}most r\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*the most durabl\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*a (\w+ )more durabl\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*a (\w+ ){1,5}the strongest\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*stretch constanc\w*( \w+){0,4}") )


	ans, line_match = fet(text, pats)
	#ans = '0'
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}\w*stretch the least\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*the least stretch\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*a (\w+ ){0,2}the least\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*the least (\w+ )a\w*( \w+){0,4}") )
	

	ans, line_match = fet(text, pats)
	#ans = '0'
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)
	

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}\w*((result)|(experi)) (\w+ )?not valid\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*differ stre\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*differ (\w+ ){0,3}differ\w*( \w+){0,4}") )
	

	ans, line_match = fet(text, pats)
	#ans = '0'
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)
	




	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}\w*tr[ia]{2}l\w*( \w+){0,4}") )
	ans, line_match = fet(text, pats)
	if ans == '1':
		pats = []	
		pats.append( re.compile(r"(\w+ ){0,4}\w*more (\w+ )?tr[ia]{2}l\w*( \w+){0,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*more than (\w+ )?two tr[ia]{2}l\w*( \w+){0,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*third tr[ia]{2}l\w*( \w+){0,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*three tr[ia]{2}l\w*( \w+){0,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*there tr[ia]{2}l\w*( \w+){0,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*fourth tr[ia]{2}l\w*( \w+){0,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*four tr[ia]{2}l\w*( \w+){0,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*anoth tr[ia]{2}l\w*( \w+){0,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*addit tr[ia]{2}l\w*( \w+){0,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*a red tr[ia]{2}l\w*( \w+){0,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*repeat (\w+ )?tr[ia]{2}l\w*( \w+){0,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*ad\w* (\w+ )?tr[ia]{2}l\w*( \w+){0,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*tr[ia]{2}l a red\w*( \w+){0,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*number of tr[ia]{2}l\w*( \w+){0,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*tr[ia]{2}l instead\w*( \w+){0,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*perform (\w+ )?tr[ia]{2}l\w*( \w+){0,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*amount of tr[ia]{2}l\w*( \w+){0,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*tr[ia]{2}l not just\w*( \w+){0,4}") )
 		ans, line_match = fet(text, pats)
 	if ans == '0':
 		pats = []	
		pats.append( re.compile(r"(\w+ ){0,4}\w*time\w*( \w+){0,4}") )
		ans, line_match = fet(text, pats)
		if ans == '1':
			pats = []	
			pats.append( re.compile(r"(\w+ ){0,4}\w*more (\w+ )?time\w*( \w+){0,4}") )
			pats.append( re.compile(r"(\w+ ){0,4}\w*mani time\w*( \w+){0,4}") )
			pats.append( re.compile(r"(\w+ ){0,4}\w*a red time\w*( \w+){0,4}") )
			pats.append( re.compile(r"(\w+ ){0,4}\w*anoth time\w*( \w+){0,4}") )
			pats.append( re.compile(r"(\w+ ){0,4}\w*time instead\w*( \w+){0,4}") )
			pats.append( re.compile(r"(\w+ ){0,4}\w*third time\w*( \w+){0,4}") )
			ans, line_match = fet(text, pats)
	if ans == '0':
 		pats = []	
		pats.append( re.compile(r"(\w+ ){0,4}\w*more test\w*( \w+){0,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*repeat the (\w+ )?procedur\w*( \w+){0,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*repeat the test\w*( \w+){0,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*repeat all\w*( \w+){0,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*((redo)|(repeat)) the experi\w*( \w+){0,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*((trial)|(experi)) again\w*( \w+){0,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*than twice\w*( \w+){0,4}") )
		ans, line_match = fet(text, pats)
	#do three

	#ans = '0'
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)
	

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}\w*((\weigh)|(wai)|(wright)\w*)\w*( \w+){0,4}") )
	ans, line_match = fet(text, pats)	

	if ans == '1':
		if ( text.find( 'wright') > 0):
			text.replace ('wright', 'weight')
		pats = []	
		pats.append( re.compile(r"(\w+ ){0,4}\w*ho\w{0,2} much ((\weigh\w*)|(wai\w*))\w*( \w+){0,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*h\w{0,3} much ((\weigh\w*)|(wai\w*)|(wright))\w*( \w+){0,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*ho\w{0,2} ((much)|(mani)|(heavi))\w* (\w+ )?(the )?((\weigh\w*)|(mass))\w*( \w+){0,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*amount of (\w+ )?\weigh\w*( \w+){0,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*mass of the \weigh\w*( \w+){0,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*measur of the \weigh\w*( \w+){0,4}") )
		#pats.append( re.compile(r"(\w+ ){0,4}\w*certain \weight\w*( \w+){0,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*((stat)|(includ)|(determin)|(know)|(specif)|(giv)|(provid)|(sai))\w* (\w+ ){0,4}\weigh\w*( \w+){0,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*same \weigh\w*( \w+){0,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*\weigh\w* \weigh\w*( \w+){0,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*size of the \weigh\w*( \w+){0,4}") )
		#pats.append( re.compile(r"(\w+ ){0,4}\w*same wai\w*( \w+){0,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*what (\w+ ){0,4}\weigh\w*( \w+){0,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*number of \weigh\w*( \w+){0,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*\weigh\w* (\w+ ){0,4}same\w*( \w+){0,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*exact (\w+ ){0,2}\weigh\w*( \w+){0,4}") )

		#put same amount of weight
			#same wai
 		#includ the weight

	 	#determin the weight
		#know the weight
		#specifi the amount of weight

		#state the amount of weight
			#the weight should have been the exact same size
			 #weight us for everi plastic sampl constant
		#same amount of weight
		#specif weight of the weight
		#specif amount of weight
		#specifi the amount of weight
		ans, line_match = fet(text, pats)


	
	#ans = '0'
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)
	

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}\w*same (\w+ ){0,2}length\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*same (\w+ ){0,2}distanc\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*uniform length\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*constant length\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*constant size\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*keep (\w+ ){0,3}constant\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*same size\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*same measur\w*( \w+){0,4}") )
	#pats.append( re.compile(r"(\w+ ){0,4}\w*same amount of\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*equal size\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*equal length\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*length (of (\w+ ){0,2}){0,2}(\w+ ){0,3}same\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*length (and (\w+ ){0,2})?(\w+ ){0,3}constant\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*same amount of (\w+ )?plastic\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*equal amount of (\w+ )?plastic\w*( \w+){0,4}") )
	#same length of differ plastic
		#size of each materi befor be stretch should be held constant . 
	#rest the plastic at the same length
 	#keep all the other plastic at the same length
	#plastic sampl were the same length
		#the length is not the same
		#be clear about the length of each plastic
		#each plastic sampl the same size
		#specif size of the origin piec of plastic
		#length is not the same
		#length of each type of plastic be the same
		#standard length
		#same size plastic


	ans, line_match = fet(text, pats)
	#ans = '0'
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)
	

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}\w*plastic\w*( \w+){0,4}") )
	ans, line_match = fet(text, pats)
	
	if ans == '1':
		pats = []
		pats.append( re.compile(r"(\w+ ){0,4}\w*how long (\w+ ){1,3}plastic\w*( \w+){0,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*plastic how long\w*( \w+){0,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*plastic length\w*( \w+){0,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*how much plastic\w*( \w+){0,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*how much of the plastic \w+\w*( \w+){0,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*measur of (\w+ )plastic \w+\w*( \w+){0,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*amount of plastic\w*( \w+){0,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*measur the plastic \w+\w*( \w+){0,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*length of (the )?plastic\w*( \w+){0,4}") )
		ans, line_match = fet(text, pats)

		if ans == '1' and line_match.find('time') > 0:
			ans = '0'
	if ans == '0':
		pats = []
		pats.append( re.compile(r"(\w+ ){0,4}\w*((origin)|(initi)|(standard)|(start)|(certain)|(exact)|(first)) ((length)|(measur)|(size)|(long))\w*( \w+){0,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*percentag stretch\w*( \w+){0,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*((measur)|(check)) (the )?length\w*( \w+){0,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*((includ)|(specif)|(list)|(inform)|(set)|(provid)|(document)|(giv)|(sai)|(inlaid)|(show))\w* (\w+ ){0,3}((length)|(size))\w*( \w+){0,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*specif size\w*( \w+){0,4}") )
		pats.append( re.compile(r"(\w+ ){0,4}\w*by measur\w*( \w+){0,4}") )
		ans, line_match = fet(text, pats)
	#pats.append( re.compile(r"(\w+ ){0,4}\w*length (\w+ ){0,2}plastic\w*( \w+){0,4}") )
		#the measur of everi plastic
	#record the origin length
	#initi length of the plastic wa
	#plastic how long ar thei etch
		#measur of the plastic
	#start length
	#specifi the start length
 		#each plastic sampl the same size
		#specif size of the origin piec
		#specif about the length of each piec
		#list the length of the plastic
		#how long the plastic
		#measur the length of the plastic

					#2967

	
	#ans = '0'
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)
	

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}\w*where the clamp\w*( \w+){0,4}") )

	ans, line_match = fet(text, pats)
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}\w*same thick\w*( \w+){0,4}") )

	ans, line_match = fet(text, pats)
	#ans = '0'
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)
	#be more specif

	#the temperatur is kept constant

	#how to add weight
	#2798 2814 2820 2905 3008 3141 3142 3101 3197 3247
	#if Id in [2798, 2814, 2820, 3002, 3148, 3196, 3850, 2905, 2963, 3008, 3066, 3141, 3142, 3101, 3162, 3197, 3252, 3247]:
	#3395 3956 3879 3794 3866 3781 3732 3723 2798 282 2886 2888
	#if Id in [3070, 3403, 3395, 4022, 4009, 3956, 3850, 3806, 3879, 3794, 3866, 3781, 3732, 3709, 3723, 2798, 2820, 2886, 2888, 3148, 3196]:
	#	answer = [0,0,0,1,1,1]

	return answer, fi, fi2









