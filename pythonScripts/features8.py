#LT Autograder. A system that automatically grades short answer essays.
#Copyright (C) 2012 Luis Tandalla


import collections, re
from util import *


def feature8(**kwargs):
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
	pats.append( re.compile(r"(\w+ ){0,4}\w*((remind)|(both)|(too)|(also)|(same)|(like)|(common)|(onli)|(neither of them)|(self experi)) (\w+ )*((read)|(school))\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*((both)|(to)|(also)|(same)) ha\w* (\w+ )*read\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*(\w+ )wai (\w+ )*(\. (\w+ )*)?read\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*becaus he cant read\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*thei can not read veri well\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*felt (\w+ )*read\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*[pg]\w+ reader (\w+ )*((also)|(like)|(n?either)|(such as)|(too)|(just as)|(that is)|(as well)|(same))\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*read (\w+ ){0,2}((too)|(like)|(same)|(also)|(either)|(just ((as)|(like))))\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*read (\w+ )*becaus (\w+ )*((also)|(like)|(n?either)|(such as)|(too)|(just as)|(that is)|(as well)|(same))\w*( \w+){0,4}") )	
	
	ans, line_match = fet(text, pats)	
	if line_match and line_match.find('the read') >= 0: ans = '0'
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}\w*((he)|(paul)) ((wa)|(is)) (\w+ ){0,2}((motiv)|(inspir)|(encourag)) (\w+ ){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}((wa)|(is)) (\w+ ){0,2}((motiv)|(inspir)|(encourag)) (\w+ ){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*it (\w+ ){0,4}((motiv)|(inspir)|(encourag)) (\w+ )*") )
	pats.append( re.compile(r"(\w+ ){0,4}((motiv)|(inspir)|(encourag)) (\w+ ){0,4}paul (\w+ ){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}((felt)|(bec\wm)) ((motiv)|(inspir)|(encourag)) (\w+ ){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}((work)|(train)|(tr[yin]\w?)) ha[rn]d\w* (\w+ ){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}to ((do)|(be)) better (\w+ ){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}confid (\w+ ){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}((set)|(put)) hi mind (\w+ ){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}c[oa]\w* (\w+ )?over ?come? (\w+ ){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}role model (\w+ ){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}g\wve (\w+ )?hope (\w+ ){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}be ?come? (a )?better (\w+ ){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}get better (\w+ ){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}ca\w* (\w+ )?succe (\w+ ){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}((potenti)|(academ)|(educ)|(determin)|(succe)|(goal)|(accomplish)|(to do ((good)|(well)))) (\w+ ){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}push ((paul)|(himself)|((\w+ )?ha[rn]d\w*)) (\w+ ){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}he could do\w* (\w+ ){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}((get good)|(up( \w+){0,2})) grade (\w+ ){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}school (\w+ )import(\w+ ){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}he c[ao]\w* (\w+ )?be (\w+ )?good (\w+ ){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}do the best (\w+ ){0,4}") )
	ans, line_match = fet(text, pats)	
	
#	if line_match and line_match.find('the read') >= 0: ans = '0'
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}((sympath)|(emphat)|(empat))\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}((alon)|(common)|(connect)|(closer)|(alik)|(relat)|(similar)|(bond)) (\w+ ){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}remind (\w+ )*him\w* (\w+ ){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}same ((condit)|(situat\w*)) (\w+ ){0,4}") )		
	pats.append( re.compile(r"(\w+ ){0,4}kn[oe]w (\w+ )*feel (\w+ ){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}feel better about himself (\w+ ){0,4}") )

	ans, line_match = fet(text, pats)	

	#pats.append( re.compile(r"(\w+ )*sorri (\w+ )*") )		
	#	pats.append( re.compile(r"(\w+ )*differ (\w+ )*") )
	#	pats.append( re.compile(r"(\w+ )*a lot by him (\w+ )*") )
	#pats.append( re.compile(r"(\w+ )*feel (\w+ )*") )
	#	pats.append( re.compile(r"(\w+ )*werent so differ (\w+ )*") )
	#	pats.append( re.compile(r"(\w+ )*felt (\w+ )*") )
	#	pats.append( re.compile(r"(\w+ )*feel (\w+ )*") )
	#	pats.append( re.compile(r"(\w+ )*same (\w+ )*") )
	#	pats.append( re.compile(r"(\w+ )*like (\w+ )*") )
	#	pats.append( re.compile(r"(\w+ )*understand (\w+ )*") )
	#	pats.append( re.compile(r"(\w+ )*effect (\w+ )*") )
	#	pats.append( re.compile(r"(\w+ )*himself (\w+ )*") )
	
	#	if line_match and line_match.find('the read') >= 0: ans = '0'
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)
	
	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}su\w{0,2}ris\w* (\w+ ){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}((shock)|(astonish)|(puzz)|(overw)|(astound)|(stun)|(intrig))\w* (\w+ ){0,4}") )		
	pats.append( re.compile(r"(\w+ ){0,4}((paul)|(he)) (\w+ ){0,3}((amaz)|(impress))\w* (\w+ ){0,4}") )		
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}why didnt you tell me about thi ?(\w+ ){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}why mr leonard did not tell him( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}mr leonard never told( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}why mr leonard (\w+ ){0,3}t\wl\w( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}why (\w+ )*secret (\w+ ){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}why ((mr leonard)|(he)|(the coach)) (\w+ ){1,3}((mention)|(tell)|(told)|(sai)|(share)|(inform))( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}why ((mr leonard)|(he)|(the coach)) (\w+ ){0,3}((kept)|(hid\w*)|(quiet))( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}why \w*((nt)|(not)) ((mr leonard)|(he)|(the coach)) (\w+ ){0,3}((mention)|(tell)|(told)|(sai)|(inform)|(share)|(kept)|(hid\w*))( \w+){0,4}") )
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}((help)|(teach)|(assist)|(coach)|(train)|(taught)|(tutor)) (\w+ )?(((mr )?leonard)|(him?)|(hi teacher)) (\w+ )*read\w* ?(\w+ ){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}((show)) (((mr )?leonard)|(him?)|(hi teacher)) (\w+ ){0,2}read\w* ?(\w+ ){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}help (\w+ )?(((mr )?leonard)|(him)) (\w+ )*help (\w+ )?((him)|(paul)) ?(\w+ ){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}return \w+ favor ?(\w+ ){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}((invit)|(took)|(take)) ((him)|((mr )?leonard)) (\w+ )*center ?(\w+ ){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}tutor ((him)|((mr )?leonard)) ?(\w+ ){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}motiv (\w+ )?to help ?(\w+ ){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}help mr leonard ?(\w+ ){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}repai ?(\w+ ){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}pai (\w+ ){0,3}back ?(\w+ ){0,4}") )
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)
	
	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}its? (\w+ )?time (\w+ ){0,3}((start)|(begin)) (\w+ )?train ?(\w+ ){0,4}") )
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}rea\w (\w+ )?\w*loud ?(\w+ ){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}call (up)?on to rea\w ?(\w+ ){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}in front ?(\w+ ){0,4}") )
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}curio\w* ?(\w+ ){0,4}") )		
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)


	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'	
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}((star)|(champion)|(nation)|(famou))\w*( |$)(\w+ ){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}won the meter( |$)(\w+ ){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*((great)|(compet)|(coll\wg)|(track)|(amaz)|(fantast)|(talent)|(famou)|(renown)|(except)|(excel)|(awes))\w* athlet\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*((great)|(compet)|(coll\wg)|(amaz)|(except)|(fantast)|(talent)|(famou)|(renown)|(excel)|(awes))\w* hurdler\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*((great)|(compet)|(coll\wg)|(amaz)|(except)|(fantast)|(talent)|(famou)|(renown)|(excel)|(awes)|(good)|(former))\w* (\w+ )?runner\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}record\w*( \w+){0,4}") )		
	pats.append( re.compile(r"(\w+ ){0,4}((track)|(field)) scholarship ?(\w+ ){0,4}") )			
	ans, line_match = fet(text, pats)					
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'	
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}all too? familiar( \w+){0,4}") )
	ans, line_match = fet(text, pats)					
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'	
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}realiz why ?(\w+ ){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}realiz (\w+ ){0,4}help\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}realiz what mr ?(\w+ ){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}under ?st\w* (\w+ )?((why)|(mr)|(leonard)) ?(\w+ ){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}intent ?(\w+ ){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}show (\w+ )?why ?(\w+ ){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}that is why ?(\w+ ){0,4}") )	
	ans, line_match = fet(text, pats)					
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'	
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}((thank)|(grate)|(honor)|(respect)|(bless)|(touch)|(privileg)) ?(\w+ ){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}time (\w+ )?to help \w+ excel ?(\w+ ){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*do\w* (\w+ ){0,3}for him( \w+){0,4}") )
	ans, line_match = fet(text, pats)					
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'	
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}confus( \w+){0,4}") )
	ans, line_match = fet(text, pats)					
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	pats = []
	if not line_match:		
		pass
#	ans, line_match = fet(text, pats)					
#	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	#if ans == '0' and label[index] == '1' : print 'FALSE NEGATIVE\t%s\n' % text	
#	if ans == '1' and label[index] == '0': print 'FALSE POSITIVE\t' + text + '\n'	
#	if ans == '1' and label[index] == '0' and score == 0 and score2 == 0: print 'FALSE POSITIVE\t%s\n%s\n%d\t%d\n' % (text, line_match, score, score2 )
	#if ans == '1' and label[index] == '0' and score == 0 and score2 == 0: print 'FALSE POSITIVE\t%s' % ( line_match )
#	if ans == '1' and label[index] == '1': print 'TRUE POSITIVE\t%s\n%s\n%d\t%d\n' % (text, line_match, score, score2 )
	#if ans == '1' and label[index] == '1': print 'TRUE POSITIVE\t%s' % (line_match )

	#answer = [ int( sum( answer ) > 0 ) ]

	return answer, fi, fi2


