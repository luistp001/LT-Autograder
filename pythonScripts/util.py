#LT Autograder. A system that automatically grades short answer essays.
#Copyright (C) 2012 Luis Tandalla

import collections, re, math
import sys

def cleantext(text, SET ):
	text=text.lower()
	
	textn = ""
	for let in text:
		if let.isalpha() or let.isdigit():
			textn = textn + let
		elif let == '.':
			textn = textn + " . "
		else:
			textn = textn + ' '
	text = textn

	while text.find('  ') > 0:
		text = text.replace('  ', ' ')

	to_replace = ['do', 'ca', 'did', 'does','was', 'is', 'were', 'should', 'would', 'are', 'wo', 'could']
	for to_change in to_replace:
		to_change_old = to_change + 'n t '
		to_change_new = to_change + 'nt '
		text = text.replace(to_change_old, to_change_new)	
	text = text.replace('it s ', 'its ')		
	text = text.replace('thei re ', 'theire ')			
	
	words_of_text = text.split()
	word_prev = words_of_text[0]
	word_now = ''
	textn = word_prev 
	for i in range(len(words_of_text)-1):
		word_now = words_of_text[i+1]
		if  not ( word_prev == word_now ):
			textn = textn + ' ' + word_now
		word_prev = word_now
	text = textn
	if SET == 7:
		text = text.replace('realli ', '')
		text = text.replace('alwai ', '')
		text = text.replace('find a wai to ', '')
		text = text.replace('seem to be ', 'is ')
		text = text.replace('is try to be ', 'is ')

	return text

def toint(let): #This function is not necessary
	if let == '0':
		return 0
	if let == '1':
		return 1
	if let == '2':
		return 2
	if let == '3':
		return 3

def fet(text, patterns, pr = False):
	# This functions returns '1' if any of the patterns
	# is found in text.
	essa = text.lower()
	for pat in patterns:
		match = re.search(pat, essa)
		if match is not None:
			if pr:
				print match.group(0)
			return '1', match.group(0)
	return '0', None


def calc_tfidf ( inv_index, num_documents, inv_index_train = None ):
	# It weights the raw counts of inv_index using 'term frequency - inverse document frequency'.
	if not inv_index_train: inv_index_train = inv_index # When testing, the the inverted index obtained
														# from training is used. When training, only one
														# inverted index is used.	

	tfidf = collections.defaultdict(lambda: collections.defaultdict(lambda: 0.0) )
	leNN = collections.defaultdict(lambda: 0.0)
	
	for word in inv_index_train:	
		#print num_documents
		#print len ( inv_index_train[word]  )
		idf = math.log10( num_documents  / float( len ( inv_index_train[word]  ) + 1 )  )
		if word in inv_index:
		  for Id in inv_index[word]:
			tf = inv_index[word][Id]
			tfidf[word][Id] = ( 1 + math.log10(tf) ) * idf
			leNN[Id] = leNN[Id] + tfidf[word][Id]**2
	for Id in leNN:
		leNN[Id] =math.sqrt( leNN[Id] )

	return tfidf, leNN

def normalize ( list_of_vec): 
	#It applies 1 + log and normalizes a list of vectors
	new_list = []

	for vec in list_of_vec:
		normvec = 0.0
		for word in vec:
			vec[word] = 1 + math.log10(vec[word])
			normvec += vec[word] ** 2
		for word in vec:
			vec[word] = vec[word] / math.sqrt(normvec)
		new_list.append ( vec )

	return new_list

def normalize2 ( list_of_vec): 
	#It applies 1 + log and normalizes a dictionary lists of vectors

	new_dict = {}

	for i in list_of_vec: # It iterates over the answers
	 	new_list = []
	 	for vec in list_of_vec[i] : # It iterates over matches for an answer
	 		new_line_match_dic = {}
			normvec = 0.0
			for word in vec: # It iterates over each word of a match.
				new_line_match_dic[word] = 1 + math.log10(vec[word])
				normvec += new_line_match_dic[word] ** 2
			for word in vec:
				new_line_match_dic[word] = new_line_match_dic[word] / math.sqrt(normvec)
			new_list.append ( new_line_match_dic ) # It adds new match to the new LIST
	 	new_dict[i] = new_list # It adds new list of answer to new dictionary 

	return new_dict




