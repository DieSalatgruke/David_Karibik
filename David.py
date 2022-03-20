import os
import zipfile
import json
import datetime
import shutil
import xml.etree.ElementTree as ET

SAVED_DATA = 'path.json'


def extract_xml_data():
    tree = ET.parse('C:\\MaHo\\test\\Von\\temp\\00523-2022-90022-FFA-20220308.xml')
    root = tree.getroot()
    list_root = []
    for element in root.findall("*"):
        list_root.append(element.text)
    projekt_nummer = list_root[5]
    auflistungsnum = projekt_nummer[8:13]
    for elm in range(auflistungsnum):
        auf_list = []
        if elm != '0':
            auflistnum = auf_list.append(elm)
            print(auflistnum)
            return auflistnum


    #pro_num = [projekt_nummer.split('')]
    #'-'.join(pro_num[0:3] + pro_num[4:7] + pro_num[-1])


def delete_dir():
    path_del_dir = data_from_json["path_temp"]
    shutil.rmtree(path_del_dir)


def path_reader():
    with open('path.json', 'r') as f:
        data_json = json.load(f)
        return data_json


def filename_creater():
    date_all = datetime.datetime.today().strftime('%Y%m%d')
    date_year = datetime.datetime.today().strftime('%Y')
    filename = str(input('Dateiname(FFA): '))
    filename = str(data_from_json['tue_nr'] + '-' + date_year + '-' + filename + '-' + 'FFA' + '-' + date_all + '.zip')
    return filename


def dir_creater():
    dirname = str(input('Projektnummer(LK): '))
    dirname = str(data_from_json['lk'] + '-' + dirname)
    return dirname


def file_handler(*args):
    try:
        with open(f'{data_from_json["path_archiv"]}\\'
                  f'{datetime.datetime.today().strftime("Archiv_Protokoll_FFA_" + "%Y%m.txt")}', mode='a+') as file:
            file.write('-' * 45 + '\n')
            file.write('Protokoll ' + datetime.datetime.today().strftime('%A, den %d %B %Y') + '\n')
            file.write('Eintrag vorgenommen: ' + datetime.datetime.today().strftime('%X') + '\n')
            file.write('-' * 45 + '\n')
            file.write('\n')
            for arg in args:
                file.writelines(arg + '\n')

    except FileExistsError:
        with open(f'{data_from_json["path_archiv"]}\\'
                  f'{datetime.datetime.today().strftime("Archiv_Protokoll_FFA_" + "%Y%m.txt")}', mode='w+') as file:
            file.write('\n' + '-' * 45 + '\n')
            file.write('Neuer Eintrag in das Protokoll.' + '\n')
            file.write('Uhrzeit Eintragung: ' + datetime.datetime.today().strftime('%X') + '\n')
            file.write('-' * 45 + '\n')
            file.write('\n')
            for arg in args:
                file.writelines(arg + '\n')


if __name__ == '__main__':
    extract_xml_data()
    data_from_json = path_reader()
    file_name = filename_creater()
    dir_name = dir_creater()

    if os.path.exists(f'{data_from_json["path_from"]}\\{file_name}'):
        if os.path.exists(f'{data_from_json["path_to"]}\\{dir_name}{data_from_json["ending_path_to"]}'):
            with zipfile.ZipFile(f'{data_from_json["path_from"]}\\{file_name}', 'r') as source:
                source.extractall(f'{data_from_json["path_to"]}\\{dir_name}{data_from_json["ending_path_to"]}')
            file_handler(f'{data_from_json["path_from"]}\\{file_name}',
                         f'{data_from_json["path_to"]}\\{dir_name}{data_from_json["ending_path_to"]}')
            print('Done!')
            input()

        else:
            print('Fail!')
            input()
    else:
        print('Fail!')
        input()
