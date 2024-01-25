from datasets_generations import save_cached_datasets_for_pelvicMR, save_cached_datasets_for_amos22
from create_amos22_labels_csv import add_file_paths_to_labels_csv_file


'''
This assumes the datasets follow the directory structure specified in the instructions.pdf,
Otherwise please change the paths in the config.py file accordingly.
'''

# when generating the datasets we used: random.seed(42)

# modify the amos22 meta csv to include images paths (this is used later)
add_file_paths_to_labels_csv_file()

# create cached datasets for the 1st dataset
save_cached_datasets_for_pelvicMR()

# create cached datasets for the 2nd dataset
save_cached_datasets_for_amos22()