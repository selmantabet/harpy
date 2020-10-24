import argparse


parser = argparse.ArgumentParser(description='Define time interval, in minutes.')
parser.add_argument('-s', action='store', dest='parsed_interval', help='Time interval (in minutes)')
args = parser.parse_args()
timeInterval = int(args.parsed_interval)

os.system("extract_features_mapper.py -s " + timeInterval)