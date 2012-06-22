import sys
import argparse
import xmlrpclib


# Command line options...
DOC_STRING = """
Hello!
This script uses a web service hosted by Kyle H. Ambert, at Oregon Health & Science University, 
to classify documents in terms of their likelihood of containing information related to gene 
expression and neurons. Named after the Icelandic word for neighbor, my system uses an algorithm
called kIGNN (k-Information-Scaled Nearest Neighbor) to arrive at probability estimates based on the 
content of an article's MEDLINE record or, in some cases, its fulltext (primarily only availble for 
Neuroscience publications in 2010). It only needs to know the PubMed ID you're interested in!
It can be used in two ways:

	[1] From the command line:  
		"python nagranni.py -pmid 19368830"
	[2] From another python script: 
		import nagranni
		nagranni(pmid=19368830)

That's it! If there are any problems, or if the server goes down for some reason, send me an email at
ambertk@gmail.com. I invite you to use this in your research, but be sure to cite and read the 
publication describing the kIGNN algorithm! 

	Ambert KH, Cohen AM. "k-Information Gain Scaled Nearest Neighbors: A Novel 
	Approach to Classifying Protein-Protein Interactions in Free-Text."
	IEEE/ACM Transactions on Computational Biology and Bioinformatics, 2012
"""
parser = argparse.ArgumentParser(description=DOC_STRING)
parser.add_argument("-pmid", "--pmid", type=str, help="Specify combiner. [Default]")

def nagranni(pmid):
	s = xmlrpclib.ServerProxy('http://skynet.ohsu.edu:8983')
	return s.getAnnotation(pmid)


if __name__ == "__main__":
	args = parser.parse_args()
	sys.stdout.write("{PMID}:\t{PR}\n".format(PMID=args.pmid, PR=nagranni(args.pmid)))