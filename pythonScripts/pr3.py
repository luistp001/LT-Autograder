#LT Autograder. A system that automatically grades short answer essays.
#Copyright (C) 2012 Luis Tandalla

# This cripts makes some preprocessing steps. Some of the calculations and files produced
# by it are not used in the final model. They are included because they were used in the
# development phase

import collections, re, math
from analyze_essay import *

from features import *
from util import *

import sys

def process3( SET, TEST, nameFileTraining, nameFileTest = None ):
 #It makes some processing steps.
 fi = [] # List of vectors of words for each answer,		NOT USED IN FINAL MODEL
 fi2 = collections.defaultdict(lambda: []) # It contains vectors of words for each match of each answer,		NOT USED IN FINAL MODEL

 fi_test = [] 
 fi2_test = collections.defaultdict(lambda: [])

 reader = open(nameFileTraining, 'r' )
 if TEST: reader_test = open(nameFileTest, 'r' )


 inv_index = {}		#Inverted index of words in the essays,		NOT USED IN FINAL MODEL
 inv_index_u = {}	#Inverted index of words in the essays,		NOT USED IN FINAL MODEL
 inv_index_b = {}	#Inverted index of bigrams in the essays,	NOT USED IN FINAL MODEL
 inv_index_t = {}	#Inverted index of trigrams in the essays,	NOT USED IN FINAL MODEL

 data = collections.OrderedDict() # It contains information of the essays.
 docs = {}		# It contains the essays as vectors of words
 docs2 = {}		# It contains the essays as vectors of bigrams

 docs_u = {}	# It contains the essays as vectors of words
 docs_b = {}	# It contains the essays as vectors of bigrams
 docs_t = {}	# It contains the essays as vectors of trigrams

 inv_index_test = {}
 inv_index_u_test = {}
 inv_index_b_test = {}
 inv_index_t_test = {}

 data_test = collections.OrderedDict()
 docs_test = {}
 docs2_test = {}

 docs_u_test = {}
 docs_b_test = {}
 docs_t_test = {}

 vocab1 = collections.defaultdict(lambda: 0.0)		# words that appeared in the essays
 vocab2 = collections.defaultdict(lambda: 0.0)		# bigrams that appeared in the essays
 vocab3 = collections.defaultdict(lambda: 0.0)		# trigrams that appeared in the essays

 vocab1_test = collections.defaultdict(lambda: 0.0)
 vocab2_test = collections.defaultdict(lambda: 0.0)
 vocab3_test = collections.defaultdict(lambda: 0.0)


 numFeat = 0

 # Creating bag of words, bigrams, and trigrams

 for row in reader:

	line = row.split('\t')
	if line[0] == 'Id':				continue
	Id = int(line[0])	
	essay = { }		# It will contain the information of an essay
	essay['set'] = int(line[1])
	if not essay['set'] == SET:		continue
	essay['s1'] = int(line[2])
	essay['s2'] = int(line[3])	
	essay['text'] = cleantext(line[4], SET)
	# The following two lines makes some calculations to the text of the essays.	
	docs, docs2, docs_u, docs_b, docs_t, vocab1, vocab2, vocab3, inv_index, inv_index_u, inv_index_b, inv_index_t = a_essay ( Id, essay['text'], docs, docs2, docs_u, docs_b, docs_t, vocab1, vocab2, vocab3, inv_index, inv_index_u, inv_index_b, inv_index_t) 			
	
	#fs is a list with ones of zeroes depending if an essay has certain answer or not
	# fi and fi2 are updated.
	fs, fi, fi2 = feature(text = essay['text'], fi = fi, set = SET, Id = Id, score = essay['s1'], score2 =essay['s2'], fi2 =fi2 )	

	# New features are calculated from fs, and fs is updated. f is a raw score predicted 
	# for the essay using the values of fs. f is NOT USED IN FINAL MODEL
	f, fs = calculate_f(fs, SET)
	
	text = essay['text']
	essay['f'] = f	
	essay['fs'] = fs
	essay['n_words'] = len(text.split() )
	essay['n_sentences'] = len( text.split( '.' ) )
	essay['sentence_ave_size'] = essay['n_words'] * 1./ essay['n_sentences']
	data[Id] = essay 	# The information of the current essays is saved to 'data'
	numFeat = len(fs)	
 
 #The procedure above is repeated for the test data.
 if TEST:
  for row in reader_test:
	line = row.split('\t')
	if line[0] == 'Id':				continue
	Id = int(line[0])
	essay = { }
	essay['set'] = int(line[1])
	if not essay['set'] == SET:		continue
	essay['text'] = cleantext(line[2], SET)
	labe = []
	docs_test, docs2_test, docs_u_test, docs_b_test, docs_t_test, vocab1_test, vocab2_test, vocab3_test, inv_index_test, inv_index_u_test, inv_index_b_test, inv_index_t_test = a_essay ( Id, essay['text'], docs_test, docs2_test, docs_u_test, docs_b_test, docs_t_test, vocab1_test, vocab2_test, vocab3_test, inv_index_test, inv_index_u_test, inv_index_b_test, inv_index_t_test)	
	fs, fi_test, fi2_test = feature(text = essay['text'], fi = fi_test, set = SET, Id = Id, score = 0, score2 = 0, fi2 =fi2_test, label = labe)	
	f, fs = calculate_f(fs, SET)
		
	text = essay['text']
	essay['f'] = f	
	essay['fs'] = fs
	essay['n_words'] = len(text.split() )
	essay['n_sentences'] = len( text.split( '.' ) )
	essay['sentence_ave_size'] = essay['n_words'] * 1./ essay['n_sentences']
	data_test[Id] = essay
	
 # The raw counts of words, bigrams and features are weighted using 
 # 'term frequency - inverse document frequency'. # The length of each
 # vector of words is also calculated
 tfidf, leNN = calc_tfidf( inv_index, len(docs) )
 tfidf_u, leNN_u = calc_tfidf( inv_index_u, len(docs) )
 tfidf_b, leNN_b = calc_tfidf( inv_index_b, len(docs) )
 tfidf_t, leNN_t = calc_tfidf( inv_index_t, len(docs) )

 if TEST:
  tfidf_test, leNN_test = calc_tfidf( inv_index_test, len(docs) , inv_index)
  tfidf_u_test, leNN_u_test = calc_tfidf( inv_index_u_test, len(docs) , inv_index_u )
  tfidf_b_test, leNN_b_test = calc_tfidf( inv_index_b_test, len(docs) , inv_index_b )
  tfidf_t_test, leNN_t_test = calc_tfidf( inv_index_t_test, len(docs) , inv_index_t )

 print 'Normalizing vectors' 
 fi = normalize ( fi )
 fi2 = normalize2 ( fi2 )
 numSim = { 1: len( fi ), 2: len(fi2) }
 print 'Finding cosine similarities 1' #between each essay and each answer
 for Id in data:			data[Id]['lsim_list'] = cos_sim ( data[Id]['text'], Id, fi, tfidf, leNN)
 if TEST: 
 	for Id in data_test:	data_test[Id]['lsim_list'] = cos_sim ( data_test[Id]['text'], Id, fi, tfidf_test, leNN_test)	

 print 'Finding cosine similarities 2' #between each essay and each match of an answer
 for Id in data:			data[Id]['lsim_list2'] = cos_sim2 ( data[Id]['text'], Id, fi2, tfidf, leNN)
 if TEST: 
 	for Id in data_test:	data_test[Id]['lsim_list2'] = cos_sim2 ( data_test[Id]['text'], Id, fi2, tfidf_test, leNN_test)	
	
 tol1 = 10
 tol2 = 10
 tol3 = 10

 vocab_1 = []
 vocab_2 = []
 vocab_3 = []
# Only words, bigrams, and trigrams with counts greater than tol are used.
 for word in vocab1:
	if len(inv_index_u[word]) > tol1  : vocab_1.append( word )
 for word in vocab2:
	if len(inv_index_b[word]) > tol2 : vocab_2.append( word )
 for word in vocab3:
	if len(inv_index_t[word]) > tol3 : vocab_3.append( word )	


 print 'Writing Files'
 write(SET, 'training', vocab_1, vocab_2, vocab_3, inv_index_u, inv_index_b, inv_index_t, data, docs_u, docs_b, docs_t , tfidf_u, tfidf_b, tfidf_t, numFeat, numSim , leNN_u)
 if TEST:
  	write(SET, 'test', vocab_1, vocab_2, vocab_3, inv_index_u_test, inv_index_b_test, inv_index_t_test, data_test, docs_u_test, docs_b_test, docs_t_test , tfidf_u_test, tfidf_b_test, tfidf_t_test, numFeat, numSim , leNN_u_test)
  