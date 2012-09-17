#LT Autograder. A system that automatically grades short answer essays.
#Copyright (C) 2012 Luis Tandalla


import collections, re
from util import *

def feature6(**kwargs):
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
	pats.append( re.compile(r"(\w+ )*\w*act(iv)? transport( \w+)*" ) )	
	ans2, line_match2 = fet(text, pats)	
	ans = '0'
	if line_match2:
		pats = []
		pats.append( re.compile(r"(\w+ )*\w*e[nv]er\w* (\w+ )?(is )?((requir)|(us)|(need)|(invol))\w*( \w+)*" ) )	
		pats.append( re.compile(r"(\w+ )*\w*((requir)|(us)|(need)|(take)) (\w+ ){0,5}e[nv]er\w*( \w+)*" ) )
		pats.append( re.compile(r"(\w+ )*\w*((against)|(up)|(across)) the concentr gr\w*( \w+)*" ) )
		pats.append( re.compile(r"(\w+ )*\w*from (\w+ ){0,3}((low)|(less))\w* (\w+ )?to (\w+ ){0,3}((high)|(great))\w*( \w+)*" ) )
		pats.append( re.compile(r"(\w+ )*\w*with the aid\w*( \w+)*" ) )
		pats.append( re.compile(r"(\w+ )*\w*us of atp?\w*( \w+)*" ) )
		ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	ans, index, fi, pats = reset(index, fi)
	#pats.append( re.compile(r"(\w+ )*\w*select membran\w* (\w+ )*" ) )
	#possible_sentences = re.findall(r"((\w+ )*pass(iv)? ((transport)|(diffus))( \w+)*)", text.replace( 'passiv transport .', 'passiv transport')) 
	possible_sentences = re.findall(r"((\w+ )*pass(iv)?( \w+)*)", text.replace( 'passiv transport .', 'passiv transport')) 		
	#anst, line_match2 = fet(text, pats)
	ans = '0'
	for possible_sentence in possible_sentences:
	  line_match2 = possible_sentence[0]
	  if ans == '0':
	
	#if line_match2:
		#if score > 0: print str(Id) + '\t' + str(score) + '\t' + str(score2) + '\t' + line_match2
		pats = []
		pats.append( re.compile(r"(\w+ )*\w*energi is not\w*( \w+)*" ) )
		pats.append( re.compile(r"(\w+ )*\w*no energ\w*( \w+)*" ) )
		pats.append( re.compile(r"(\w+ )*\w*neither energ\w*( \w+)*" ) )
		pats.append( re.compile(r"(\w+ )*\w*no(t|r) (\w+ ){0,4}energ\w*( \w+)*" ) )
		pats.append( re.compile(r"(\w+ )*\w*without (\w+ ){0,3}energ\w*( \w+)*" ) )
		pats.append( re.compile(r"(\w+ )*\w*doesn\w* (\w+ ){0,3}energ\w*( \w+)*" ) )
		pats.append( re.compile(r"(\w+ )*\w*((along)|(with)) the (concentr )?gra\w*( \w+)*" ) )
		
		#ans, line_match = fet(line_match2, pats)
		ans, line_match = fet(line_match2 , pats)
		#if line_match:	print str(Id) + '\t' + str(score) + '\t' + str(score2) + '\t' + line_match2
		#if not line_match and score > 0:	print str(Id) + '\t' + str(score) + '\t' + str(score2) + '\t' + line_match2
		
		#if line_match : print str(score) + '\t' + text
		#if line_match : print str(score) + '\t' + line_match
	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	ans, index, fi, pats = reset(index, fi)
	#pats.append( re.compile(r"(\w+ )*\w*select membran\w* (\w+ )*" ) )
	possible_sentences = re.findall(r"((\w+ )*\w*pump( \w+)*)", text) 
	#anst, line_match2 = fet(text, pats)
	ans = '0'
	for possible_sentence in possible_sentences:
	  line_match2 = possible_sentence[0]
	  if ans == '0':
	
	#if line_match2:
		#if score > 0: print str(Id) + '\t' + str(score) + '\t' + str(score2) + '\t' + line_match2
		pats = []
		pats.append( re.compile(r"(\w+ )*\w*sodium potassium pump\w*( \w+)*" ) )
		
		#ans, line_match = fet(line_match2, pats)
		ans, line_match = fet(line_match2 , pats)
		#if line_match:	print str(Id) + '\t' + str(score) + '\t' + str(score2) + '\t' + line_match2
		#if not line_match and score > 0:	print str(Id) + '\t' + str(score) + '\t' + str(score2) + '\t' + line_match2
		
		#if line_match : print str(score) + '\t' + text
		#if line_match : print str(score) + '\t' + line_match
	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)


	

	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ )*\w*di((ff)|(sc))us\w* (\w+ )*" ) )
