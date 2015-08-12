import ctypes
from urllib import urlretrieve
import urllib
import urllib2
import re
from PIL import Image

def comicURL():
	response = urllib2.urlopen('http://xkcd.com/')
	html = response.read()
	matchObj = re.search( r'(imgs\.xkcd\.com/comics/[A-z_]+)', html, re.M|re.I)
	if matchObj:
   		print "matchObj.group() : ", matchObj.group()
   		return matchObj.group()
	else:
   		print "No match!!"

def getImage(url):
	f = open('image.png','wb')
	f.write(urllib.urlopen("http://" + url + ".png").read())
	f.close()

def convert(image):
	im = Image.open(image)
	im.save('image.jpg')


getImage(comicURL())
convert("image.png")

SPI_SETDESKWALLPAPER = 20 
ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, "image.jpg" , 0)