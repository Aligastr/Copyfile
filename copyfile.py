import os
import json
import sys
import argparse

parser = argparse.ArgumentParser()

#arguments
parser.add_argument('--target', type=str, help='Ziel der Prüfung (HDD oder TAPE)', required=True)
parser.add_argument('--dir', type=str, help='Pfad', required=True)
parser.add_argument('--outputdir', type=str, help='folder to store csv files', required=True)
parser.add_argument('--hdd_name', type=str, help='Pfad', required=True)
args = parser.parse_args()

#variablen
hdd_var = args.target
pfad = args.dir
outputdir = args.outputdir
hdd_name = args.hdd_name
#csv_file=r"C:\Users\butso\dev\copyfile\text_{}.csv".format(hdd_var)
csv_file=r"{}{}{}.csv".format(outputdir, os.sep, hdd_var)

#Erzeugt Liste von Dataien in eingegebene Pfad
with open(csv_file, 'a', encoding="utf-8") as fw:
    for dirpath, dirnames, filenames in os.walk(pfad): # Testpfad
        for file in filenames:
            a = []
            a.append(f"{file}")
            a.append(f"{dirpath}/{file}")
            a.append(str(os.path.getsize(dirpath + os.sep + file)))
            a.append(hdd_name)
            fw.write(";".join(a))
            fw.write('\n')
