import argparse
import extract_features

parser = argparse.ArgumentParser(description='Define time interval, in minutes.')
parser.add_argument('-t', action='store', dest='parsed_interval', help='Time interval (in minutes)')
parser.add_argument('-p', action='store', dest='parsed_path', help='HARPY installation path)')
parser.add_argument('-m', action='store', dest='parsed_MAClist', help='MAC List directory')
parser.add_argument('-o', action='store', dest='parsed_output', help='Output path')
args = parser.parse_args()
timeInterval = int(args.parsed_interval)


extract_features_mapper.mac_map(args.parsed_MAClist, args.parsed_output, extract_features_mapper.extract_features(args.parsed_path, timeInterval))

