from tld import get_tld

#create a function that return domain's name
def get_domain_name(url):
    domain_name = get_tld(url)
    return domain_name

print(get_domain_name("https://github.com"))
