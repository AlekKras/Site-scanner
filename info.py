import os

#analogy of Linux whois command
def get_info(url):
    command = "whois" + url
    process = os.popen(command)
    results = str(process.read())
    return results
#print(get_info("github.com"))
