This program is the source code of my final submission for the Kaggle Competition 
"Automated Student Assessment Prize, Phase Two – Short Answer Scoring". 

Requirements:
- python 2.7 or greater
- package R with libraries Boruta, randomForest, nlme, and gbm (these can be installed from the CRAN)

The program can be run on Windows or Linux, but Linux is recommended. The files 'Instructions_Linux.txt'
and 'Intructions_Windows.txt' provide the instructions to train and test the system. 

The model may take days to be completely trained. However, some parameters can be modified to considerably 
reduce the training time. These changes may also reduce the performance of the model. 

I tried that the code has as few differences as possible compared to the code I sent as part of my final
model submission. I mostly added comments and descriptions, but the code can be cleaned considerably. It 
has several lines that make calculations and produce files that were used in the development of the model 
but not in the final model.


EXTERNAL DATA:

The external data used are:

- The file /pythonScripts/PorterStemmer.py is an implementation of the Porter Stemmer algorithm downloaded 
  from http://tartarus.org/martin/PorterStemmer/python.txt
- The file /pythonScripts/correct2.py use code downloaded from http://norvig.com/spell-correct.html
- The file /pythonScripts/ae.txt was copied from /usr/share/dict/american-english.txt located in any 
  linux debian distribution.
- The file /pythonScripts/big.txt was downloaded from http://norvig.com/big.txt

ADDITIONAL FILES:

The script /AdditionalFiles/uniqueLexicon.py creates the lexicon for the spell corrector.
feat.py and label.py located in pythonScripts are the scripts used for labeling the training data.
'/TrainingCode/training/training_x_label.csv' are the files that contain 
the labels of the training data.

For any questions, feel free to contact me at luistp001@gmail.com
