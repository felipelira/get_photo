from progress.bar import Bar
import requests
import os
import sys
import time

def create_folder(path):
	if not os.path.isdir(path):
		os.makedirs(path)

def download_images(urls, path):
	create_folder(path)  # makes sure path exists
	n = 0
	for url in urls:
		n = n + 1
		extension = url.split("/")[-1].split('.')[-1] # get the image extension
		image_name = path.split('/')[-1] + '_' + str(n) + '.' + extension
		image_path = os.path.join(path, image_name)

		if not os.path.isfile(image_path):  # ignore if already downloaded
			response=requests.get(url,stream=True)

			with open(image_path,'wb') as outfile:
				outfile.write(response.content)
