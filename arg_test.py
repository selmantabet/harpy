import argparse
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

parser = argparse.ArgumentParser(description='Define time interval, in minutes.')
parser.add_argument('-s', action='store', type = int, default = 5, dest='parsed_interval', help='Time interval (in minutes)')
parser.add_argument('-p', action='store', type = str, default = dir_path, dest='parsed_path', help='Path')
args = parser.parse_args()
print("-------Parsed Section (args)--------")
print(type(args))
print(args)
print("-------Investigate inside namespace--------")
print(type(args.parsed_interval))
print(args.parsed_interval)
print(type(args.parsed_path))
print("-------Convert--------")
print(type(int(args.parsed_interval)))
print(int(args.parsed_interval))
print(type(args.parsed_path))
print(args.parsed_path)