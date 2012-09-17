# LT Autograder. A system that automatically grades short answer essays.
# Copyright (C) 2012 Luis Tandalla

# This script trains and saves two Random Forests 
# to predict the scores of the essays.

ntrees = 501
correct <- function( train_data, double){
# If double is true, this functions doubles the training data.

  if (double){
    train_data2 <- train_data  # A copy of training data
    train_data2[,'f2.x'] <- train_data2[,'f3.x'] # It changes the values of the score
						  # given by the first grader to the 
						  # values of the score given by the second grader
    train_data <- rbind(train_data, train_data2) # It combines both copies of the training data
  }  
  return (train_data)
}

library(randomForest)
library(Boruta)
library(nlme)

for (actual in c('model_53', 'model_53a')){

models <- list()

load('VariablesSelected/selection_w.RData')
load('VariablesSelected/selection_b.RData')
load('VariablesSelected/selection_f.RData')
load('VariablesSelected/selection_lo.RData')


for (SET in 1:10){

print ( paste( 'training', SET) )

training_main <- read.csv(paste('training/training_', SET, '.csv', sep = '')) # It reads main training file
training_f <- read.csv(paste('training/training_', SET, '_f.csv', sep = '')) # It reads file with answers
training_w <- read.csv(paste('training/training_', SET, '_w.csv', sep = '')) # It reads file with bag of words
training_b <- read.csv(paste('training/training_', SET, '_b.csv', sep = '')) # It reads file with bag of bigrams
if (SET != 4){
training_lo <- read.csv(paste('training/training_', SET, '_l_prob3.csv', sep = '')) #It reads file with labels
training_lo <- training_lo[,2:ncol(training_lo) ]
}
if (SET == 4){ #set 4 does not have labels.
training_lo <- training_f
}

# Due to a bug, there are no labels for essay 22952, so this essay is eliminated from all training data.
training_main <- training_main[ which(training_main$Id != 22952), ]
training_f <- training_f[ which(training_f$Id != 22952), ]
training_w <- training_w[ which(training_w$Id != 22952), ]
training_b<- training_b[ which(training_b$Id != 22952), ]
training_lo <- training_lo[ which(training_lo$Id != 22952), ]

names(training_main)[2:4] <- c('f.x','f2.x','f3.x')
# The following lines combine the four data frames.
training_now <- merge( training_main, training_b, by.x = 'Id', by.y = 'Id')
training_now <- merge( training_now, training_w, by.x = 'Id', by.y = 'Id')
training_now <- merge( training_now, training_f, by.x = 'Id', by.y = 'Id')

if (SET != 4){
training_now <- merge( training_now, training_lo, by.x = 'Id', by.y = 'Id')
}
row.names(training_now) <- training_now$Id
tr <- training_now

# The following lines gets the relevant variables selected for words, bigrams, answer, and labels.
bors <- variables_selected_w[[SET]]
bors <- TentativeRoughFix( bors )
form <- getConfirmedFormula(bors)
bors2 <- variables_selected_b[[SET]]
form2 <- getConfirmedFormula(bors2)
borsf <- variables_selected_f[[SET]]
formf <- getNonRejectedFormula(borsf)
borslo <- variables_selected_lo[[SET]]
formlo <- getNonRejectedFormula(borslo)

form <- asOneFormula( form, form2, formf, formlo, omit = 'f2.x') # It combines all the variables.
form_s <- all.vars(form)
form <- as.formula( paste( 'f2.x', '~', paste( form_s, collapse= '+') ) )

double_data = TRUE
tr2 <- correct(tr, double_data) # It doubles the training data

#It trains rf
rf <- randomForest( form, data = tr2, ntree = ntrees, do.trace = FALSE, importance = TRUE)
models[[SET]] <- rf
}

save( models, file = paste( '../newTrainedModelFiles/models_', actual, '.RData', sep="" ) )

}
