from googlesearch import search
import requests

for x in search('site:BR.LINKEDIN.COM/IN/ + "@GMAIL.COM" + CEO + "SÃO PAULO"', tld='com', stop=200, lang='pt-BR'):
    r = requests.get(x)
    print(r.url)