#LT Autograder. A system that automatically grades short answer essays.
#Copyright (C) 2012 Luis Tandalla

import collections, re
from util import *

def feature3(**kwargs):
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



	oldl = [' in china', ' in austria', ' from china', ' chines', ' austrian', 'china s ']
	new = ''
	for old in oldl:
		text = text.replace(old, new)				
	old = 'panda bear'
	new = 'panda'
	text = text.replace(old, new)			
	old = 'koala bear'
	new = 'koala'
	text = text.replace(old, new)		

	index = 0
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}\w*harmless\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*not danger\w*( \w+){0,4}") )	
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}\w*bamboo\w*( \w+){0,4}") )	
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}\w*(\w+ ){0,5}eucalyptu\w*( \w+){0,4}") )			
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []		
	pats.append( re.compile(r"(\w+ ){0,4}\w*((no\w* like)|(differ)|(howev)) (\w+ ){0,3}((python)|(snake)|(cobra))\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*((unlik)|(wherea)|(oppos)) (\w+ ){0,2}((python)|(snake)|(cobra))\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*((python)|(snake)|(cobra)) (\w+ ){0,2}((differ)|(howev))\w*( \w+){0,4}") )		
	pats.append( re.compile(r"(\w+ ){0,4}\w*((python)|(snake)|(cobra)) (\w+ ){0,2}on the other\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*on the other hand (\w+ ){0,2}((python)|(snake)|(cobra))\w*( \w+){0,4}") )
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	#pats.append( re.compile(r"(\w+ ){0,4}\w*^black\w*( \w+){0,4}") )			
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}\w*allig\w*( \w+){0,4}") )			
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}\w*koala (\w+ ){0,7}panda (\w+ ){0,6}((similar)|(alik))\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*panda (\w+ ){0,7}koala (\w+ ){0,6}((similar)|(alik))\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*koala (\w+ ){0,5}((similar)|(alik)) (\w+ ){0,4}panda\w*( \w+){0,4}") )
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}\w*specialist\w*( \w+){0,4}") )			
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)


	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
#	pats.append( re.compile(r"(\w+ ){0,4}\w*eat (\w+ )*on\w*( \w+){0,4}") )					
#	pats.append( re.compile(r"(\w+ ){0,4}\w*eat (\w+ )*same\w*( \w+){0,4}") )
#	pats.append( re.compile(r"(\w+ ){0,4}\w*spec\w* (\w+ )*food\w*( \w+){0,4}") )			
#	pats.append( re.compile(r"(\w+ ){0,4}\w*on (\w+ )*food\w*( \w+){0,4}") )			
#	pats.append( re.compile(r"(\w+ ){0,4}\w*on (\w+ )*thing\w*( \w+){0,4}") )			
	

	pats.append( re.compile(r"(\w+ ){0,4}\w*eat (\w+ )?(exclus )?on \w+\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*eat (\w+ )*onli on \w+\w*( \w+){0,4}") )			
	pats.append( re.compile(r"(\w+ ){0,4}\w*eat (\w+ )*noth but on \w+\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*eat (\w+ )*specif\w*( \w+){0,4}") )		
	pats.append( re.compile(r"(\w+ ){0,4}\w*((certain)|(specif\w*)) (\w+ ){0,2}((food)|(type)|(plant)|(thing)|(diet))\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*(\w+ ){0,5}((limit)|(strict)|(uni\w*)|(exclus)|(regular)|(particular)|(special)|(select))\w* diet\w*( \w+){0,4}") )		
	pats.append( re.compile(r"(\w+ ){0,4}\w*(\w+ ){0,5}((on)|(a)|(singl)|(limit)|(exclus)|(primari)) (type of )?food sourc\w*( \w+){0,4}") )		
	pats.append( re.compile(r"(\w+ ){0,4}\w*(\w+ ){0,5}((on)|(a)|(singl)|(limit)|(exclus)|(primari)) (type of )?sourc of food\w*( \w+){0,4}") )		
		

	pats.append( re.compile(r"(\w+ ){0,4}\w*eat (\w+ ){0,2}same( \w+){0,2}\w*( \w+){0,4}") )

	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)
	
	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}\w*generalist\w*( \w+){0,4}") )			
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)
	
	
	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
