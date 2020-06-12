import requests
#the domain to scan for subdomains
domain = 'google.com'
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
