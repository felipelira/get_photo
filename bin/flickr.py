


from flickrapi import FlickrAPI

KEY = 'c6a2c45591d4973ff525042472446ca2'
SECRET = '202ffe6f387ce29b'

SIZES = ["url_o", "url_k", "url_h", "url_l", "url_c"]  # in order of preference



def get_photos(image_tag):
	extras = ','.join(SIZES)
	flickr = FlickrAPI(KEY, SECRET)
	photos = flickr.walk(text=image_tag,  # it will search by image title and image tags
							extras=extras,  # get the urls for each size we want
							privacy_filter=1,  # search only for public photos
							per_page=50,
							sort='relevance')  # we want what we are looking for to appear first
	return photos


def get_urls(image_tag, max):

	photos = get_photos(image_tag)
	counter=0
	urls=[]

	for photo in photos:
		if counter < max:
			url = get_url(photo)  # get preffered size url
			if url:
				urls.append(url)
				counter += 1
			# if no url for the desired sizes then try with the next photo
		else:
			break
	
	return urls

def get_url(photo):
	for i in range(len(SIZES)):  # makes sure the loop is done in the order we want
		url = photo.get(SIZES[i])
		if url:  # if url is None try with the next size
			return url



def get_urls(image_tag, max):
	photos = get_photos(image_tag)
	counter=0
	urls=[]

	for photo in photos:
		if counter < max:
			url = get_url(photo)  # get preffered size url
			if url:
				urls.append(url)
				counter += 1
			# if no url for the desired sizes then try with the next photo
		else:
			break

	return urls
