import os
import json
import csv
from config import config

baseDir = config.baseDir
baseDirAmos22 = config.baseDirAmos22

'''
This code adds paths to the amos22 labels csv meta file
(that can be downloaded from the provided dataset: https://zenodo.org/records/7262581/files/labeled_data_meta_0000_0599.csv?download=1)

This code assumes the original csv file is located at 'baseDir' as it appears in the config.py file, and will
create the new csv file there as well.
'''

# helper function to add a column to the amos22 labels csv
def add_column_to_csv(orig_csv_path, new_csv_path, new_header, column):
    
  with open(orig_csv_path, 'r') as file:
      reader = csv.reader(file)
      header = next(reader)  # assuming first row is header
      rows = list(reader)
  
  header.append(new_header)
  
  for row in rows:
      index = int(row[0]) - 1
      row.append(column[index])
  
  with open(new_csv_path, 'w', newline='') as file:
      writer = csv.writer(file)
      writer.writerow(header)
      writer.writerows(rows)

def add_file_paths_to_labels_csv_file():

    amos22_json_filepath = os.path.join(baseDirAmos22,'dataset.json')

    with open(amos22_json_filepath, 'r') as file:
        python_dict = json.load(file)

    names_list = ['']*600
    labels_list = ['']*600

    for name_label in python_dict['training']:
        image_number = int(name_label['image'].split('_')[1].split('.')[0])-1

        names_list[image_number] = name_label['image'][1:]
        labels_list[image_number] = name_label['label'][1:]

    for name_label in python_dict['test']:
        image_number = int(name_label['image'].split('_')[1].split('.')[0])-1

        names_list[image_number] = name_label['image'][1:]
        labels_list[image_number] = 'None' # amos22 had no labels for test set

    for name_label in python_dict['validation']:
        image_number = int(name_label['image'].split('_')[1].split('.')[0])-1

        names_list[image_number] = name_label['image'][1:]
        labels_list[image_number] = name_label['label'][1:]

    orig_labels_csv_path = os.path.join(baseDir,'labeled_data_meta_0000_0599.csv')
    new_labels_csv_path = os.path.join(baseDir,'labeled_data_meta_0000_0599_with_paths.csv')


    add_column_to_csv(orig_labels_csv_path, new_labels_csv_path, 'image path', names_list)
    add_column_to_csv(new_labels_csv_path, new_labels_csv_path, 'labels path', labels_list)
