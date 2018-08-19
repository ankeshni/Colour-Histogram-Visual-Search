
# USAGE
# python search.py --dataset images --index index.cpickle

# import the necessary packages
from pyimagesearch.searcher import Searcher
import numpy as np
import argparse
import cPickle
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required = True,
	help = "Path to the directory that contains the images we just indexed")
ap.add_argument("-i", "--index", required = True,
	help = "Path to where we stored our index")
args = vars(ap.parse_args())

# load the index and initialize our searcher
index = cPickle.loads(open(args["index"]).read())
searcher = Searcher(index)

# loop over images in the index -- we will use each one as
# a query image
for (query, queryFeatures) in index.items():
	# perform the search using the current query
	results = searcher.search(queryFeatures)

	# load the query image and display it
	path = query
	queryImage = cv2.imread(path,1)	
	cv2.imshow("Query", queryImage)
	print "query: %s" % (query)


	# initialize the two montages to display our results --
	# we have a total of 25 images in the index, but let's only
	# display the top 10 results; 5 images per montage, with
	# images that are 400x166 pixels
	montageA = np.zeros((queryImage.shape[0] * 5, queryImage.shape[1], 3))
	montageB = np.zeros((queryImage.shape[0] * 5, queryImage.shape[1], 3))

	# loop over the top ten results
	for j in xrange(0, 10):
		# grab the result (we are using row-major order) and
		# load the result image
		(score, imageName) = results[j]
		path = imageName
		result = cv2.imread(path,1)
		print "\t%d. %s : %.3f" % (j + 1, imageName, score)

		# check to see if the first montage should be used
		if j < 5:
			montageA[j * queryImage.shape[0]:(j + 1) * queryImage.shape[0], :] = result

		# otherwise, the second montage should be used
		else:
			montageB[(j - 5) * queryImage.shape[0]:((j - 5) + 1) * queryImage.shape[0], :] = result

	# show the results
	cv2.imshow("Results 1-5", montageA.astype('uint8'))
	cv2.imshow("Results 6-10", montageB.astype('uint8'))
	cv2.waitKey(0)


A seminar on Human Decision Making (At Chess) and Item-Response Theory by Dr Kenneth W. Regan, in which we used his large chess data in .aif format available on the UB Metallica server to try to find presence of hot hand in chess using my python scripts to drive a program created by him to get the data, parse the data generated by the program and use it to draw inferences from it.