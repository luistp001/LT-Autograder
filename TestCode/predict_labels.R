# LT Autograder. A system that automatically grades short answer essays.
# Copyright (C) 2012 Luis Tandalla

# This script predicts the probabilities that the essays of the test data
# have the answers (labels) or not.

library(nlme)
library(Boruta)
library(randomForest)
load( file = '../alreadySavedModelFiles/models_labels3.RData' )

ntrees = 501

sets <- c( 1:3, 5:10) # set 4 was not included in training
for (SET in sets){
print( paste('SET', SET) )

test_main <- read.csv(paste('test/test_', SET, '.csv', sep = '')) # It reads main file
test_w <- read.csv(paste('test/test_', SET, '_w.csv', sep = '')) # It reads file with counts of words
test_b <- read.csv(paste('test/test_', SET, '_b.csv', sep = '')) # It reads file with counts of bigrams
test_t <- read.csv(paste('test/test_', SET, '_t.csv', sep = '')) # It reads file with counts of trigrams
names(test_main)[2] <- c('f.x')


training_label <- read.csv(paste('training/training_', SET, '_label.csv', sep = ''))

label_predictions_test <- data.frame( test_main$Id )
names( label_predictions_test ) <- c( 'Id' )

label_probabilities_test <- data.frame( test_main$Id )
names( label_probabilities_test ) <- c( 'Id' )

print('starting')



for (LABEL in 0:( ncol(training_label) - 2 ) ){

training_main <- data.frame( cbind( training_label[["Id"]], training_label[[ paste('label_',LABEL, sep ='') ]] ) )
names(training_main) <- c('Id','LABEL') 
n_pos <- sum(training_main[['LABEL']]) # Number of essays that contain a certain label.
if ( n_pos > 3){ # The following is done only if more than 3 essays contain a certain label.
print( paste('label', LABEL) )

test_main <- data.frame( cbind( test_main[["Id"]] ) )
names(test_main) <- c( 'Id' ) 
test_now <- merge( test_main, test_w, by.x = 'Id', by.y = 'Id')
test_now <- merge( test_now, test_b, by.x = 'Id', by.y = 'Id')
test_now <- merge( test_now, test_t, by.x = 'Id', by.y = 'Id')
row.names(test_now) <- test_now$Id

rf_labels <- model_labels[[SET]][[LABEL+1]] # Loads Random Forest for the current set and answer

t_prob <- predict( rf_labels, newdata= test_now, type = 'prob') # It predicts the probabilities of having an answer
t_prob <- as.vector( t_prob[,2] )
t_pred <- as.numeric( as.vector( predict( rf_labels, newdata= test_now, type = 'response') ) )

test_predictions <- data.frame( cbind( test_now[['Id']], t_pred ) )
test_probabilities <- data.frame( cbind( test_now[['Id']], t_prob ) )
names(test_predictions) = c( 'Id' , paste( 'PRED_',LABEL, sep ='')  )
names(test_probabilities ) = c( 'Id' , paste( 'PROB_',LABEL, sep ='')  )

label_predictions_test <- merge( label_predictions_test, test_predictions, by.x = 'Id', by.y = 'Id')
label_probabilities_test <- merge( label_probabilities_test, test_probabilities, by.x = 'Id', by.y = 'Id')


}

}


# Probabilities and predictions are written in csv files
write.csv( label_predictions_test, file = paste('test/test_', SET, '_l_pred3.csv', sep = '') )
write.csv( label_probabilities_test, file = paste('test/test_', SET, '_l_prob3.csv', sep = '') )



}

