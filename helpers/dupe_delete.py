# Delete duplicates

from hashlib import md5
from os import path, getcwd, remove, walk
from base64 import b64encode

def get_file_list(directory) :
    file_list = []
    for root, dirs, files in walk(directory) :
        file_list.extend([path.join(root, file) for file in files])
    return file_list

def hash_file(filepath) :
    with open(filepath, 'rb') as f:
        # Hash file
        file_hash = md5(f.read()).digest()
        return b64encode(file_hash).decode()            

def find_duplicates(file_list) :
    # Dictionary of hash to file path
    hashes = {}
    dupe_list = []
    for file in file_list :
        hash = hash_file(file)

        if hash in hashes :
            dupe_list.append(file)
            print('Found dupe file,', file, 'against', hashes[hash])
        else :
            hashes[hash] = file

    return dupe_list

def delete_dupes(dupe_list) :
    for file in dupe_list :
        
        try :
            remove(file)
            print('Deleting file ', file)
        except :
            print('Failed to delete', file)

def main():
    directory = getcwd()

    files = get_file_list(directory)

    dupes = find_duplicates(files)

    delete_dupes(dupes)

if __name__ == '__main__':
    main()