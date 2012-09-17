# LT Autograder. A system that automatically grades short answer essays.
# Copyright (C) 2012 Luis Tandalla

# This script predicts the score of the test essays using the trained Gradient Boosting Machines.

correct_predictions <- function( prediction, training_now ) {
# This functions changes the predicted real value score to integer
# that falls between the minimum and maximum grade allowable.
prediction <- as.numeric(as.vector(prediction))
prediction <- round( prediction )
prediction [ which(prediction > max(training_now$f2.x))] <- max(training_now$f2.x)
prediction [ which(prediction < min(training_now$f2.x))] <- min(training_now$f2.x)

return (prediction)
}

library(gbm)
library(nlme)


actual <- 'model_60'

for(actual in c('model_60','model_62')){
predte <- data.frame()
load( file = paste( '../alreadySavedModelFiles/models_', actual, '.RData', sep="" ) ) 

for (SET in 1:10){

print ( paste( 'training', SET) )

training_main <- read.csv(paste('training/training_', SET, '.csv', sep = ''))
names(training_main)[2:4] <- c('f.x','f2.x','f3.x')
training_now <- training_main

test_main <- read.csv(paste('test/test_', SET, '.csv', sep = ''))
test_f <- read.csv(paste('test/test_', SET, '_f.csv', sep = ''))
test_w <- read.csv(paste('test/test_', SET, '_w.csv', sep = ''))
test_b <- read.csv(paste('test/test_', SET, '_b.csv', sep = ''))
if (SET != 4){
test_le <- read.csv(paste('test/test_', SET, '_l_pred3.csv', sep = ''))
test_lo <- read.csv(paste('test/test_', SET, '_l_prob3.csv', sep = ''))
test_le <- test_le[,2:ncol(test_le) ]
test_lo <- test_lo[,2:ncol(test_lo) ]
}
if (SET == 4){
test_le <- test_f
test_lo <- test_f
}

names(test_main)[2] <- c('f.x')
test_now <- merge( test_main, test_b, by.x = 'Id', by.y = 'Id')
test_now <- merge( test_now, test_w, by.x = 'Id', by.y = 'Id')
test_now <- merge( test_now, test_f, by.x = 'Id', by.y = 'Id')
test_now <- merge( test_now, test_le, by.x = 'Id', by.y = 'Id')
test_now <- merge( test_now, test_lo, by.x = 'Id', by.y = 'Id')
row.names(test_now) <- test_now$Id
te <- test_now
te[,'f3.x'] = 1

pte <- te$f2.x
pte <- correct_predictions( pte, training_now )


gbmModel <- models[[SET]][[1]]
best.iter <- models[[SET]][[2]]

ntrees = best.iter
pte <- predict(gbmModel, te, n.trees = best.iter)
prte <- data.frame(test_now[['Id']],pte)
names(prte) <- c('Id', 'essay_score')
#The following line saves the predicted real values
write.csv(prte, file = paste('predictions/for_stack/test_', actual,'_', SET, '.csv', sep = '') , row.names = FALSE )
pte <- correct_predictions( pte, training_now )
predictionste <- data.frame( test_now[["Id"]] , pte )
predte <- rbind( predte, predictionste)
}
names(predte) <- c('Id', 'essay_score')
#The following line saves the predicted integer values
write.csv(predte, file = paste('predictions/', actual,'.csv', sep = '') , row.names = FALSE )

}
