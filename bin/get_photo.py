from flickr import get_urls
from downloader import download_images
import os
import argparse
from argparse import RawTextHelpFormatter
import time


def download(options):
	
	keywords = (options.k).strip().split(',')

	for key in keywords:

		print('Getting urls for', key)
		urls = get_urls(key, options.n)
		
		print('Downloading images for', key)
		path = os.path.join( options.o , key)

		download_images(urls, path)

def argsCheck():

	parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter)
	parser.add_argument('-k', metavar='keyword', 
			help='Keyword used to search for the photos.', required=True)

	parser.add_argument('-o', metavar='outdir', 
			help='Name of the output directory. Default: data/[keywords]', default = 'data',required=False)
	parser.add_argument('-n', metavar='number', 
			help='Number of photos to download. Default=10', default = 10, type=int, required=False)
	
	args = parser.parse_args()
	download(args)


if __name__=='__main__':

	start_time = time.time()

	argsCheck()

	print('Took', round(time.time() - start_time, 2), 'seconds')
