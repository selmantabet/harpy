import extract_features as extract
import os
path = os.path.dirname(os.path.realpath(__file__))

extract.mac_map(os.path.join(path, "csv_files", "ListCSV.csv"), extract.extract_features(path, 7), os.path.join(path, "csv_files"))