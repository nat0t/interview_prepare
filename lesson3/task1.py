"""
Написать программу, которая будет содержать функцию для получения имени файла из полного пути до него. При вызове
функции в качестве аргумента должно передаваться имя файла с расширением. В функции необходимо реализовать поиск
полного пути по имени файла, а затем «выделение» из этого пути имени файла (без расширения).
"""
import os


def get_file_name(path: str) -> str:
    return os.path.splitext(os.path.basename(path))[0]


if __name__ == '__main__':
    file_name = '/home/master/Загрузки/Cheer up/18. Billy Joel - Uptown Girl.mp3'
    print(f'{file_name}\t\t{get_file_name(file_name)}')
