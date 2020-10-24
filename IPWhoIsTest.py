from ipwhois import IPWhois
from pprint import pprint

ip_query = IPWhois('8.8.8.8')
RDAP = ip_query.lookup_rdap(depth=1)
print(type(RDAP))
print(RDAP["asn_description"])
pprint(RDAP)