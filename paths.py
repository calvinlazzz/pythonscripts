from pathlib import Path

root_dir = Path('files')
file_path = root_dir.glob('**/*.txt') 

for path in file_path:
    parent_folder = path.parts[-2]
    #print(parent_folder)
    new_filename = parent_folder + '-' + path.name
    new_filepath = path.with_name(new_filename)
    path.rename(new_filepath)