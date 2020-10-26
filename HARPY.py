import argparse
import os
import extract_features as extract

dir_path = os.path.dirname(os.path.realpath(__file__))

parser = argparse.ArgumentParser(description='Project HARPY Preprocessor: Takes Joy JSON flow files, compiles all relevant features and maps MAC addresses to each flow from a separate CSV for classification.')
parser.add_argument('-t', action='store', type = int, default = 5, dest='parsed_interval', help='Time interval (integer value, in minutes).')
parser.add_argument('-p', action='store', type = str, default = dir_path, dest='parsed_path', help='App Path, must contain json_files and csv_files folders.')
parser.add_argument('-l', action='store', type = str, default = os.path.join(dir_path, "csv_files", "ListCSV.csv"), dest='parsed_MAClist', help='ListCSV.csv File.')
parser.add_argument('-o', action='store', type = str, default = os.path.join(dir_path, "csv_files"), dest='parsed_output', help='Output Path.')
args = parser.parse_args()

print(" ")
print("HARPY Path: " + args.parsed_path)
print(" ")
print("ListCSV.csv Directory: " + args.parsed_MAClist)
print(" ")
print("Output Path: " + args.parsed_output)
print(" ")

extract.mac_map(args.parsed_MAClist, extract.extract_features(args.parsed_path, args.parsed_interval), args.parsed_output)

