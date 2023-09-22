try:
    from fake_useragent import UserAgent
    import requests, re, sys, json, argparse, cloudscraper, subprocess
    from multiprocessing.dummy import Pool
    from urllib3.exceptions import InsecureRequestWarning
    requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
except:
    print (f'[INFO] pip install -r requirements.txt')

action = subprocess.getoutput('python3 ./lib/themes/RFU/agritourismo.py -u https://pantheawine.com/')
if action != '':
    print (action)
else:pass