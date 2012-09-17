# LT Autograder. A system that automatically grades short answer essays.
# Copyright (C) 2012 Luis Tandalla

# This script averages the four predictions calculated by the Random Forests
# and the Gradient Boosting Machines. The rounded value of those numbers are the final 
# predicted scores of the Autograder.

correct_predictions_s <- function( prediction, training_now ) {
# This functions changes the predicted real value score to integer
# that falls between the minimum and maximum grade allowable.

prediction <- as.numeric(as.vector(prediction))
prediction <- round( prediction )
prediction [ which(prediction > max(training_now$score))] <- max(training_now$score)
prediction [ which(prediction < min(training_now$score))] <- min(training_now$score)

return (prediction)
}

AvePred <- data.frame()

for (SET in 1:10){
labels <- read.csv(paste('training/training_', SET, '.csv', sep = ''))
names(labels)[3] <- 'score'
actual = 'model_60'
test_1 <- read.csv (paste('predictions/for_stack/test_', actual,'_', SET, '.csv', sep = '')  )
actual = 'model_62'
test_2 <- read.csv (paste('predictions/for_stack/test_', actual,'_', SET, '.csv', sep = '')  )
actual = 'model_53'
test_3 <- read.csv (paste('predictions/for_stack/test_', actual,'_', SET, '.csv', sep = '')  )
actual = 'model_53a'
test_4 <- read.csv (paste('predictions/for_stack/test_', actual,'_', SET, '.csv', sep = '')  )

test <- test_1
test[,2] = test_1[,2] + test_2[,2] + test_3[,2] + test_4[,2]
test[,2] = correct_predictions_s( test[,2]/4, labels ) 

AvePred <- rbind(AvePred, test)

}

names(AvePred) <- c('Id', 'essay_score')
write.csv(AvePred, file = paste('finalModel/finalPrediction.csv', sep = '') , row.names = FALSE )
