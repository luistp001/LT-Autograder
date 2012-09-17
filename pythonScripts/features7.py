#LT Autograder. A system that automatically grades short answer essays.
#Copyright (C) 2012 Luis Tandalla


import collections, re
from util import *

def feature7(**kwargs):
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
	index = -1



	line_match = None
	answer = []
	matchs = []

	
	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}\w*is (\w+ )?har?d wo\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*hard work (\w+ ){0,2}\.") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*((rose)|(she)) (\w+ )work (\w+ )?hard\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*((rose)|(she)) (\w+ )?work (\w+ ){0,3}much\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*sens of respons\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*respons person\w*( \w+){0,4}") )	


	pats.append( re.compile(r"(\w+ ){0,4}\w*((rose)|(she)) (\w+ ){0,4}((ha?rd ?wor)|(respon(s|c))|(dedic))\w*( \w+){0,4}") )	
	pats.append( re.compile(r"^((ha?rd ?wor)|(respon(s|c)))\w*( \w+){0,4}") )	
	pats.append( re.compile(r"^(\w+ )*((ha?rd ?wor)|(respon(s|c)))\w* \.") )	
	ans, line_match = fet(text, pats)	
	#if line_match and re.search ( r"(don)|(not)|(\w+nt)|( (s|(no)) )|(much)|(lot)", line_match): ans = '0'
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	

	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}\w*((rose)|(she)) (\w+ ){0,4}((determin)|(persis)|(persev))\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*((ha is)|(her)) ((determin)|(persis)|(persev)|(will power)|(strength of will))\w*( \w+){0,4}") )	
	pats.append( re.compile(r"^((determin)|(persis)|(persev)|(confid)|(will power)|(strength of will))\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*((rose)|(she)) never (\w+ )?give up\w*( \w+){0,4}") )	
	ans, line_match = fet(text, pats)	
	if line_match and re.search ( r"(not)|(\w+nt)", line_match): ans = '0'
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)
	

	ans, index, fi, pats = reset(index, fi)	
	if text.find('.') > 0:check = text[:text.find('.')]
	else: check = text

	pats.append( re.compile(r"(\w+ ){0,4}\w*((rose)|(she)) (\w+ ){1,4}((((( |^)car\w( |$))|(selfless)|(unselfish)|(concern)|(gentl)|(sympa\w*)|(nice)|(kind)|(support)|(thoughtf\w*)|(compassion)|(protect)|(comfort)|(kind)|(conscienc)|(caut\w*)|(compa\w*)|(loyal)|(consol)|(sensit)|(eager)|(love)))|(consider)|(toughtf\w*))\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*((rose)|(she)) is (\w+ )?((sister)|(aunt)|(manna)|(famili))\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*worri (\w+ ){1,2}((sister)|(aunt)|(manna)|(famili))\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*((( |^)car\w( |$))|(selfless)|(unselfish)|(concern)|(gentl)|(sympa\w*)|(nice)|(kind)|(support)|(thoughtf\w*)|(compassion)|(protect)|(comfort)|(kind)|(conscienc)|(caut\w*)|(compa\w*)|(loyal)|(consol)|(sensit)|(eager)|(love)) (\w+ ){0,5}((sister)|(aunt)|(manna)|(famili)|(other))\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*dedic to her ((sister)|(aunt)|(manna)|(famili))\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*((( |^)car\w( |$))|(selfless)|(unselfish)|(concern)|(gentl)|(sympa\w*)|(nice)|(kind)|(support)|(thoughtf\w*)|(compassion)|(protect)|(comfort)|(kind)|(conscienc)|(caut\w*)|(compa\w*)|(loyal)|(consol)|(sensit)|(eager)|(love)) ((trait)|(heart))\w*( \w+){0,4}") )	
	pats.append( re.compile(r"^ ?(\w+ )?((( |^)car\w( |$))|(selfless)|(unselfish)|(concern)|(gentl)|(sympa\w*)|(nice)|(kind)|(support)|(thoughtf\w*)|(compassion)|(protect)|(comfort)|(kind)|(conscienc)|(caut\w*)|(compa\w*)|(loyal)|(consol)|(sensit)|(eager)|(love))\w*( \w+){0,4}") )	
	pats.append( re.compile(r"^ ?(\w+ )?toughtf\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*do anyth for anyon\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*sens of ((sister)|(aunt)|(manna)|(famili))\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*((((sister)|(aunt)|(manna)|(famili)))|(other (peopl )?)) befor her ?self\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*((((sister)|(aunt)|(manna)|(famili)))|(other (peopl )?)) first\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*trait (\w+ )*is her ((( |^)car\w( |$))|(selfless)|(unselfish)|(concern)|(gentl)|(sympa\w*)|(nice)|(kind)|(support)|(thoughtf\w*)|(compassion)|(protect)|(comfort)|(kind)|(conscienc)|(caut\w*)|(compa\w*)|(loyal)|(consol)|(sensit)|(eager)|(love))\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*((( |^)car\w( |$))|(selfless)|(unselfish)|(concern)|(gentl)|(sympa\w*)|(nice)|(kind)|(support)|(thoughtf\w*)|(compassion)|(protect)|(comfort)|(kind)|(conscienc)|(caut\w*)|(compa\w*)|(loyal)|(consol)|(sensit)|(eager)|(love)) ?$") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*((( |^)car\w( |$))|(selfless)|(unselfish)|(concern)|(gentl)|(sympa\w*)|(nice)|(kind)|(support)|(thoughtf\w*)|(compassion)|(protect)|(comfort)|(kind)|(conscienc)|(caut\w*)|(compa\w*)|(loyal)|(consol)|(sensit)|(eager)|(love)) person\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*be((tter)|(st)) for her ((sister)|(aunt)|(manna)|(famili))\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*((n ?t)|(not)) (\w+ ){0,2}((hurt)|(upset))\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*pleas\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*make (\w+ )happi\w*( \w+){0,4}") )

#	pats.append( re.compile(r"((rose)|(she)) is (\w+ )?veri care (person)?") )	
#	pats.append( re.compile(r"((rose)|(she)) (\w+ ){1,4}") )	
#	pats.append( re.compile(r"((rose)|(she)) care (\w+ ){1,3}((her ((sister)|(aunt)|(manna)|(famili)))|(other))") )	
#	pats.append( re.compile(r"((dedic)|(love)|(loyal\w*)) (\w+ )?her famili") )	
#	pats.append( re.compile(r"^(\w+ )?((thought)|(care))") )	
#	pats.append( re.compile(r"c\w* of other peopl feel") )	
#	pats.append( re.compile(r"((care)|(thought\w*)) $") )	
#	pats.append( re.compile(r"love trait") )	

#	pats.append( re.compile(r" ((care)|(thoughtful)|(selfless)) ") )	
#	pats.append( re.compile(r"((rose)|(she)) (\w+ )?compa\w*") )	
#	pats.append( re.compile(r"((rose)|(she)) is veri famili") )	

#	pats.append( re.compile(r"((consol)|(loyal)|(kind))\w* ?$") )
#	pats.append( re.compile(r"for her famili") )




	#pats.append( re.compile(r"((rose)|(she)) (\w+ ){1,3}(veri )?((care )|(compassion)|(kind)|(consider)) ?(\w+ )*") )	
#	pats.append( re.compile(r"((rose)|(she)) (\w+ ){1,4}((thoughtf))\w*") )	
#	pats.append( re.compile(r"((rose)|(she)) (\w+ )?((care)|(look out)|(worri)) (\w+ ){0,3}(her )?((famili)|(sister)|(peopl)|(aunt)|(manna)|(other))") )	
#	pats.append( re.compile(r"^(\w+ )*((love (\w+ ){0,2}famili))") )	
#	pats.append( re.compile(r"(\w+ )*famili person") )		
#	pats.append( re.compile(r"^((care)|(compassion)|(thoughtf\w*))") )	
#	pats.append( re.compile(r"^(\w+ )*((care)|(compassion)|(thoughtf\w*)|(help)) \.") )	
#	pats.append( re.compile(r"(\w+ )*sens of fam\w*( \w+){0,4}") )	
#	pats.append( re.compile(r"(\w+ )*((motherli)|(matern))( \w+)*") )
#	pats.append( re.compile(r"mother figur\w*") )	
#	pats.append( re.compile(r"(\w+ )*((selfless)|(unselfish))") )	
#	pats.append( re.compile(r"^((rose)|(she)) (\w+ ){1,3}((grate)|(loyal)|(support)|(help ))") )			
#	pats.append( re.compile(r"(\w+ )*pleas ((her famili)|(everyon)|(her sister)|(her aunt))") )	
	
#	pats.append( re.compile(r"((rose)|(she)) is understand") )
#	pats.append( re.compile(r"for anyon") )

	ans, line_match = fet(check, pats)	
#	if line_match and re.search ( r" ((ha)|(don)|(not)|(onli)) ", line_match): ans = '0'
#	if line_match and re.search ( r"(onli)|(don)|(not)|(\w+nt)|( (s|(no)) )|(much)|(lot)|(too)|(ha to)|(monei)", line_match): ans = '0'
#	if line_match and re.search ( r"(stress)|(kind of)", line_match): ans = '0'
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)


	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"^(\w+ )*((help)|(give)) person\w*( \w+){0,4}") )	
	pats.append( re.compile(r"^(\w+ )*((rose)|(she)) i?s (\w+ )?(veri )?((help)|(give))\w*( \w+){0,4}") )	
	pats.append( re.compile(r"^(\w+ )*((rose)|(she)) (is )?((tr[iy])|(want)|(work)) (\w+ ){0,2}to help (\w+ ){1,2}((famili)|(sister)|(aunt)|(manna))\w*( \w+){0,4}") )	
	pats.append( re.compile(r"^(\w+ )*help ?(\.|$)") )	
	#pats.append( re.compile(r"^(\w+ )*optim") )	
	#pats.append( re.compile(r"^(\w+ )*posit") )
	ans, line_match = fet(text, pats)	

	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)


	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}\w*((rose)|(she)) (\w+ ){1,3}((hope)|(posit)|(reassur)|(assur)|(optim)|(patien))\w*( \w+){0,4}") )	
	pats.append( re.compile(r"^((hope)|(posit)|(reassur)|(assur)|(optim))\w*( \w+){0,4}") )	
	pats.append( re.compile(r"^(\w+ )*\w*((hope)|(posit)|(reassur)|(assur)|(optim))\w* ?(\.|$)") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*trait (\w+ ){0,3}^((hope)|(posit)|(reassur)|(assur)|(optim))\w*( \w+){0,4}") )
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}\w*respect person\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*((rose)|(she)) is (\w+ )?respect\w*( \w+){0,4}") )	
	pats.append( re.compile(r"^respect\w*( \w+){0,4}") )	
	pats.append( re.compile(r"^(\w+ )*respect ?(\.|$)") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*respect (\w+ )?her\w*( \w+){0,4}") )	
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"^(\w+ )*worri\w* ?(\.|$)") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*worri\w* person\w*( \w+){0,4}") )	
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}\w*((rose)|(she)) is (\w+ ){0,3}sincer\w*( \w+){0,4}") )	
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)	

	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}\w*((rose)|(she)) (\w+ ){0,3}\w*((understand)|(matur))\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*((rose)|(she)) (\w+ ){0,3}((ground)|(grown up))\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*((rose)|(she)) (\w+ ){0,3}stand (\w+ )?her ground\w*( \w+){0,4}") )
	pats.append( re.compile(r"^(\w+ )*((understand)|(matur))(( \.)|($))\w*( \w+){0,4}") )
	pats.append( re.compile(r"^(\w+ )*is (\w+ ){0,2}strong\w*( \w+){0,4}") )
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)	

	#if ans == '0' and label[3] == '1' : print 'FALSE NEGATIVE\t%s\n' % text	
	#if ans == '1' and label[19] == '0': print 'FALSE POSITIVE\t' + text + '\n'	
	#if ans == '1' and label[3] == '0': print 'FALSE POSITIVE\t%s\n%s\n%d\t%d\n' % (text, line_match, score, score2 )
	#if ans == '1' and label[3] == '1': print 'TRUE POSITIVE\t%s\n%s\n%d\t%d\n' % (text, line_match, score, score2 )


	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}\w*((motherli)|(matern))\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*mother figur\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*trait (\w+ )*like (\w+ )mo(m|(ther))\w*( \w+){0,4}") )		
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}\w*(\w+)((nt)|( not)) (\w+ ){0,2}((repli)|(respond)|(answer)|(sai)|(tell)).*hurt ((her)|(aunt))\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*hurt ((her)|(aunt)).* tell\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*the truth\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*not (\w+ ){0,2}tell her aunt\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*if ((rose)|(she)) fe((el)|(lt)) weigh\w? down\w*( \w+){0,4}") )	
	#pats.append( re.compile(r"^(\w+ )*hope") )	
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}\w*lo\w* angl\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*papa\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*better (\w+ )?job\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*get paid more\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*make (more )?monei\w*( \w+){0,4}") )	
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)	

	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}\w*help (\w+ )?(([hp]aul)|(brother)) (\w+ ){1,2}((colleg)|(school))\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*(([hp]aul)|(brother)) (\w+ ){0,3}((colleg)|(school))\w*( \w+){0,4}") )	
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)	

	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}\w*asleep (\w+ )*essai\w*( \w+){0,4}") )	
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)	

	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}\w*((you and me)|(us)|(them)) to go to ((colleg)|(school))\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*and (\w+ ){1,4}go to ((colleg)|(school))\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*the[im]\w? (\w+ )*((colleg)|(school))\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*both (\w+ )*((colleg)|(school))\w*( \w+){0,4}") )	
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)	

	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}\w*fe((el)|(lt)) okai\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*rub her ey\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*ask (\w+ ){0,3}((her sister)|(sister)|(manna)) (\w+ ){0,3}((wrong)|(ok)|(okai)|(on)|(alright)|(feel))\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*if (\w+ ){0,2}((wrong)|(ok)|(okai)|(on)|(alright)|(feel))\w*( \w+){0,4}") )	
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)	

	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}\w*((rose)|(she)) kept nod\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*mayb (\w+ )?life \w+ get \w+er\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*ma\we her feel lighter\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*that her life (\w+ ){0,2}get \w+er\w*( \w+){0,4}") )	
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)	

	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}\w*comfort her\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*comfort manna\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*its onli been four month\w*( \w+){0,4}") )
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)	


	#if ans == '0' and label[16] == '1' : print 'FALSE NEGATIVE\t%s\n' % text	
	#if ans == '1' and label[19] == '0': print 'FALSE POSITIVE\t' + text + '\n'	
	#if ans == '1' and label[19] == '0': print 'FALSE POSITIVE\t%s\n%s\n%d\t%d\n' % (text, line_match, score, score2 )
	#if ans == '1' and label[19] == '1': print 'TRUE POSITIVE\t%s\n%s\n%d\t%d\n' % (text, line_match, score, score2 )




#	if answer2 == 0 and score == 2: print '%s\n' % text


#	if answer2 == 0 and score == 2: print '%d\t%d\t%s\n' % ( answer1, answer2, text)

	return answer, fi, fi2












