import os

#basic Linux nmap command
def get_nmap(options, ip):
    command = 'nmap' + options + " " + ip
    process = os.popen(command)
    results = str(process.read())
    return results
#paste any ip address
#print(get_nmap('185.60.216.35'))
