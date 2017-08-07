import os
from string import maketrans

def encode_files():
    a = os.listdir(r"D:/Dev/practice/python/resources/alphabet")
    working_dir = os.getcwd()
    os.chdir("D:/Dev/practice/python/resources/alphabet")

    for file_name in a:
        intab = "aeiou"
        outtab = "31579"
        transtab = maketrans(intab, outtab)
        os.rename(file_name, file_name.translate(transtab))
        print(file_name)

    os.chdir(working_dir)

def decode_files():
    a = os.listdir(r"D:/Dev/practice/python/resources/alphabet")
    working_dir = os.getcwd()
    os.chdir("D:/Dev/practice/python/resources/alphabet")

    for file_name in a:
        intab = "31579"
        outtab = "aeiou"
        transtab = maketrans(intab, outtab)
        os.rename(file_name, file_name.translate(transtab))
        print(file_name)

    os.chdir(working_dir)

decode_files()
