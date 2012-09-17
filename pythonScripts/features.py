#LT Autograder. A system that automatically grades short answer essays.
#Copyright (C) 2012 Luis Tandalla

# This script searches if an essay has the answers needed for a high score.

from features1 import *
from features2 import *
from features3 import *
from features4 import *
from features5 import *
from features6 import *
from features7 import *
from features8 import *
from features9 import *
from features10 import *

def feature(**kwargs):
	
	Id = kwargs['Id'] 			
	set = kwargs['set'] 		
	if int(Id) % 100 == 0: print  Id
	# It calls a different function for each set.
	if set == 1:			return feature1(**kwargs)
	elif set == 2:			return feature2(**kwargs)
	elif set == 3:			return feature3(**kwargs)
	elif set == 4:			return feature4(**kwargs)
	elif set == 5:			return feature5(**kwargs)
	elif set == 6:			return feature6(**kwargs)
	elif set == 7:			return feature7(**kwargs)
	elif set == 8:			return feature8(**kwargs)
	elif set == 9:			return feature9(**kwargs)
	elif set == 10:			return feature10(**kwargs)
	else: 
		return [0], fi, fi2


