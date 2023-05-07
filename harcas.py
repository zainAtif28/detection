import urllib.request

url = "https://github.com/opencv/opencv/raw/master/data/haarcascades/haarcascade_eye.xml"
filename = "haarcascade_eye.xml"

urllib.request.urlretrieve(url, filename)