#	pats.append( re.compile(r"(\w+ ){0,4}\w*adapt\w*( \w+){0,4}") )			
#	pats.append( re.compile(r"(\w+ ){0,4}\w*locat\w*( \w+){0,4}") )		
#	pats.append( re.compile(r"(\w+ ){0,4}\w*place\w*( \w+){0,4}") )				
#	pats.append( re.compile(r"(\w+ ){0,4}\w*differ\w*( \w+){0,4}") )
#	pats.append( re.compile(r"(\w+ ){0,4}\w*live\w*( \w+){0,4}") )
#	pats.append( re.compile(r"(\w+ ){0,4}\w*ani\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*((live)|(surviv)|(ad[oa]pt)) (\w+ ){0,2}anyw\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*((live)|(surviv)|(ad[ao]pt)) (\w+ ){0,2}((mani)|(differ))\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*((live)|(surviv)|(ad[ao]pt)) (\w+ ){0,3}((ani)|(var\w*))\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*((live)|(surviv)|(ad[oa]pt)) (\w+ ){0,3}((more)|(numer)|(multipl)|(lot of)|(rang of))\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*ad[oa]pt (\w+ )?eas\w*( \w+){0,4}") )		
	pats.append( re.compile(r"(\w+ ){0,4}\w*ad[ao]pt (\w+ )*((new)|(rapid)|(chang)|(fast))\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*ad[oa]pt (\w+ ){0,3}((environ)|(place)|(surround)|(climat)|(locat))\w*( \w+){0,4}") )

	pats.append( re.compile(r"(\w+ ){0,4}\w*(\w+ ){0,3}multipl locat( \w+){0,3}\w*( \w+){0,4}") )		
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	
	pats.append( re.compile(r"(\w+ ){0,4}\w*eat (\w+ ){0,3}((mani)|(var\w*)|(differ)|(anyt\w*)|(multipl)|(everyt\w*)|(everi th\w*)|(ani ))( \w+){0,3}\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*ad[oa]pt (\w+ ){0,3}((food)|(eat))\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*diet chang\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*easier to feed\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w* no specif\w* (\w+ ){0,2}((food)|(type)|(plant)|(thing)|(diet))\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*eat what ?e\w*( \w+){0,4}") )	

#	pats.append( re.compile(r"(\w+ ){0,4}\w*eat\w*( \w+){0,4}") )			
#	pats.append( re.compile(r"(\w+ ){0,4}\w*food\w*( \w+){0,4}") )			
#	pats.append( re.compile(r"(\w+ ){0,4}\w*diet\w*( \w+){0,4}") )			
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []	
	pats.append( re.compile(r"(\w+ ){0,4}\w*((exclus( \w+)?)|(strict)|(certain)|(specif)|(given)|(special)) (\w+ ){0,2}((area)|(environ)|(place)|(locat)|(condit)|(region)|(climat)|(habitat)|(part of the ((world)|(earth)))|(ecosystem))( \w+){0,3}\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*((live)|(stai)|(remain)|(adapt)|(surviv)|(suit)|(requir)|(familiar)|(stick)) (\w+ ){0,2}((on)|(same)|(there)|(their)) (\w+ ){0,2}((area)|(environ)|(place)|(locat)|(condit)|(region)|(climat)|(habitat)|(part of the ((world)|(earth)))|(ecosystem)|(lifestyle))\w*( \w+){0,4}") )		
	pats.append( re.compile(r"(\w+ ){0,4}\w*((depend)|(reli)) (\w+ ){0,2}their ((area)|(environ)|(place)|(locat)|(condit)|(region)|(climat)|(habitat)|(part of the ((world)|(earth)))|(ecosystem))\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*(\w+ ){0,3}nativ (\w+ ){0,2}((area)|(environ)|(place)|(locat)|(condit)|(region)|(climat)|(habitat)|(part of the ((world)|(earth)))|(ecosystem))\w*( \w+){0,4}") )		
	pats.append( re.compile(r"(\w+ ){0,4}\w*limit (\w+ ){0,3}((area)|(environ)|(place)|(locat)|(condit)|(region)|(climat)|(habitat)|(part of the ((world)|(earth)))|(ecosystem)|(to live))\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*(\w+ ){0,3}natur habitat\w*( \w+){0,4}") )	

	pats.append( re.compile(r"(\w+ ){0,4}\w*live (\w+ )?(exclus (\w+ )?)?on \w+( \w+)?\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*live (\w+ ){0,2}onli on \w+\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*live (\w+ ){0,3}specif\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*surviv in on\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*live onli\w*( \w+){0,4}") )	

	pats.append( re.compile(r"(\w+ ){0,4}\w*c((an?)|(ould))( \w+)? onli( \w+)? ((live)|(surviv))( \w+){0,2}\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*c((an?)|(ould))( \w+)? ((live)|(surviv))( \w+)? onli( \w+){0,2}\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*onli( \w+)? c((an?)|(ould))( \w+)? ((live)|(surviv))( \w+){0,2}\w*( \w+){0,4}") )

	ans, line_match = fet(text, pats)
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)





	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}\w*(([iu]nabl)|(troubl)|(tough)) (\w+ )?ad(([oa]pt)|(just))\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*no?t (\w+ )?(be abl to )?ad(([oa]pt)|(just))\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*wo(uld)?((nt)|( not)) (be abl to )?surviv\w*( \w+){0,4}") )	

	pats.append( re.compile(r"(\w+ ){0,4}\w*no?t ((live)|(surviv)|(ad[oa]pt)) (\w+ ){0,2}anyw\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*no?t ((live)|(surviv)|(ad[ao]pt)) (\w+ ){0,2}((mani)|(differ))\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*no?t ((live)|(surviv)|(ad[ao]pt)) (\w+ ){0,3}((ani)|(var\w*))\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*no?t ((live)|(surviv)|(ad[oa]pt)) (\w+ ){0,3}((more)|(numer)|(multipl)|(lot of)|(rang of))\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*no?t ad[oa]pt (\w+ )?eas\w*( \w+){0,4}") )		
	pats.append( re.compile(r"(\w+ ){0,4}\w*no?t ad[ao]pt (\w+ )*((new)|(rapid)|(chang)|(fast))\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*no?t ad[oa]pt (\w+ ){0,3}((environ)|(place)|(surround)|(climat)|(locat))\w*( \w+){0,4}") )

	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)


	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}\w*generalist( \w+)* ((is)|(favor)|(like)) (\w+ )?chang\w*( \w+){0,4}") )		
	pats.append( re.compile(r"(\w+ ){0,4}\w*chang (\w+ )*((favor)|(like)) (\w+ )*generalist\w*( \w+){0,4}") )	
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)


	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
