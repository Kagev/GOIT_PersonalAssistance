
from methods.imports import os, re, shutil, Path

# ----------SETTINGS----------


IMAGES = ['JPEG', 'PNG', 'JPG', 'SVG']
VIDEO = ['AVI', 'MP4', 'MOV', 'MKV']
DOCUMENTS = ['DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX']
AUDIO = ['MP3', 'OGG', 'WAV', 'AMR']
ARCHIVES = ['ZIP', 'TAR']
FOLDERS = ['IMAGES', 'VIDEO', 'DOCUMENTS', 'AUDIO', 'ARCHIVES']


# ----------METAGRAPHY----------


CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
MAP = {}


for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    MAP.update({ord(c): l, ord(c.upper()): l.upper()})


# ----------TOOLS----------


path_folders = []
path_files = []


def get_extension(file: str) -> str:
        match = re.search(r'\.\w{1,2}\w{1,2}$', file)
        if match:
            return match[0][1:]
        else:
            return None
        

def get_name(file: str) -> str:
    return re.sub(r'\.\w{3,4}$', '', file)


def normalize(file: str) -> str:
    if get_extension(file):
        file_new_name = re.sub(r'\W', '_', get_name(file).translate(MAP))
        return f"{file_new_name}.{get_extension(file)}"
    else:
        return re.sub(r'\W', '_', get_name(file).translate(MAP))


def scan(folder: Path) -> None:
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in FOLDERS:
                path_folders.append(item)
                scan(item)
            else:
                continue
        else:
            path_files.append(item)


def handle_file(file_path: Path, target_folder: Path) -> None:
    target_folder.mkdir(exist_ok=True, parents=True)
    file_path.replace(target_folder / normalize(file_path.name))


def handle_archive(file_path: Path, target_folder: Path) -> None:
    target_folder.mkdir(exist_ok=True, parents=True)
    path_to_unpack = target_folder / normalize(get_name(file_path.name)) / get_extension(file_path.name)
    try:
        shutil.unpack_archive(file_path, path_to_unpack)
    except shutil.ReadError:
       print('Unpack error')
    file_path.unlink()


def handle_folder(folder: Path) -> None:
    if not os.listdir(folder):
        try:
            folder.rmdir()
        except OSError:
            print(f'{folder} removing error')
    else:
        os.rename(folder, Path(str(folder).translate(MAP)))


# ----------MAIN----------

archives = []
audio = []
documents = []
images = []
video = []
other = []
extensions = set()
unknown_extensions = set()

def clean(work_folder: Path) -> None:
    scan(work_folder)
    for file in path_files:
        if get_extension(file.name):
            if get_extension(file.name).upper() in ARCHIVES:
                extensions.add(get_extension(file.name))
                archives.append(file.name)
                handle_archive(file, work_folder / 'Sorted' / 'ARCHIVES')

            elif get_extension(file.name).upper() in AUDIO:
                extensions.add(get_extension(file.name))
                audio.append(file.name)
                handle_file(file, work_folder / 'Sorted' / 'AUDIO')

            elif get_extension(file.name).upper() in DOCUMENTS:
                extensions.add(get_extension(file.name))
                documents.append(file.name)
                handle_file(file, work_folder / 'Sorted' / 'DOCUMENTS') 

            elif get_extension(file.name).upper() in IMAGES:
                extensions.add(get_extension(file.name))
                images.append(file.name)
                handle_file(file, work_folder / 'Sorted' / 'IMAGES') 

            elif get_extension(file.name).upper() in VIDEO:
                extensions.add(get_extension(file.name))
                video.append(file.name)
                handle_file(file, work_folder / 'Sorted' / 'VIDEO') 

            else:
                unknown_extensions.add(get_extension(file.name))
        else:
            continue
    
    for folder in path_folders:
            handle_folder(folder)
    
    print('-' * 50)
    print(f'ARCHIVES {archives}')
    print('-' * 50)
    print(f'AUDIO {audio}')
    print('-' * 50)
    print(f'DOCUMENTS {documents}')
    print('-' * 50)
    print(f'IMAGES {images}')
    print('-' * 50)
    print(f'VIDEO {video}')
    print('-' * 50)
    print(f'REGISTER_EXTENTIONS {extensions}')
    print('-' * 50)
    print(f'UNKNOWN_EXTENSIONS {unknown_extensions}')
    print('-' * 50)

def main() -> None:
    while True:
        user_input = input()
        