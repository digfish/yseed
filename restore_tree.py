#!/usr/bin/env python
# recria a árvore de directórios guardada
# by pescadorDigital, 14/06/2022
# version 0.1

### BIBLIOTECAS ###
from os import makedirs
import os.path
import yaml
import sys

### CONSTANTES ###

### FUNCOES ###
def walkTree(dictree,todir):
    for child in dictree.keys():
        if type(dictree[child]) == dict:
            newdirname = todir + "/" + child;
            print ("Creating " + newdirname)
            os.makedirs(newdirname)
            walkTree(dictree[child],newdirname)

### PROGRAMA PRINCIPAL #####

if __name__ == "__main__":
    dictree = yaml.safe_load(open(sys.argv[1],'r'))
    if len(sys.argv) < 3: todir = '.'
    else: todir = sys.argv[2]
    walkTree(dictree,todir)
