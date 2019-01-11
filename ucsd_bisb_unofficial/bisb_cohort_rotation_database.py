#===============================================================================
# bisb_cohort_rotation_database.py
#===============================================================================

"""Class to facilitate handling the BISB Cohort Rotation google sheet"""




# Imports ======================================================================

import csv
import json
import sys
sys.path.pop(0)

from pytablewriter import MarkdownTableWriter




# Imports ======================================================================

class BISBCohortRotationDatabase:

    def __init__(self, csv_file_path: str):
        with open(csv_file_path, 'r') as f:
            self.header = f.readline().rstrip().split(',')[1:]
            self.dict = {name: data for name, *data, in csv.reader(f)}
    
    def add_column(self, column_name: str, d: dict):
        self.header.append(column_name)
        for name in d.keys():
            self.dict[name].append(d[name])
    
    def add_json(self, column_name, json_file_path: str):
        with open(json_file_path, 'r') as f:
            self.add_column(column_name, json.load(f))
    
    def markdown_table(self, *columns):
        writer = MarkdownTableWriter()
        writer.header_list = ['Name'] + (
            [self.header[col] for col in columns] if columns else self.header
        )
        writer.value_matrix = [
            [name] + (
                [self.dict[name][col] for col in columns]
                if columns else self.dict[name]
            )
            for name in sorted(self.dict.keys())
        ]
        return writer.dumps()




# Test =========================================================================

if __name__ == '__main__':
    print(BISBCohortRotationDatabase('/Users/anthonyaylward/Documents/web-projects/ucsd-bisb-unofficial/instance/protected/bisb-cohort-rotation-database.csv').markdown_table(1, 2))