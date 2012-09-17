#LT Autograder. A system that automatically grades short answer essays.
#Copyright (C) 2012 Luis Tandalla

import collections

def a_essay ( Id, text, docs, docs2, docs_u, docs_b, docs_t, vocab1, vocab2, vocab3, inv_index, inv_index_u, inv_index_b, inv_index_t):
	# This function calculates the vector of words, bigrams, and trigrams and the inverted index of each of them from 'text'. 
	# The resulting calculations are added to all of the 'docs' and the 'inv_index's. Also, the new words, bigrams, and trigrams
	# appeared are added to the 'vocab's. 
	
	docs2[Id] = collections.defaultdict(lambda: 0.0)
	docs_u[Id] = collections.defaultdict(lambda: 0.0)
	docs_b[Id] = collections.defaultdict(lambda: 0.0)
	docs_t[Id] = collections.defaultdict(lambda: 0.0)
				
	twords2 = text.split(' . ') #Split the text in sentences
	sufId = 0
	word_prev = ''
	word_prev2 = ''
	for twords3 in twords2:
		if twords3 == '':
			continue
		twords = twords3.split() # Split the sentence in words
		sufId += 1
		Idb = str(Id) + '_' + str(sufId) #Id of sentence


		for word in twords:
			if word == '.':			continue
			docs[Idb] = collections.defaultdict(lambda: 0.0)
			docs[Idb][word] = docs[Idb][word] + 1
			docs2[Id][word] = docs2[Id][word] + 1
			docs_u[Id][word] = docs_u[Id][word] + 1
			
			bigram = word_prev + "_" + word
			trigram = word_prev + "_" + word_prev2 + "_" + word
			

			vocab1[word] = vocab1[word] + 1
													
			if word not in inv_index:				inv_index[word] = collections.defaultdict(lambda: 0.0)
			inv_index[word][Idb]  = inv_index[word][Idb] + 1

			if word not in inv_index_u:				inv_index_u[word] = collections.defaultdict(lambda: 0.0)
			inv_index_u[word][Id]  = inv_index_u[word][Id] + 1
		
			if word_prev == '':						word_prev = word
			else:
				if bigram not in inv_index_b:		inv_index_b[bigram] = collections.defaultdict(lambda: 0.0)
				inv_index_b[bigram][Id]  = inv_index_b[bigram][Id] + 1
				docs_b[Id][bigram] = docs_b[Id][bigram] + 1
				vocab2[bigram] = vocab2[bigram] + 1

				if word_prev2 == '':
					word_prev2 = word_prev
					word_prev = word					
				else:
					if trigram not in inv_index_t:	inv_index_t[trigram] = collections.defaultdict(lambda: 0.0)
					inv_index_t[trigram][Id]  = inv_index_t[trigram][Id] + 1
					docs_t[Id][trigram] = docs_t[Id][trigram] + 1
					vocab3[trigram] = vocab3[trigram] + 1

					word_prev2 = word_prev
					word_prev = word

	return docs, docs2, docs_u, docs_b, docs_t, vocab1, vocab2, vocab3, inv_index, inv_index_u, inv_index_b, inv_index_t

def calculate_f(fs, SET):
	#Given fs, a list of features with 0's or 1's and the set, this function
	# calculate more features and a score for the essay using only this list.
	f = sum(fs)
	sf = sum(fs)
	
	if SET == 2:			
		f = int(sum(fs[0:4])>0) + sum(fs[4:]) 
		fs.append( sum(fs[4:]) )
	if SET == 3:			
		#f = sum(fs[:10]) 
		f = int(sum(fs)>0) 
		fs1 = int ( sum( [ fs[13], fs[5] , fs[7] , fs[9] ] ) > 0 )
		fs2 = int ( sum( [ fs[8] , fs[10] , fs[11], fs[12]   ] ) > 0 )
		#fs2 = int ( sum( [ fs[26] ] ) > 0 )
		fs3 = 0
		fs3 = int ( sum( [ fs[8] , fs[10] , fs[11], fs[12] ] ) > 1 )


		f = fs3 + fs2
		fs.append(fs1)
		fs.append(fs2)
		fs.append(fs3)
#		f = sum( [ fs[8] , fs[10] , fs[11], fs[12]   ] )
		if f > 2 : f = 2
	if SET == 4:			
		fs1 = int(f>0)
		fs2 = int( sum(fs) > 4)
		f = fs1 + fs2
		fs.append(fs1)
		fs.append(fs2)

	if SET == 5:	
		if f == 0: f =0
		elif f == 1 or f ==2: f = 1
		elif f == 3: f =2
		else: f =3

	if SET == 6:
		if f > 3: f = 3
	if SET == 7:
		fs1 = int ( sum(fs[:10]) > 0 )
		fs2 = int ( sum(fs[10:]) > 0 and fs1 > 0)
		f = fs1 + fs2
		fs.append(fs1)
		fs.append(fs2)

	if SET == 8:
		if f > 2: f = 2
	if SET == 9:
		if f > 2: f = 2

	if SET == 10:

		fs1 = int ( sum( [ fs[0], fs[3], fs[6], fs[9] ] ) > 0 )
		fs2 = int ( sum( [ fs[21], fs[1], fs[4], fs[7], fs[10], fs[20] ] ) > 0 )
		fs3 = int ( sum( [ fs[2], fs[5], fs[8], fs[11], fs[12], fs[13], fs[14], fs[15], fs[16], fs[17], fs[18], fs[19] ] ) > 0 )
		f = fs1 + fs2 + fs3
		f = f-1
		if f > 2: f = 2
		if f < 0: f = 0
		fs.append(fs1)
		fs.append(fs2)
		fs.append(fs3)

	fs.append(sf)

	return f, fs