#	possible_sentences = re.findall(r"((\w+ )*\w*diffus\w*( \w+)*)", text) 
	anst, line_match2 = fet(text, pats)
	ans = '0'

#	for possible_sentence in possible_sentences:
#	  line_match2 = possible_sentence[0]
#	  if ans == '0':
	if line_match2:
		#if score > 0: print str(Id) + '\t' + str(score) + '\t' + str(score2) + '\t' + line_match2
		pats = []
		pats.append( re.compile(r"(\w+ )*\w*((along)|(with)|(follow)) (\w+ )concentr gra\w*( \w+)*" ) )
		pats.append( re.compile(r"(\w+ )*\w*((high)|(great))\w* (\w+ )?\w*to (\w+ ){0,3}((low)|(less))\w*( \w+)*" ) )			
		pats.append( re.compile(r"(\w+ )*\w*((high)|(great))\w* (\w+ )*move (\w+ )*to (\w+ ){0,4}((low)|(less))\w*( \w+)*" ) )			
		pats.append( re.compile(r"(\w+ )*\w*without (\w+ ){0,3}energ" ) )
		
		#ans, line_match = fet(line_match2, pats)
		ans, line_match = fet(text, pats)
		#if line_match:	print str(Id) + '\t' + str(score) + '\t' + str(score2) + '\t' + line_match2
		#if not line_match and score > 0:	print str(Id) + '\t' + str(score) + '\t' + str(score2) + '\t' + line_match2
		
		#if line_match : print str(score) + '\t' + text
		#if line_match : print str(score) + '\t' + line_match

	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)


		
	ans, index, fi, pats = reset(index, fi)
	#pats = []
	#pats.append( re.compile(r"(\w+ )*\w*osmosi\w* (\w+ )*" ) )
	possible_sentences = re.findall(r"((\w+ )*\w*osmosi\w*( \w+)*)", text.replace( 'osmosi . ', 'osmosi ')) 
	#anst, line_match2 = fet(text, pats)
	ans = '0'
	for possible_sentence in possible_sentences:
	  line_match2 = possible_sentence[0]
	  if ans == '0':
	#if line_match2:
		pats = []
		pats.append( re.compile(r"(\w+ )*low\w* (\w+ )*high\w* ?(\w+ )*" ) ) 
		pats.append( re.compile(r"(\w+ ){0,4}((mo)|(transport)|(diff)|(transfer)|(flow)|(pass)|(come))\w* (of )?water (\w+ ){0,6}\w?((cross)|(in(to)? ((and)|(or)) out of)|(th(ro)?u(gh)?)|(between)) (\w{1,3} )?(\w+ ){0,2}((cell)|(membran)|(barrier))" ) )		
		pats.append( re.compile(r"(\w+ ){0,4}water (\w+ )?((mo)|(transport)|(diff)|(transfer)|(flow)|(pass)|(come))\w* (\w+ ){0,6}\w?((cross)|(in(to)? ((and)|(or)) out of)|(th(ro)?u(gh)?)|(between)) (\w{1,3} )?(\w+ ){0,2}((cell)|(membran)|(barrier))" ) )		
		pats.append( re.compile(r"osmosi (which )?(\w+ )?(the )?((mo)|(transport)|(diff)|(transfer)|(flow)|(pass)|(come))\w* (\w{1,3} )water" ) )		
		pats.append( re.compile(r"(\w+ )*water (\w+ )*go\w* ?(\w+ )*" ) )	
		pats.append( re.compile(r"hyperto\w* (\w+ )*hypoto\w*" ) )
		pats.append( re.compile(r"hypoto\w* (\w+ )*hyperto\w*" ) )
		pats.append( re.compile(r"(\w+ )*high\w* (\w+ )*low\w* ?(\w+ )*" ) ) #1
		pats.append( re.compile(r"(\w+ )*low\w* (\w+ )*high\w* ?(\w+ )*" ) ) #2
		pats.append( re.compile(r"substanc (\w+ )*pass (\w+ )*membran\w* ?(\w+ )*" ) )
		pats.append( re.compile(r"(\w+ )*semi permeabl membran\w* ?(\w+ )*" ) )
		pats.append( re.compile(r"(\w+ )*gradient ?(\w+ )*" ) ) #1
		pats.append( re.compile(r"(\w+ )*get\w* water ?(\w+ )*" ) )
		pats.append( re.compile(r"(\w+ )*pull\w* water ?(\w+ )*" ) )			
		pats.append( re.compile(r"(\w+ )*pass\w* (\w+ )*water ?(\w+ )*" ) )
		pats.append( re.compile(r"(\w+ )*water (\w+ )*pass\w* ?(\w+ )*" ) )
		pats.append( re.compile(r"(\w+ )*let\w* (\w+ )*water ?(\w+ )*" ) ) ########### 1.5					
		pats.append( re.compile(r"(\w+ )*\w*water diffus\w*( \w+)*" ) ) ########### 1.5					
		ans, line_match = fet(line_match2, pats)
		if Id == 15327:
			print ans 
			print line_match
	

		
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ )*\w*fac\w* diffus\w* (\w+ )*" ) )
#	possible_sentences = re.findall(r"((\w+ )*\w*diffus\w*( \w+)*)", text) 
	anst, line_match2 = fet(text, pats)
	ans = '0'

