from socket import gethostbyname

def obtain_ip_address(url):
    return gethostbyname(url)

#print(obtain_ip_address("github.com"))
