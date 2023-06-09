import re 
import requests
from io import StringIO

domains_lists = [
    'https://adaway.org/hosts.txt',
    'https://bitbucket.org/ethanr/dns-blacklists/raw/8575c9f96e5b4a1308f2f12394abd86d0927a4a0/bad_lists/Mandiant_APT1_Report_Appendix_D.txt',
    'https://gitlab.com/quidsup/notrack-blocklists/raw/master/notrack-malware.txt',
    'https://hostfiles.frogeye.fr/firstparty-trackers-hosts.txt',
    'https://osint.digitalside.it/Threat-Intel/lists/latestdomains.txt',
    'https://pgl.yoyo.org/adservers/serverlist.php?hostformat=hosts&showintro=0&mimetype=plaintext',
    'https://phishing.army/download/phishing_army_blocklist_extended.txt',
    'https://raw.githubusercontent.com/anudeepND/blacklist/master/adservers.txt',
    'https://raw.githubusercontent.com/bigdargon/hostsVN/master/hosts',
    'https://raw.githubusercontent.com/crazy-max/WindowsSpyBlocker/master/data/hosts/spy.txt',
    'https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Alternate%20versions%20Anti-Malware%20List/AntiMalwareHosts.txt',
    'https://raw.githubusercontent.com/FadeMind/hosts.extras/master/add.2o7Net/hosts',
    'https://raw.githubusercontent.com/FadeMind/hosts.extras/master/add.Risk/hosts',
    'https://raw.githubusercontent.com/FadeMind/hosts.extras/master/add.Spam/hosts',
    'https://raw.githubusercontent.com/FadeMind/hosts.extras/master/UncheckyAds/hosts',
    'https://raw.githubusercontent.com/PolishFiltersTeam/KADhosts/master/KADhosts.txt',
    'https://raw.githubusercontent.com/Spam404/lists/master/main-blacklist.txt',
    'https://raw.githubusercontent.com/Te-k/stalkerware-indicators/master/generated/hosts',
    'https://s3.amazonaws.com/lists.disconnect.me/simple_ad.txt',
    'https://s3.amazonaws.com/lists.disconnect.me/simple_malvertising.txt',
    'https://urlhaus.abuse.ch/downloads/hostfile/',
    'https://v.firebog.net/hosts/AdguardDNS.txt',
    'https://v.firebog.net/hosts/Admiral.txt',
    'https://v.firebog.net/hosts/Easylist.txt',
    'https://v.firebog.net/hosts/Easyprivacy.txt',
    'https://v.firebog.net/hosts/Prigent-Ads.txt',
    'https://v.firebog.net/hosts/Prigent-Crypto.txt',
    'https://v.firebog.net/hosts/static/w3kbl.txt',
    'https://zerodot1.gitlab.io/CoinBlockerLists/hosts_browser'
]

for domains_list in domains_lists:
    r = requests.get(domains_list)
    stri = StringIO(r.text)
    header = '-- BEGIN: {}\npolicy.add(\n    policy.suffix(policy.DENY,\n        policy.todnames({{'.format(domains_list)
    footer = '\n        }})\n    )\n)\n-- END: {}'.format(domains_list)
    print(header)
    first = True
    while True:
        nl = stri.readline()
        if nl:
            if not re.search('^#.*', nl) and not re.search('^\n$', nl) and not re.search('localhost', nl.lower()):
                if first:
                    print('            \'{}\''.format(re.sub('[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+', '', nl).strip()), end='')
                    first = False
                else:
                    print(',\n            \'{}\''.format(re.sub('[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+', '', nl).strip()), end='')
        else:
            break
    print(footer)
