import random
import os
import shutil
import argparse

dir_path = r'./images'


def create_folder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)


def divide_set(file_names, ratio):
    file_names_len = len(file_names)
    test_file_names_len = int(file_names_len * ratio)

    for i in range(test_file_names_len):
        file_name = file_names[i]
        print(file_name)
        jpg_name = file_name + '.jpg'
        xml_name = file_name + '.xml'
        shutil.copyfile(dir_path + '/' + jpg_name, './test/' + jpg_name)
        shutil.copyfile(dir_path + '/' + xml_name, './test/' + xml_name)

    for i in range(test_file_names_len, file_names_len):
        file_name = file_names[i]
        print(file_name)
        jpg_name = file_name + '.jpg'
        xml_name = file_name + '.xml'
        shutil.copyfile(dir_path + '/' + jpg_name, './train/' + jpg_name)
        shutil.copyfile(dir_path + '/' + xml_name, './train/' + xml_name)


def main():
    os_files = os.listdir(dir_path)
    file_names = []

    parser = argparse.ArgumentParser()
    parser.add_argument('--ratio', help='.ratio of test set', type=float,
                        default=0.2)
    args = parser.parse_args()

    for dir in os_files:
        if dir[:-4] not in file_names:
            file_names.append(dir[:-4])

    random.shuffle(file_names)

    create_folder('./test')
    create_folder('./train')

    divide_set(file_names, args.ratio)

    print('done.')


if __name__ == '__main__':
    main()
