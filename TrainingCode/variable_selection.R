# LT Autograder. A system that automatically grades short answer essays.
# Copyright (C) 2012 Luis Tandalla

# This script finds, independently, the relevant words, bigrams, answers, and predictions 
# of labels needed to predict the score of an essay

library(randomForest)
library(Boruta)

maxRunp_fw = 150 # Maximum number of Random Forest to run for answers and words
maxRunp_b = 70 	 # Maximum number of Random Forest to run for bigrams
ntrees = 151
 
sets <- 1:10

types <- c('f', 'w', 'b', 'lo')

for (type in types){

variables_selected = list()

for (SET in sets){

print ( paste( 'training', SET) )

training_main <- read.csv(paste('training/training_', SET, '.csv', sep = ''))
training_f <- read.csv(paste('training/training_', SET, '_f.csv', sep = ''))
training_w <- read.csv(paste('training/training_', SET, '_w.csv', sep = ''))
training_b <- read.csv(paste('training/training_', SET, '_b.csv', sep = ''))
if (SET != 4){
training_lo <- read.csv(paste('training/training_', SET, '_l_prob3.csv', sep = ''))
training_lo <- training_lo[,2:ncol(training_lo) ]
}
if (SET == 4){
training_lo <- training_f
}

# Due to a bug, there are no labels for essay 22952, so this essay is eliminated from all training data.
training_main <- training_main[ which(training_main$Id != 22952), ]
training_f <- training_f[ which(training_f$Id != 22952), ]
training_w <- training_w[ which(training_w$Id != 22952), ]
training_b<- training_b[ which(training_b$Id != 22952), ]
training_lo <- training_lo[ which(training_lo$Id != 22952), ]

names(training_main)[2:4] <- c('f.x','f2.x','f3.x')
maxRunsp = maxRunp_fw
if (type == 'f'){
training_now <- merge( training_main, training_f, by.x = 'Id', by.y = 'Id')
}
if (type == 'w'){
training_now <- merge( training_main, training_w, by.x = 'Id', by.y = 'Id')
}
if (type == 'b'){
training_now <- merge( training_main, training_b, by.x = 'Id', by.y = 'Id')
maxRunsp = maxRunp_b
}
if (type == 'lo'){
training_now <- merge( training_main, training_lo, by.x = 'Id', by.y = 'Id')
}
row.names(training_now) <- training_now$Id

# It trains Boruta algorithm.
bor <- Boruta( f2.x ~ . -f.x - f3.x - Id , data = training_now , doTrace=0, ntree = ntrees, maxRuns = maxRunsp )
variables_selected[[SET]] <-bor

}

#Relevant words, bigrams, answers, and predictions 
# of labels
if (type == 'f'){
variables_selected_f <- variables_selected
save(variables_selected_f, file = 'VariablesSelected/selection_f.RData')
}
if (type == 'w'){
variables_selected_w <- variables_selected
save(variables_selected_w, file = 'VariablesSelected/selection_w.RData')
}
if (type == 'b'){
variables_selected_b <- variables_selected
save(variables_selected_b, file = 'VariablesSelected/selection_b.RData')
}
if (type == 'lo'){
variables_selected_lo <- variables_selected
save(variables_selected_lo, file = 'VariablesSelected/selection_lo.RData')
}

}
