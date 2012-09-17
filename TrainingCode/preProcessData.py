#LT Autograder. A system that automatically grades short answer essays.
#Copyright (C) 2012 Luis Tandalla

#Preprocessing stage, Training
import sys
sys.path.append('../pythonScripts')

from pr1 import process1
from pr2 import process2
from pr3 import process3

nameTrainingIn = '../TrainingFile/train_rel_2.tsv'
nameTrainingOut1 = '../AdditionalFiles/train_rel_2_2.tsv'
nameTrainingOut2 = '../AdditionalFiles/train_rel_2_3.tsv'


process1( nameTrainingIn, nameTrainingOut1, test = False) #correcting mispelled words
print '\nStemming'
process2( nameTrainingOut1, nameTrainingOut2 ) 
print 'Calculating Features'
for SET in range(1,11):
 process3( SET, False , nameTrainingOut2) 