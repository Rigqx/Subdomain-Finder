import requests

domain = 'amongusfree.us' # Website

file = open('subdomain.txt', 'r')

content = file.read()
subdomains = content.splitlines()

for subdomain in subdomains:
	url = f'https://{subdomain}.{domain}'
	try:
		requests.get(url)
	except requests.ConnectionError:
		pass
	else:
		print("Discovered Subdomain: ", url)		