#	for possible_sentence in possible_sentences:
#	  line_match2 = possible_sentence[0]
#	  if ans == '0':
	if line_match2:
		#if score > 0: print str(Id) + '\t' + str(score) + '\t' + str(score2) + '\t' + line_match2
		pats = []
		pats.append( re.compile(r"(\w+ )*\w*protein channel\w*( \w+)*" ) )
		pats.append( re.compile(r"(\w+ )*\w*((requir)|(us)|(need)|(take)) (\w+ ){0,5}e[nv]er\w*( \w+)*" ) )
				
		
		#ans, line_match = fet(line_match2, pats)
		ans, line_match = fet(text, pats)
		#if line_match:	print str(Id) + '\t' + str(score) + '\t' + str(score2) + '\t' + line_match2
		#if not line_match and score > 0:	print str(Id) + '\t' + str(score) + '\t' + str(score2) + '\t' + line_match2
		
		#if line_match : print str(score) + '\t' + text
		#if line_match : print str(score) + '\t' + line_match

	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ )*\w*endocytosi\w* (\w+ )*" ) )
#	possible_sentences = re.findall(r"((\w+ )*\w*diffus\w*( \w+)*)", text) 
	anst, line_match2 = fet(text, pats)
	ans = '0'

#	for possible_sentence in possible_sentences:
#	  line_match2 = possible_sentence[0]
#	  if ans == '0':
	if line_match2:
		#if score > 0: print str(Id) + '\t' + str(score) + '\t' + str(score2) + '\t' + line_match2
		pats = []
		pats.append( re.compile(r"(\w+ )*\w*surround a substanc\w*( \w+)*" ) )
		pats.append( re.compile(r"(\w+ )*\w*cell surround\w*( \w+)*" ) )
		pats.append( re.compile(r"(\w+ )*\w*engulf\w*( \w+)*" ) )
		pats.append( re.compile(r"(\w+ )*\w*vesicl around\w*( \w+)*" ) )
		
		#ans, line_match = fet(line_match2, pats)
		ans, line_match = fet(text, pats)
		#if line_match:	print str(Id) + '\t' + str(score) + '\t' + str(score2) + '\t' + line_match2
		#if not line_match and score > 0:	print str(Id) + '\t' + str(score) + '\t' + str(score2) + '\t' + line_match2
		
		#if line_match : print str(score) + '\t' + text
		#if line_match : print str(score) + '\t' + line_match

	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	ans, index, fi, pats = reset(index, fi)
	#pats = []
	#pats.append( re.compile(r"(\w+ )*\w*select membran\w* (\w+ )*" ) )
	possible_sentences = re.findall(r"((\w+ )*\w*((semi)|(select)) ?(\w+ )?(membran\w*)?\w*( \w+)*)", text) 
	#anst, line_match2 = fet(text, pats)
	ans = '0'

	for possible_sentence in possible_sentences:
	  line_match2 = possible_sentence[0]
	  if ans == '0':
		pats = []
		pats.append( re.compile(r"(\w+ )*\w*decid\w*( \w+)*" ) )
		pats.append( re.compile(r"(\w+ )*\w*choose\w*( \w+)*" ) )
		pats.append( re.compile(r"(\w+ )*\w*control what\w*( \w+)*" ) )
		pats.append( re.compile(r"(\w+ )*\w*allow (\w+ )?certain\w*( \w+)*" ) )
		pats.append( re.compile(r"(\w+ )*\w*let certain\w*( \w+)*" ) )
		pats.append( re.compile(r"(\w+ )*\w*let thing\w*( \w+)*" ) )
		####let thing in and out of the cell that ar smalle
		
		#ans, line_match = fet(line_match2, pats)
		ans, line_match = fet(text, pats)
		#if line_match:	print str(Id) + '\t' + str(score) + '\t' + str(score2) + '\t' + line_match2
		#if not line_match and score > 0:	print str(Id) + '\t' + str(score) + '\t' + str(score2) + '\t' + line_match2
		
		#if line_match : print str(score) + '\t' + text
		#if line_match : print str(score) + '\t' + line_match

	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)


	if score == 1 and sum(answer) == 0: print str(Id) + '\t' + str(score) + '\t' + str(score2) + '\t' + str(answer) + '\t' + text
	return answer, fi, fi2












