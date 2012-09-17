#LT Autograder. A system that automatically grades short answer essays.
#Copyright (C) 2012 Luis Tandalla

import collections, re
from util import *

def feature10(**kwargs):
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
	text = text.replace( 'temp .', 'temp')
	text = text.replace( ' th ', ' the ')
	index = -1

	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"^black\w*( \w+){0,4}") )			
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}\w*((keep)|(make)) (\w+ )*((warm)|(hot))\w*( \w+){0,4}") )				
	pats.append( re.compile(r"(\w+ ){0,4}\w*absorb more heat\w*( \w+){0,4}") )			
	pats.append( re.compile(r"(\w+ ){0,4}\w*((insid)|(dog)) will be warm\w*( \w+){0,4}") )			
	pats.append( re.compile(r"(\w+ ){0,4}\w*incre\w* (\w+ ){0,3}temp\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*get (\w+ ){0,2}h((ea)|(o))t\w*( \w+){0,4}") )			
	pats.append( re.compile(r"(\w+ ){0,4}\w*more heat\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*stai (\w+ )?warm\w*( \w+){0,4}") )			
	pats.append( re.compile(r"(\w+ ){0,4}\w*temp\w* (\w+ )*high\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*((would)|(will))\w* be (\w+ )?((hot)|(warm))\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*warm\w*( \w+){0,4}") )
	
	pats.append( re.compile(r"(\w+ ){0,4}\w*heat it up\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*absorb heat more\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*absorb more energi\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*absorb the most heat\w*( \w+){0,4}") )			
	pats.append( re.compile(r"(\w+ ){0,4}\w*attract all the heat\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*high\w* temp\w*( \w+){0,4}") )		
	pats.append( re.compile(r"(\w+ ){0,4}\w*temp\w* (\w+ ){0,3}((incr)|(rise))\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*it hot\w*( \w+){0,4}") )		
	
	ans, line_match = fet(text, pats)					
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}\w*experi\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*highest\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*hottest\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*warmest\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*jar\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*lid\w*( \w+){0,4}") )
	ans, line_match = fet(text, pats)					
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"^dark\w*( \w+){0,4}") )			
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}\w*will absorb heat\w*( \w+){0,4}") )			
	pats.append( re.compile(r"(\w+ ){0,4}\w*attract heat\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*take in heat\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*collect on heat\w*( \w+){0,4}") )	
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}\w*\w+ second h\w+\w*( \w+){0,4}") )
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"^light\w*( \w+){0,4}") )			
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)


	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}\w*no?t (\w+ ){1,2}hot\w*( \w+){0,4}") )			
	pats.append( re.compile(r"(\w+ ){0,4}\w*no?t overh\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*no?t absorb (\w+ ){0,3}heat\w*( \w+){0,4}") )
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}\w*\w+ second c\w+\w*( \w+){0,4}") )
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"^white\w*( \w+){0,4}") )			
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}\w*stai (\w+ ){0,2}cool\w*( \w+){0,4}") )		
	pats.append( re.compile(r"(\w+ ){0,4}\w*((keep)|(make)) (\w+ )*((co((ol)|(ld)))|(low))(er)?\w*( \w+){0,4}") )				
	pats.append( re.compile(r"(\w+ ){0,4}\w*(\w+ )*((absorb)|(attract)) less heat\w*( \w+){0,4}") )			
	pats.append( re.compile(r"(\w+ ){0,4}\w*(\w+ )*((absorb)|(attract)) heat less\w*( \w+){0,4}") )			
	pats.append( re.compile(r"(\w+ ){0,4}\w*no?t be as ((hot)|(warm))\w*( \w+){0,4}") )			
	pats.append( re.compile(r"(\w+ ){0,4}\w*less hot\w*( \w+){0,4}") )			
	pats.append( re.compile(r"(\w+ ){0,4}\w*no?t ((absorb)|(attract)) (\w+ ){0,2}heat\w*( \w+){0,4}") )			
	pats.append( re.compile(r"(\w+ ){0,4}\w*temp\w* (\w+ )*low\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*((would)|(will))\w* be (\w+ )?co((ol)|(ld))\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*no?t get (\w+ ){0,2}hot\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*to be co((ol)|(ld))\w*( \w+){0,4}") )
	pats.append( re.compile(r"(\w+ ){0,4}\w*no?t overh\w*( \w+){0,4}") )		
	pats.append( re.compile(r"(\w+ ){0,4}\w*cool\w* (\w+ ){0,3}\w*hous\w*( \w+){0,4}") )			
	pats.append( re.compile(r"(\w+ ){0,4}\w*cool down\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*least amount of heat\w*( \w+){0,4}") )			
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	ans, index, fi, pats = reset(index, fi)
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)


	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}\w*lowest (air )?te\w+\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*white (lid )?(jar )?((is)|(wa)|(had)) the co((ol)|(ld))es\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*least hot( \w+){0,5}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*least (\w+ )?tem\w+\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*4 ?2 (\w+ )*co((ol)|(ld))es\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*co((ol)|(ld))er th[ea]n the other\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*((kept)|(remain)|(stai)) (\w+ )*co((ol)|(ld))est\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*coolest te\w+( \w+)* 10\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*lowest\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*co((ol)|(ld))est\w*( \w+){0,4}") )	
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}\w*5 ?[023485]\w*( \w+){0,4}") )			
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}\w*4 ?[123]\w*( \w+){0,4}") )			
	pats.append( re.compile(r"(\w+ ){0,4}\w*((around)|(low)|(up to)) 40\w*( \w+){0,4}") )
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}\w*4 ?[789]( \w+){0,4}") )			
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}\w*4 ?[456]( \w+){0,4}") )			
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}\w*((1 ?[012] )|( 9 ))((deg)|(cal)|(c ))\w*( \w+){0,4}") )			
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)



	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}\w*2 ?9\w*( \w+){0,4}") )			
	pats.append( re.compile(r"(\w+ ){0,4}\w*3 ?0\w*( \w+){0,4}") )			
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}\w*1 ?8\w*( \w+){0,4}") )			
		
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}\w*2 ?[01]\w*( \w+){0,4}") )		
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)


	


	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}\w*midd\w*( \w+){0,4}") )		
	pats.append( re.compile(r"(\w+ ){0,4}\w*med\w*( \w+){0,4}") )	
	pats.append( re.compile(r"(\w+ ){0,4}\w*comfort ((te)|(fo))\w+\w*( \w+){0,4}") )

	#	pats.append( re.compile(r"right am\w*") )		
	#	pats.append( re.compile(r"\w+ just r\w+") )					
	#	pats.append( re.compile(r"good t\w*") )		

	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	ans, index, fi, pats = reset(index, fi)
	pats.append( re.compile(r"(\w+ ){0,4}\w*the (more )?((dark)|(light))\w* the\w*( \w+){0,4}") )			
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)



		




	return answer, fi, fi2


