#          
#
#             PROJECT HARPY - Backend Service - HBKU Final Year Project
#
#    Data Collection, Preprocessing and Launcher Developer: Selman Tabet
#    Machine Learning Developer: Mohamed Amara
#    Frontend and App Developer: Omar Elshal
#    Supervisor: Dr. Ala Al-Fuqaha
#
#

# ---- Prerequisite file structure ----
# - Harpy directory                 // Main app directory (MANDATORY, most essential argument to be provided via CLI unless already cd'd to it)
# |_  /pcap_files/                  // Capture files (MANDATORY - for Joy Tool Shell Script)
# |_  /csv_files/                   // (Default) Output of the feature extraction script (MANDATORY)
# |     |_  ListCSV.csv             // List of MAC addresses (Optional iff the absolute path was provided via CLI)
# |_  /json_files/                  // Where Joy JSON output is stored (MANDATORY)
#       |_  whois_record.json       // For RDAP requests in extract_features.py (MANDATORY)
#
# DO NOT RUN UNLESS THE MANDATORY FILES AND FOLDERS IN THE FILE TREE ARE COMPLETE
#
#
#
# Changelog: HARPY V4.0 - Machine Learning and Frontend Update.
#
# [CODE]
#   - Added Frontend code (using React Native framework).
#   - Added Machine Learning Module for training and classification.
# 
#
# [ROADMAP]
#
# * Next Beta branch, in anticipation of new datasets: 
#     ~ Have harpy.py output the number of MACs in ListCSV.csv, this would be handed over to extract_features as an argument that goes directly
#     to the device_co for loop to avoid hardcoding values.
#     ~ For the same reason previously stated, the number of capture files needs to be calculated so that the value in the days_co for loop may
#     be dynamically adjusted for the files in /pcap_files/ directory.
#     ~ New Python script may be developed to call cisco/joy for all MACs in ListCSV.csv, but this would limit the execution environment to POSIX
#     due to the potential usage of os.system(joy <args>), unless the user has "joy" cmd(let) somehow defined on their NT system.
#     ~ In the event that the WHOIS Record was found to be outdated, it shall be cleared and rebuilt to address concerns with outdated registries.
#
#

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