####pats.append( re.compile(r"(\w+ ){0,4}\w*(\w+ ){0,5}invas\w*( \w+){0,4}") )			
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)


	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)


	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}\w*(\w+ ){0,5}herb\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*veg\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*eat ((plant)|(natur))\w*( \w+){0,4}") )		
	pats.append( re.compile(r"(\w+ ){0,4}\w*no?t eat (\w+ )?((meat)|(anim))\w*( \w+){0,4}") )
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	
	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}\w*((eat)|(rate)|(devour)|(consum)|(prei)|(feed)) (\w+ ){0,2}((other)|(of)) (\w+ )?((anim)|(meat)|(live [to]\w+)|(reptil)|(mice)|(insect)|(rat)|(rodent))\w*( \w+){0,4}") )		
	pats.append( re.compile(r"(\w+ ){0,4}\w*((eat)|(rate)|(devour)|(consum)|(prei)|(feed)) (\w+ ){0,3}((anim)|(meat)|(live [to]\w+)|(reptil)|(mice)|(insect)|(rat)|(rodent))\w*( \w+){0,4}") )		
	pats.append( re.compile(r"(\w+ ){0,4}\w*((eat)|(rate)|(devour)|(consum)|(prei)|(feed)) (\w+ ){0,1}((other))\w*( \w+){0,4}") )		
	pats.append( re.compile(r"(\w+ ){0,4}\w*carn\w*( \w+){0,4}") )		
	pats.append( re.compile(r"(\w+ ){0,4}\w*meat eater\w*( \w+){0,4}") )		