def cos_sim ( text, Id, features_vec, tfidf, leNN): 
	# This function calculates cosine similarity between 'text' and each
	# of the answers in features_vec
	
	sentenc = text.split(' . ')
	lsim = []
	return lsim
	for fis in features_vec: #It iterates over answers
		scores = []
		sufId = 0
		for twords3 in sentenc: #It iterates over the words of the text
			if twords3 == '':
				continue
			sufId += 1
			Indb = str(Id) + '_' + str(sufId)
			scor = 0.0
			for word in fis: #It iterates over the words of an answer
				if word in tfidf and Indb in tfidf[word]: #It uses the calculated tfidf
					scor += tfidf[word][Indb] * fis[word]  #weighted counts of words
			if leNN[Indb] == 0: scor = 0
			else:	scor = scor / leNN[Indb]
			scores.append( scor )
		lsim.append( max(scores) )
	return lsim

def cos_sim2 ( text, Id, features_vec, tfidf, leNN): #between features and  text
	# This function calculates cosine similarity between 'text' and each
	# match for each of the answers in features_vec

	if int(Id) % 100 == 0: print Id
	sentences = text.split(' . ')
	lsim = []
	# This resulting values of this function were used in the development phase,
	# but they are not used in the final model. Also, it takes some time to run
	# because there are four nested loops. For this reason, currently, it only 
	# returns an empty list .
	return lsim
	for i in features_vec: #It iterates over answers
	  possible_scores = [ 0.0 ]
	  for line_match_dict in features_vec[i]:		#It iterates over the matches of an answer
		scores = []
		sufId = 0
		for sentence in sentences: # It iterates over each sentence of the text
			if sentence == '':
				continue
			sufId += 1
			Indb = str(Id) + '_' + str(sufId)
			scor = 0.0
			for word in line_match_dict: # It iterates over the word of each match
				if word in tfidf and Indb in tfidf[word]:
					scor += tfidf[word][Indb] * line_match_dict[word] 
			if leNN[Indb] == 0: scor = 0
			else:	scor = scor / leNN[Indb] # Score is the cosine similarity bewteen a sentence
											 # of a text and a match of features_vect
			possible_scores.append( scor ) 
	  lsim.append( max(possible_scores) )
	return lsim


def update_ans( ans, line_match, fi, index, matchs, answer, fi2 = collections.defaultdict(lambda: [])):
	
	if ans == '1':
		matchs.append( line_match ) 
		line_match_dict = collections.defaultdict(lambda: 0.0)
		for word in line_match.split():
			fi[index][word] = fi[index][word] + 1
			line_match_dict[word] = line_match_dict[word] + 1		
		if not line_match_dict in fi2[index]:
			fi2[index].append( line_match_dict )
	answer.append( int(ans) )
	return answer, fi, matchs, fi2

def reset (index, fi):
	index +=1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	return ans, index, fi, pats


