from dir import *
from domain import *
from ip import *
from nmap import *
from robots import *
from info import *

#check if directory is created.
#If not, it creates it
ROOT_DIR = 'companies'
create_directory(ROOT_DIR)

#main function
def main(name, url):
    domain_name = get_domain_name(url)
    ip = obtain_ip_address(url)
    port = get_nmap('-F', ip_address)
    robots_txt = get_robots(url)
    info = get_info(domain_name)
    create_report(name,full_url,domain_name, port, robots_txt, info)

#create a function that makes a report
def create_report(name, full_url, domain_name, port, robots_txt, info):
    project_dir = ROOT_DIR + '/' + name
    create_dir(project_dir)
    write_file(project_dir + '/full_url.txt', full_url)
    write_file(project_dir + '/domain_name.txt', domain_name)
    write_file(project_dir + '/port.txt', port)
    write_file(project_dir + '/robots_txt.txt', robots_txt)
    write_file(project_dir + '/info.txt', info)

#main('github', 'https://github.com/')
