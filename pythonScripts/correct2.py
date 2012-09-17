#LT Autograder. A system that automatically grades short answer essays.
#Copyright (C) 2012 Luis Tandalla

import re, collections, sys
#This file uses code from http://norvig.com/spell-correct.html

def words(text): return re.findall('[a-z]+', text.lower()) 
  #It returns all the words from a text

def train(features):
  #It returns two dictionaries with the counts of words 
  #and bigrams contained in the file features
    model = collections.defaultdict(lambda: 1)
    model2 = collections.defaultdict(lambda: 1)
    for f in features:
        model[f] += 1
    for i in range(len(features) - 1):
      f = features[i] +  " " + features[i+1]
      model2[f] += 1
    return model, model2


class correct2:

  def __init__(self, SET = '0'):
    # It creates lexicon (list of right words)
    # It creates a list of special words depending on the set
    # It creates a list of extra words
    # It creates two dictionaries with the counts of words and bigrams

    self.SET = int(SET)    
    self.unify = False
    if SET == 10: self.unify = True
    self.NWORDS, self.NWORDS2 = train(words(file('../AdditionalFiles/big.txt').read())) #It calculates counts of words and bigrams
                                                                     #from file 'big.txt'
    reader2 = file('../AdditionalFiles/ae2.txt').read()                      # It creates lexicon from
    self.lexicon = re.findall( r'(\w+)\n', str(reader2))  # file 'ae2.txt' 
    self.special = [] #It creates a  list of special words
    if SET == 1:
      self.special.extend( [ 'vinegar','experiment','replicate','samples','containers','rinse'])

    if SET == 2:
      self.special.extend( [ 'stretchable','stretchability','stretchiest','unstretched'])

    if SET == 3 or SET == 4:
      self.special.extend( [ 'generalist','federalist', 'generalists','federalists','python', 'pythons','mice','panda','koala','achenbach','koalas','pandas','alligator','alligators','lizzard','lizzards','crockadile','crockadiles'])
      self.special.extend( [ 'herbivores','vegetarians', 'pg', 'herbivore','vegetarian', 'repopulate','pg','raccoon','raccoons','australia','warmness','carnivores','carnivore' ,'antartica','macinnes','predator','predators'] )

    if SET == 5 or SET == 6:
      self.special = ['rna', 'dna', 'trna', 'mrna', 'rrna', 'amino', 'golgi', 'er', 'codon', 'peptide', 'atp', 'membrane','anticodon','anticodons','codons','polypeptide' ]
      self.special.extend( [ 'corrosion','reticulum','endoplasmic','ribosomes','ribosome','lysosomes','lysosome','endocytosis','meiosis','mitochondria','phospolipids','metaphase','hypertonic','hypotonic'])
      self.special.extend( [ 'protein','proteins','telophase','phagocytosis','cellium','cytosis','osmosis','anaphase','homeostasis','exoplasmic','eukaryotes','exocytosis', 'prophase'])
      self.special.extend( [ 'vacuole','vacuoles','interphase','photosynthesis','solute','prokaryotes', 'mitochondrion','chromatid', 'ionic', 'chloroplast', 'nucleotide', 'nucleotides', 'permeability', 'nucleolus', 'flagellum', 'mutualism', 'organelle', 'organelles', 'permeable', 'cytoplasm', 'pseudopod', 'glycolysis', 'catalyst'])
      self.special.extend( [ 'movement','ribosomal' , 'cytokinesis','prokaryotic','eukaryotic','translocation','nucleus','isotonic'] )

    if SET == 7:
      self.special.extend( [ 'paul',  'anna', 'kolab','angeles','cambodia','los','sacramento','hearted','hardworking'])
    if SET == 8:      
      self.special.extend( [ 'mr', 'leonard', 'grabowski','obstacles','remediation','hurdler','hurdlers'])
    if SET == 9:
      self.special.extend( [ 'microdebris','catalogues', 'microsatellites', 'subtopic','subtopics','nasa','astronauts','astronaut','catalogues','timeline', 'subtitles', 'toolbag','junk'])
      self.special.extend( [ 'micro','junk'])
    if SET == 10:
      self.special.extend( [ 'deg','color' , 'attract','hotter','hottest','heat','cooler','coolest', 'black','gray','white'] )

    #Create list of extra words
    self.extra = ['dont', 'etc' ,'didnt','cant','doesnt','isnt', 'hasnt', 'im','wouldnt','american','couldnt', 'wont','responsibility','wasnt','url','gpa','werent','hadnt','arent','shouldnt','werent']
    self.extra.extend ( ['don', 'etc' ,'didn','can','doesn','isn','ok', 'hasn', 'im','wouldn','american','couldn', 'won','wasn','url','gpa','weren','hadn','aren','shouldn','weren','mph','intro','cliche','micro','persuasive','sequential','hmm','tech','corrosion','kg'] )
    self.extra.extend ( ['miligram','ie','mm','ml','covalent','outlier','experiment','lb','hr', 'usa','mc','theyre','tv','uneased','peachy','unpleased','dismissive'] )

    self.lexicon.extend( self.special)
    self.lexicon.extend( self.extra)
    
    for wor in self.special:  self.NWORDS[wor] = 10000 # It gives a high count to special words so
                                                       # so that they are preferred when a word is corrected

    for wor in self.extra:    self.NWORDS[wor] = 2      #It gives an slighly higher preference to extra words.


    
    self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
    self.cache = {}       # Main cache
    self.caches = {}      # Cache of words corrected to special words
    self.cache2 = {}      # Cache of words corrected using bigrams
    self.cache_union = {} # Cache in which the word was united to the next word
    self.small_lexicon = [] # Lexicon of words already corrected

    self.candidates2 = set()
    self.lexicon2 = [ word for word in self.lexicon if len(word) == 2 ]
    self.eliminate = False

    self.lex = {}
    #It creates list of lexicons so that each object of a list has word with the same length
    #This is done to improve speed.
    for i in range(20):
      self.lex[i+1] = [word for word in self.lexicon if len(word) == (i+1) ]
    self.lex[0] = [word for word in self.lexicon if len(word) >= 20 ] 

  def in_lexicon( self, word ):
    #It checks if a word is a right word (a not mispelled word).
    i = len(word)
    if i in self.lex: return word in self.lex[i] 
    else:             return word in self.lex[0]

  def edits1(self,word):
   # It returns a set with words that have an edit distance of 1 with the 'word'
   splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
   deletes    = [a + b[1:] for a, b in splits if b]
   transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
   replaces   = [a + c + b[1:] for a, b in splits for c in self.alphabet if b]
   inserts    = [a + c + b     for a, b in splits for c in self.alphabet]

   a = set(deletes + transposes + replaces + inserts)
   return a

  def check_deletion(self,word, candidate):
      # It checks if a right word was eliminated to produce candidate. 
      # If it was, the eliminate word is included to be returned.
      # For example, if word is tovinegar and candidate is vinegar,
      # it returns 'to vinegar' instead of just 'vinegar'.
      # Only words of length 2 are checked if they were eliminated.

      if len(word) - len(candidate) == 1 or len(candidate) > len(word):
        
        return  candidate
      if word.find(candidate) == 0 and word[len(candidate):] in self.lexicon2:
        
        return candidate + " " + word[len(candidate):]
      if word.find(candidate) == len(word) - len(candidate) and word[:len(word) - len(candidate)] in self.lexicon2:
          
          return  word[:len(word) - len(candidate)] + " " + candidate
      return candidate


  def known_edits2(self,word):
    # It returns two sets of right words. The words of one set have edit distance 
    # of 2 with the 'word' and the words of the other set have edit distance of 1. 
    # The original word is also included in both sets.

    b = self.edits1(word)
    c = self.known(b)
    a = set(e2 for e1 in b for e2 in self.edits1(e1) if e2 in self.small_lexicon or e2 in self.NWORDS )

    return (a.union(c)).union( set([word]) ), c.union( set([word]) ) 

  def known(self,words): return set(w for w in words if w in self.small_lexicon or self.in_lexicon( w ))
    # It returns a set of right words that have edit distance of 1 with the 'word'


  def correct_2(self,word, wordp = "", wordn = "", type = 1):
    # It returns a word after mispelling errors are corrected.
    # word is the word to correct.
    # wordp is the word written before 'word'
    # wordn is the word written after 'word'
    # This function is may be called iteratively once. Type
    # is the level of recursion in which the function is currently working.

    if type == 1 :  self.candidates2, candidates = self.known_edits2(word)
      # It calculates the right words with edit distance of 1 and 2.
    if type == 2 :  candidates = self.candidates2
      # candidates is the list of words is set to the list of right words 
      # with edit distance of 2 that was already calculated in the first level of recursion
    candidates2 = self.candidates2
    
    if type == 1 :
      # If a word of candidates is special, this word is returned as the corrected word.
      # The correction is added to a cache to avoid recalculation of corrected word.
      
      candidates4  = [candidate for candidate in candidates2 if len(candidate) > 4]
      candidates5  = [candidate for candidate in candidates if len(candidate) <= 4]

      for candidate in candidates4:
        if candidate in self.special:        
          temp = self.check_deletion (word, candidate)
          self.caches[word] = temp
          
          return temp
      for candidate in candidates5:
        if candidate in self.special:        
          temp = self.check_deletion (word, candidate)
          self.caches[word] = temp
          
          return temp          
        
    if not wordp == "":
      # If previous word is not empty, It forms a list of bigrams
      # with the previous word and each word of candidates. 
      # It finds the bigram with the highest count in NWORDS2.
      # If the count is greater than 1, it returns the candidate
      # that produced that bigram.

      candidates2t = set()
      for wordne in candidates:    candidates2t.add(wordp + " " +wordne)
      if len( candidates2t ) > 0:
        c2 = max(candidates2t, key=self.NWORDS2.get)
        if self.NWORDS2[c2] > 1:            
          temp = self.check_deletion (word, c2.split()[1])    
          self.cache2[wordp + ' ' + word] = temp
          
          return temp
    if word in self.cache:  return self.cache[word]

    possible_answer = max(candidates, key=self.NWORDS.get) # it finds candidate with the 
                                                           # highest count in NWORDS.


    if self.in_lexicon( possible_answer ):                 # If the possible answer is a right 
      return self.check_deletion (word, possible_answer)   # word, it is returned.

    if type == 1:  # It corrects the word at a second level of recursion
      possible_answer = self.correct_2(word, wordp, wordn, 2) 
    if type == 2: return possible_answer # The following steps are only done
                                         # with candidates that have edit distance of 1 
                                         # to the original word. Therefore, at the second level,
                                         # possible answer is returned even if it is not right.


    if self.in_lexicon( possible_answer ) :              # Possible answer is checked if is right, because
      return self.check_deletion (word, possible_answer) # it could be a no right (mispelled) word
                                                         # returned from the second level of recursion

    if len(possible_answer) >=4 and not self.in_lexicon( possible_answer ) :
      splits = [(word[:i+2], word[i+2:]) for i in range(len(word) - 3)] # It produces splits of the word           
      for word1, word2 in splits:
       if self.in_lexicon(word1) and self.in_lexicon(word2):  # If both words of a split are right, 
        return word1 + ' ' + word2                            # it returns the split

      pos_answ = ['','','']
      for word1, word2 in splits: 
        # Finds the splits that have one word right, but keeps the split with the longest
        # right word. Then, it corrects the other word and returns the split.
       if len( pos_answ[0]) < len(word1) and self.in_lexicon(word1) :  pos_answ = [word1, word1, word2 ]
       if len( pos_answ[0]) < len(word2) and self.in_lexicon(word2) : pos_answ = [word2, word1, word2 ]
      if not pos_answ[0] =='' : return self.correct( pos_answ[1] ) + ' ' + self.correct( pos_answ[2] )
      
    return self.check_deletion (word, possible_answer) # It the program goes to this point, it means 
                                                       # that the original word could not be corrected,
                                                       # so possible word is the same as the original word.


  def correct(self,word, wordp = "", wordn = ""):
    if self.SET == 10 and word.isdigit(): 
      return word

    if self.eliminate: 
      self.eliminate = False
      return ""

    union = word + wordn
    if self.unify: # This is done only for set 10
                   # It checks if the word added with the next word form a right word.
                   # If it does, the combined word is returned. Also, self.eliminate
                   # kepps track of this change so that when correcting the next word,
                   # it is eliminated.
     if (word, wordn) in self.cache_union:     
      self.eliminate = True
      return self.cache_union[ (word, wordn) ]
     else:
      #The following 4 lines are not neccesary
      if not word == 'c' and not wordn == "" and not wordn == 'a' and ( not self.in_lexicon( wordn ) or len(wordn) == 1) and self.in_lexicon( union ) :
        self.eliminate = True
        self.cache_union[ (word, wordn) ] = union
        return union
      #The following 4 lines are not neccesary
      if not word == 'c' and not wordn == "" and not word == 'a' and ( not self.in_lexicon( word ) or len(word) == 1) and self.in_lexicon( union ) :
        self.eliminate = True
        self.cache_union[ (word, wordn) ] = union
        return union

      if not word == 'c' and not wordn == "" and self.in_lexicon( union ) :
        self.eliminate = True
        self.cache_union[ (word, wordn) ] = union
        return union

    word = word.replace('obsti', 'obstac')
    if word in self.small_lexicon:    return word
    if word == '.': return word 
    if word == 'movment': return 'movement'
    if word == 'alot': return 'a lot'
    if word == 'careing': return 'caring'
    if word == 'carring': return 'caring'
    if word == 'ana': return 'anna'
    if word == 'repete': return 'repeat'
    if word == 'kalob': return 'kolab'
    if word == 'maibe': return 'maybe'
    if word == 'lable': return 'label'
    if word == 'resturaunt': return 'restaurant'
    if word == 'restraunt': return 'restaurant'
    if word == 'stuned': return 'stunned'
    if word == 'obsticles': return 'obstacles'
    if word == 'greatful': return 'grateful'
    if word == 'incommon': return 'in common'
    if word == 'coudnt': return 'couldnt'
    if word == 'dosen': return 'doesnt'
    if word == 'nt': return 'not'
    if word == 'excell': return 'excel'
    if word == 'outter': return 'outer'
    if word == 'amant' or word == 'amnt': return 'amount'
    if word == 'tipe': return 'type'
    if word == 'tripple': return 'triple'
    if word == 'hrs': return 'hours'
    if word == 'mins': return 'minutes'
    if word == 'fead': return 'feed'
    if word == 'incase': return 'in case'
    if word == 'themost': return 'the most'
    if word == 'expirement': return 'experiment'
    if word == 'shrinked': return 'shrunken'
    if word == 'donot': return 'do not'
    if word == 'inchina': return 'in china'
    if word == 'ect': return 'etc'
    if word == 'colour': return 'color'
             
    bigram = wordp + ' ' + word
    #It checks if a possible correction is available in the caches.
    if bigram in self.cache2:   return self.cache2[bigram]
    if word in self.caches:     return self.caches[word]
    if self.in_lexicon( word ): 
      self.small_lexicon.append ( word )
      return word
        
    lb = len(self.cache2) #length of 'cache using bigrams' before correcting word
    temp = self.correct_2( word, wordp, wordn)
    la = len(self.cache2) #length of 'cache using bigrams' after correcting word
    # It checks if 'cache using bigrams' is was not changed, if not and if the word
    # is not already in cache, add word with correction to main cache.
    if word not in self.cache and la == lb: self.cache[word] = temp
    return temp

if __name__ == "__main__":
    au = correct2(5)
    print au.special

