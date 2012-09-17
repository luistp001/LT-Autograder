# LT Autograder. A system that automatically grades short answer essays.
# Copyright (C) 2012 Luis Tandalla

# This script predicts the score of the test essays using the trained Random Forests

correct_predictions <- function( prediction, training_now ) {
# This functions changes the predicted real value score to integer
# that falls between the minimum and maximum grade allowable.
prediction <- as.numeric(as.vector(prediction))
prediction <- round( prediction )
prediction [ which(prediction > max(training_now$f2.x))] <- max(training_now$f2.x)
prediction [ which(prediction < min(training_now$f2.x))] <- min(training_now$f2.x)

return (prediction)
}





library(randomForest)
actual <- 'model_53'

for (actual in c( 'model_53', 'model_53a' ) ) {
predtr <- data.frame()
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


rf <- models[[SET]] 



pte <- predict( rf, te)
pte2 <- pte
pte <- correct_predictions( pte, training_now )

predictionste <- data.frame( test_now[["Id"]] , pte )
predictionste2 <- data.frame( test_now[["Id"]] , pte2 )
predte <- rbind( predte, predictionste)
names(predictionste2) <- c('Id', 'essay_score')
#The following line saves the predicted real values
write.csv(predictionste2, file = paste('predictions/for_stack/test_', actual,'_', SET, '.csv', sep = '') , row.names = FALSE )

}

names(predte) <- c('Id', 'essay_score')
#The following line saves the predicted integer values
write.csv(predte, file = paste('predictions/', actual,'.csv', sep = '') , row.names = FALSE )

}
