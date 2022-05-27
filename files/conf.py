'''
This is the Hawk configuration file. Change the configuration based on your specific needs.
'''

# API KEYS
SHODAN_API_KEY = 'Q4wtGdNmqnaQ267zzUb2rQztDRayEISI'
IPINFO_API_KEY = '8d53c2357c2a13'

# DEFAULT WORDLISTS
PASSWORDS_WORDLIST = 'files/txt/passwords.txt'
SUBDOMAINS_WORDLIST = 'files/txt/subdomains.txt'
DIRECTORIES_WORDLIST = 'files/txt/directories.txt'

# DEFAULT WIRELESS INTERFACE
DEFAULT_WIRELESS_INTERFACE = ''

# DNS MAPPING RECORDS DICTIONARY
DNS_MAPPING_RECORDS = {
    'www.google.com' : '185.199.109.153',
    'google.com' : '185.199.109.153'
}