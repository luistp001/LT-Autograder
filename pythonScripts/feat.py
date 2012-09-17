# LT Autograder. A system that automatically grades short answer essays.
# Copyright (C) 2012 Luis Tandalla

# This script contains some predefined answers for some of the sets.
# This script is called from label.py
import collections, re, math


def feat():

	feat = collections.defaultdict(lambda: [] )
	feat[6] =[]
	feat[6].append( 'Selective permeability allow certain substances to move across.' )	
	feat[6].append( 'Passive transport from an area of higher concentration to lower concentration.' )
	feat[6].append( 'Osmosis is the diffusion of water across the cell membrane.' )
	feat[6].append( 'Facilitated diffusion occurs when the membrane controls the pathway for a particle to enter or leave a cell.' )
	feat[6].append( 'Active transport occurs when a cell uses energy to move a substance across the cell membrane, and/or a substance moves from an area of low to high concentration, or against the concentration gradient.' )
	feat[6].append( 'Pumps are used to move charged particles like sodium and potassium ions through membranes using energy and carrier proteins.' )
	feat[6].append( 'Membrane-assisted transport occurs when the membrane of the vesicle fuses with the cell membrane forcing large molecules out of the cell as in exocytosis.' )
	feat[6].append( 'Membrane-assisted transport occurs when molecules are engulfed by the cell membrane as in endocytosis.' )
	feat[6].append( 'Membrane-assisted transport occurs when vesicles are formed around large molecules as in phagocytosis.' )
	feat[6].append( 'Membrane-assisted transport occurs when vesicles are formed around liquid droplets as in pinocytosis.' )
	feat[6].append( 'Protein channels or channel proteins allow for the movement of specific molecules or substances into or out of the cell.' )
	
	feat[7].append(	'thoughful cainr considered')
	feat[7].append(	'help famili')
	feat[7].append(	'responsability')
	feat[7].append(	'understandable wisdom matur')
	feat[7].append(	'hard worker')
	feat[7].append(	'optimist')
	feat[7].append(	'giving person')
	feat[7].append(	'respect')
	feat[7].append(	'determined')
	feat[7].append(	'worri')
	feat[7].append(	'motherli')
	feat[7].append(	'not tell the truth')
	feat[7].append(	'understand trip of papa')
	feat[7].append(	'understand everyone has their part to do')
	feat[7].append(	'pai for her brother')
	feat[7].append(	'she fell asleep while working on her essai')
	feat[7].append(	'comfort her sister')
	feat[7].append(	'pai wai, keep up school work, cook for famili')
	feat[7].append(	'optimist behavior after talking with aunt')
	feat[7].append(	'paul will do well in college')
	feat[7].append(	'ask sister if she is ok')



	feat[8].append(	'both could not read' )
	feat[8].append(	'try hard inspire')
	feat[8].append(	'empathi for mr leopard')
	feat[8].append(	'shock ')
	feat[8].append(	'why did you not tell me about thi')
	feat[8].append(	'help mr leoanrd becaus ehe help him')
	feat[8].append(	'walk back toward school, its time to start your train')
	feat[8].append(	'call to read aloud')
	feat[8].append(	'suspicious')
	feat[8].append(	'track start that went to college but flunk out')

	feat[9].append(	'shock statement')
	feat[9].append(	'introduction' )
	feat[9].append(	'differ headings')
	feat[9].append(	'explain space junk' )
	feat[9].append(	'crash course')
	feat[9].append(	'small pieces')
	feat[9].append(	'danger')
	feat[9].append(	'recommendation')

	feat[10].append(	'black')
	feat[10].append(	'warmer' )
	feat[10].append(	'result warmest' )
	feat[10].append(	'dark gray')
	feat[10].append(	'little warmer' )
	feat[10].append(	'almost warmest' )
	feat[10].append(	'light gray')
	feat[10].append(	'little cooler' )
	feat[10].append(	'almost coolest' )
	feat[10].append(	'white')
	feat[10].append(	'cooler' )
	feat[10].append(	'result coolest' )

	feat[1].append(	'amount of vinegar')
	feat[1].append(	'size of container' )
	feat[1].append(	'type of container' )
	feat[1].append(	'type of sample')
	feat[1].append(	'size of marble' )
	feat[1].append(	'type of vinegar' )
	feat[1].append(	'location of the samples')
	feat[1].append(	'surface area or shape' )
	feat[1].append(	'time for rinsing' )
	feat[1].append(	'rooom temperature')
	feat[1].append(	'how to rinse' )
	feat[1].append(	'are the containers closed' )
	feat[1].append(	'are fulli submerged' )
	feat[1].append(	'type climate' )

	feat[2].append(	'b stretch the most' )
	feat[2].append(	'type a is stronger' )
	feat[2].append(	'a stretch the least' )
	feat[2].append(	'result not valid' )
	feat[2].append(	'more trials' )
	feat[2].append(	'number of weights' )
	feat[2].append(	'same length ?' )
	feat[2].append(	'amount of plastic' )
	feat[2].append(	'original length' )
	feat[2].append(	'where the clamp' )
	feat[2].append(	'same thickness' )
	feat[2].append(	'how much height' )

	feat[4].append(	'spread fast' )
	feat[4].append(	'major threat' )
	feat[4].append(	'threat to the environment' )
	feat[4].append(	'invade the everglade, area, property' )
	feat[4].append(	'proliferate' )
	feat[4].append(	'new environment, climate' )

	feat[5].append(	'mRNA exits nucleus via nuclear pore.' )
	feat[5].append(	'mRNA travels through the cytoplasm to the ribosome or enters the rough endoplasmic reticulum.' )
	feat[5].append(	'mRNA bases are read in triplets called codons (by rRNA).' )
	feat[5].append(	'tRNA carrying the complementary (U=A, C+G) anticodon recognizes the complementary codon of the mRNA.' )
	feat[5].append(	'The corresponding amino acids on the other end of the tRNA are bonded to adjacent tRNAs amino acids.' )
	feat[5].append(	'A new corresponding amino acid is added to the tRNA.' )
	feat[5].append(	'Amino acids are linked together to make a protein beginning with a START codon in the P site (initiation).' )
	feat[5].append(	'Amino acids continue to be linked until a STOP codon is read on the mRNA in the A site (elongation and termination).' )


	# With set 6, indexes of the answers were changed so that 
	# they have the same indexes as the regular expressions.
	# However, this is not necessary. They are only included
	# because they were part of the development phase.
	fmatch = {}
	fmatch[6] = {}
	fmatch[6][4] = [ 0 ]
	fmatch[6][1] = [ 1, 3 ]
	fmatch[6][5] = [ 2 ]
	fmatch[6][2] = [4]
	fmatch[6][3] = [ 5]
	fmatch[6][7] = [6]
	fmatch[6][0] = [7]

	return feat, fmatch


