import os
import json
app_directory = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(app_directory, 'json_files', 'whois_record.json')) as f:
        whois_record = json.load(f)
    
print(type(whois_record))
#print(whois_record)
print(whois_record['74.125.31.105'])