# LT Autograder. A system that automatically grades short answer essays.
# Copyright (C) 2012 Luis Tandalla

# This script finds, independently, the relevant words, bigrams, and trigrams 
# needed to predict if an essay has a certain answer or not.

library(randomForest)
library(Boruta)

types <- c( 'w', 'b', 't')


formula_labels <- list()
sets <- c( 1:3, 5:10) # set 4 is not included because set 4 does
			# not have labels.
for (type in types){ 

for (SET in sets){

print( paste('SET', SET) )
formula_labels[[SET]] <- list()

training_main <- read.csv(paste('training/training_', SET, '.csv', sep = '')) # It reads main file
training_w <- read.csv(paste('training/training_', SET, '_w.csv', sep = '')) # It reads file with counts of words
training_b <- read.csv(paste('training/training_', SET, '_b.csv', sep = '')) # It reads file with counts of bigrams
training_t <- read.csv(paste('training/training_', SET, '_t.csv', sep = '')) # It reads file with counts of trigrams
names(training_main)[2:4] <- c('f.x','f2.x','f3.x')

training_label <- read.csv(paste('training/training_', SET, '_label.csv', sep = ''))

# Due to a bug, there are no labels for essay 22952, so this essay is eliminated from all training data.
training_main <- training_main[ which(training_main$Id != 22952), ]
training_w <- training_w[ which(training_w$Id != 22952), ]
training_b<- training_b[ which(training_b$Id != 22952), ]
training_t <- training_t[ which(training_t$Id != 22952), ]
training_label <- training_label[ which(training_label$Id != 22952), ]

print('starting')


for (LABEL in 0:( ncol(training_label) - 2 ) ){
print( paste('label', LABEL) )

training_main <- data.frame( cbind( training_label[["Id"]], training_label[[ paste('label_',LABEL, sep ='') ]] ) )
names(training_main) <- c('Id','LABEL') 
n_pos <- sum(training_main[['LABEL']]) # Number of essays that contain a certain label.
if ( n_pos > 3){ # The following is done only if more than 3 essays contain a certain label.


if (type == 'w'){
training_now <- merge( training_main, training_w, by.x = 'Id', by.y = 'Id')
}
if (type == 'b'){
training_now <- merge( training_main, training_b, by.x = 'Id', by.y = 'Id')
}
if (type == 't'){
training_now <- merge( training_main, training_t, by.x = 'Id', by.y = 'Id')
}
row.names(training_now) <- training_now$Id

form <- as.formula( 'as.factor(LABEL) ~ . - Id' )

mmtry <- max(floor(ncol(training_now)/3), 1) #Number of variables to try at each split
if (type == 'w'){
ntreep = 37 # Number of trees
maxRunsp = 150 # Maximum number of Random Forest to train.
}
if (type == 'b'){
ntreep = 37 # Number of trees
maxRunsp = 100 # Maximum number of Random Forest to train.
}
if (type == 't'){
ntreep = 31 # Number of trees
maxRunsp = 100 # Maximum number of Random Forest to train.
}

# It trains Boruta algorithm.
m_bor <- Boruta( form, data = training_now, ntree = ntreep, mtry = mmtry, maxRuns = maxRunsp, doTrace = 0 )
formula_labels[[SET]][[LABEL+1]] <- m_bor


}

}

}

# Relevant words, bigrams, and trigrams are saved
if (type == 'w'){
save( formula_labels, file = 'VariablesSelected/formulas_labels_w.RData' )
}
if (type == 'b'){
save( formula_labels, file = 'VariablesSelected/formulas_labels_b.RData' )
}
if (type == 't'){
save( formula_labels, file = 'VariablesSelected/formulas_labels_t.RData' )
}
}
