import argparse


parser = argparse.ArgumentParser(description='Define time interval, in minutes.')
parser.add_argument('-s', action='store', dest='parsed_interval', help='Time interval (in minutes)')
args = parser.parse_args()
print("-------Parsed Section (args)--------")
print(type(args))
print(args)
print("-------Investigate inside namespace--------")
print(type(args.parsed_interval))
print(args.parsed_interval)
print("-------Convert to int--------")
print(type(int(args.parsed_interval)))
print(int(args.parsed_interval))