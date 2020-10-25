from ipwhois import IPWhois
from pprint import pprint

try:
    print("Started...")
    ip_query = IPWhois('8.8.8.8')
    print("IPWHOis setup...")
    RDAP = ip_query.lookup_rdap(depth=1, rate_limit_timeout = 10)
    print("Lookup successful...")
    print(type(RDAP))
    print(RDAP["asn_description"])
    pprint(RDAP)
except:
    print("Failed.")