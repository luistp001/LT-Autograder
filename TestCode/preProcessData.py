#LT Autograder. A system that automatically grades short answer essays.
#Copyright (C) 2012 Luis Tandalla

#Preprocessing stage, Testing
import sys
sys.path.append('../pythonScripts')

from pr1 import process1
from pr2 import process2
from pr3 import process3

nameTrainingOut1 = 'train_rel_2_2.tsv'
nameTrainingOut2 = 'train_rel_2_3.tsv'
nameTestIn = '../TestFile/test.tsv'
nameTestOut1 = '../AdditionalFiles/test_2.tsv'
nameTestOut2 = '../AdditionalFiles/test_3.tsv'



process1( nameTestIn, nameTestOut1, test = True)  #correcting mispelled words
print 'Stemming'
process2( nameTrainingOut1, nameTrainingOut2 )
process2( nameTestOut1, nameTestOut2 )
print 'Calculating Features'
for SET in range(1,11):
 process3( SET, True, nameTrainingOut2, nameTestOut2 )