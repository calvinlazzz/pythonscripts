from pathlib import Path
import zipfile

root_dir = Path('.')
destination_path = Path('destination')

for path in root_dir.glob('**/*.zip'):
    with zipfile.ZipFile(path, 'r') as zip_ref:
        zip_ref.extractall(destination_path / Path(path.stem))
        print(f'Extracted {path} to {destination_path / path.stem}')