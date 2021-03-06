import urllib.request
import io

def get_robots(url):
    #check for existing backslash
    if url.endswith('/'):
        path = url
    else:
        path = url + "/"
    #request file
    req = urllib.request.urlopen(path + "robots.txt", data = None)
    data = io.TextIOWrapper(req, encoding="UTF-8")
    return data.read()