#	pats.append( re.compile(r"(\w+ ){0,4}\w*meat\w*( \w+){0,4}") )			
#	pats.append( re.compile(r"(\w+ ){0,4}\w*anim\w*( \w+){0,4}") )			
#	pats.append( re.compile(r"(\w+ ){0,4}\w*liv\w*( \w+){0,4}") )			
#	pats.append( re.compile(r"(\w+ ){0,4}\w*eat\w*( \w+){0,4}") )			
#	pats.append( re.compile(r"(\w+ ){0,4}\w*snack\w*( \w+){0,4}") )			
	ans, line_match = fet(text, pats)	
	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)





	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}\w*specialist( \w+){0,5} stabi\w*( \w+){0,4}") )			
	pats.append( re.compile(r"(\w+ ){0,4}\w*stabi\w*( \w+){0,5} specialist\w*( \w+){0,4}") )				
	pats.append( re.compile(r"(\w+ ){0,4}\w*stabi\w*( \w+){0,4}") )				
	pats.append( re.compile(r"(\w+ ){0,4}\w*stabl\w*( \w+){0,4}") )				
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}\w*everglad\w*( \w+){0,4}") )			
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}\w*florida\w*( \w+){0,4}") )			
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}\w*((right)|(warm)|(similar)|(suit)|(agree))\w* (\w+ )?((climat)|(environ)|(temperatur))\w*( \w+){0,4}") )						
	pats.append( re.compile(r"(\w+ ){0,4}\w*((climat)|(environ)|(temperatur)) (\w+ )?((right)|(warm)|(similar)|(suit)|(agree))\w*( \w+){0,4}") )						
	pats.append( re.compile(r"(\w+ ){0,4}\w*climat (\w+ )?right\w*( \w+){0,4}") )				
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
#	pats.append( re.compile(r"(\w+ ){0,4}\w*unit state\w*( \w+){0,4}") )						
#	pats.append( re.compile(r"(\w+ ){0,4}\w*((southern)|(the)) us((( \w+){1,5})|($)|( \.))\w*( \w+){0,4}") )								
#	pats.append( re.compile(r"(\w+ ){0,4}\w*u \. s\w*( \w+){0,4}") )											
#	pats.append( re.compile(r"(\w+ ){0,4}\w*usa\w*( \w+){0,4}") )		
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}\w*ha[rn]d\w* ((time)|(for the\w*))\w*( \w+){0,4}") )			
	pats.append( re.compile(r"(\w+ ){0,4}\w*die((( \w+){1,5})|($)|( \.))\w*( \w+){0,4}") )			
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}\w*((due)|(becaus)) (\w+ ){0,3}diet\w*( \w+){0,4}") )			# because f the diet	
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}\w*((area)|(place)) (\w+ )*((support)|(get)|(have)) (\w+ )*food\w*( \w+){0,4}") )			#area that support that food		

	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []

	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)


	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}\w*panda (\w+ ){0,5}((similar)|(alik)) (\w+ ){0,4}koala\w*( \w+){0,4}") ) #-0.035
	pats.append( re.compile(r"(\w+ ){0,4}\w*((similar)|(alik)) (\w+ ){0,4}panda (\w+ ){0,9}koala\w*( \w+){0,4}") ) #-0.0007
	pats.append( re.compile(r"(\w+ ){0,4}\w*((similar)|(alik)) (\w+ ){0,4}koala (\w+ ){0,9}panda\w*( \w+){0,4}") ) #-0.001
	pats.append( re.compile(r"(\w+ ){0,4}\w*thei (\w{1,3} )(\w+ )?((similar)|(alik))\w*( \w+){0,4}") ) #-0.0033
	pats.append( re.compile(r"(\w+ ){0,4}\w*two (\w+ )ar ((similar)|(alik))\w*( \w+){0,4}") )	#-0.0006
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}\w*koala (\w+ ){0,7}panda (\w+ ){0,6}ar the same\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*panda (\w+ ){0,7}koala (\w+ ){0,6}ar the same\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*koala (\w+ ){0,5}ar the same (\w+ ){0,4}panda\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*panda (\w+ ){0,5}ar the same (\w+ ){0,4}koala\w*( \w+){0,4}") ) #-0.035
	pats.append( re.compile(r"(\w+ ){0,4}\w*ar the same (\w+ ){0,4}panda (\w+ ){0,9}koala\w*( \w+){0,4}") ) #-0.0007
	pats.append( re.compile(r"(\w+ ){0,4}\w*ar the same (\w+ ){0,4}koala (\w+ ){0,9}panda\w*( \w+){0,4}") ) #-0.001
	pats.append( re.compile(r"(\w+ ){0,4}\w*thei (\w{1,3} )(\w+ )?ar the same\w*( \w+){0,4}") ) #-0.0033
	pats.append( re.compile(r"(\w+ ){0,4}\w*two (\w+ )ar the same\w*( \w+){0,4}") )	#-0.0006
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)



	return answer, fi, fi2	

