
# class base:
#     def __init__ (self):
#         self.name = 'tunde'
#     def print(self):
#         print('hello this', self.name)

# class myown(base):
#     def __init__ (self):
#         base. __init__ (self)
#         self.name = 'seyi'

# myown()
import requests
#the domain to scan for subdomains
domain = 'annashut.com'
# read all subdomain
file = open('subdomain.txt')
# read all content
content = file.read()
# split by new line
subdomains = content.splitlines()
# loop through
for subdomain in subdomains:
    # construct the url
    url = f"http://{subdomain}.{domain}"
    try:
        # if this raises an error that means the subdomain does not exist
        requests.get(url)
    except requests.ConnectionError:
        # if the subdomain does not exist, just pass, print nothing
        pass
    else:
        print("[+] Discovered subdomain:", url)