def write(SET, type, vocab1, vocab2, vocab3, inv_index_u, inv_index_b, inv_index_t, data, docs_u, docs_b, docs_t , tfidf_u, tfidf_b, tfidf_t, numFeat, numSiml, leNN):
	# This functions writes all the calculated values of the essays in different files

	numSim = numSiml[1]
	numSim2 = numSiml[2]
	ofile ="%s/%s_%d.csv" % ( type, type, SET )		# This file is the main file that contains the scores given by both graders, the
	filew = open(ofile, "w")						# predicted score calculated, the number of words, sentences, and average size of sentences.
	ofile ="%s/%s_%d_f.csv" % ( type, type, SET )	# This file contains the lists that an essay have the answers or not. 
	filewf = open(ofile, "w")
	ofile ="%s/%s_%d_s.csv" % ( type, type, SET )	# This file contains the first type of cosine similarities
	filews = open(ofile, "w")

	ofile ="%s/%s_%d_s2.csv" % ( type, type, SET )	# This file contains the second type of cosine similarities
	filews2 = open(ofile, "w")


	ofile ="%s/%s_%d_w.csv" % ( type, type, SET )	# This file contains the bag of words
	fileww = open(ofile, "w")
	ofile ="%s/%s_%d_wt.csv" % ( type, type, SET )	# This file contains the bag of words with tfidf weighting
	filewwt = open(ofile, "w")
	ofile ="%s/%s_%d_b.csv" % ( type, type, SET )	# This file contains the bag of bigrams
	filewb = open(ofile, "w")
	ofile ="%s/%s_%d_bt.csv" % ( type, type, SET )	# This file contains the bag of bigrams with tfidf weighting
	filewbt = open(ofile, "w")
	ofile ="%s/%s_%d_t.csv" % ( type, type, SET )	# This file contains the bag of trigrams
	filewt = open(ofile, "w")
	ofile ="%s/%s_%d_tt.csv" % ( type, type, SET )	# This file contains the bag of trigrams with tfidf weighting
	filewtt = open(ofile, "w")

	ofile ="%s/%s_%d_n.csv" % ( type, type, SET )	# This file contains the bag of words normalized with tfidf weighting
	filewn = open(ofile, "w")

	filew.write("Id,f,")
	if type == 'training': filew.write("f2,f3," )
	filew.write("n_words,n_sentences,sentenc_ave_size")
	filewf.write("Id")
	filews.write("Id")
	filews2.write("Id")
	fileww.write("Id")
	filewwt.write("Id")
	filewb.write("Id")
	filewbt.write("Id")
	filewt.write("Id")
	filewtt.write("Id")
	filewn.write("Id")
	
	for i in range ( numFeat ):						filewf.write(",feature_" + str(i))
	for i in range ( numSim ):						filews.write(",sim_" + str(i))
	for i in range ( numSim2 ):						filews2.write(",sim2_" + str(i))
	for word in vocab1:								fileww.write("," + word)
	for word in vocab1:								filewwt.write("," + word)
	for word in vocab1:								filewn.write("," + word+'_n')
	for word in vocab2:								filewb.write("," + word)
	for word in vocab2:								filewbt.write("," + word)
	for word in vocab3:								filewt.write("," + word)
	for word in vocab3:								filewtt.write("," + word)

	filew.write("\n")
	filewf.write("\n")
	filews.write("\n")
	filews2.write("\n")
	fileww.write("\n")
	filewwt.write("\n")
	filewb.write("\n")
	filewbt.write("\n")
	filewt.write("\n")
	filewtt.write("\n")
	filewn.write("\n")


	for Id in data:
		if Id % 100 == 0: print 'writing ' + str(Id)
		essay = data[Id]		
		fs = essay['fs']
		lsim = data[Id]['lsim_list']
		lsim2 = data[Id]['lsim_list2']

		filew.write(str(Id))
		filewf.write(str(Id))
		filews.write(str(Id))
		filews2.write(str(Id))
		fileww.write(str(Id))
		filewwt.write(str(Id))
		filewb.write(str(Id))
		filewbt.write(str(Id))
		filewt.write(str(Id))
		filewtt.write(str(Id))
		filewn.write(str(Id))
	
		filew.write(",%d," % (essay['f']) )
		if type == 'training': filew.write("%d,%d," % (essay['s1'], essay['s2']) )
		filew.write("%d,%d,%f" % ( essay['n_words'], essay['n_sentences'], essay['sentence_ave_size'] ) )
	
	
		for ai in fs:									filewf.write("," + str(ai))
		for ai in lsim:									filews.write("," + str(ai))
		for ai in lsim2:								filews2.write("," + str(ai))
		for word in vocab1:								fileww.write("," + str( docs_u[Id][word] ) )
		for word in vocab1:								filewwt.write("," + str( tfidf_u[word][Id] ) )
		for word in vocab1:								
			if leNN[Id] > 0:
				pr = tfidf_u[word][Id] / leNN[Id]
			else: pr = 0
			filewn.write("," + str( pr ) )
		for word in vocab2:								filewb.write("," + str( docs_b[Id][word] ) )
		for word in vocab2:								filewbt.write("," + str( tfidf_b[word][Id] ) )
		for word in vocab3:								filewt.write("," + str( docs_t[Id][word] ) )
		for word in vocab3:								filewtt.write("," + str( tfidf_t[word][Id]) )
		filew.write("\n")
		filewf.write("\n")
		filews.write("\n")
		filews2.write("\n")
		fileww.write("\n")
		filewwt.write("\n")
		filewb.write("\n")
		filewbt.write("\n")
		filewt.write("\n")
		filewtt.write("\n")
		filewn.write("\n")
	return
