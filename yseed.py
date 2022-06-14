#!/usr/bin/env python
# yseed.py
# script em python para guardar uma arvore de directï¿½rios num ficheiro  YAML
# by pescadorDigital, 14/06/22
# versao 0.1

### BIBLIOTECAS ###

from os import listdir
from os.path import isdir,islink
import os
import os.path
import sys
import yaml

### CONSTANTES ###

### FUNCOES ###

def visitparse(this_dir,dirtree):
        parent_path,dirname = os.path.split(this_dir)
        dirtree[dirname] = {}
        for f in listdir(this_dir):
                abs_path = os.path.join(this_dir,f)
                if isdir(abs_path) and not islink(abs_path):
                        visitparse(abs_path,dirtree[dirname])

def syntax():
        return sys.argv[0] + " [directory] [yml dir tree]"


### PROGRAMA PRINCIPAL #####
if __name__ == "__main__":
        dictree = {}

        if len(sys.argv) < 2:
                _dir = os.getcwd()
        else:
                if len(sys.argv) == 1:
                        print (syntax())
                else:
                        _dir = sys.argv[1]


        # despises the final /
        if _dir[-1] == '/'  : _dir = _dir[:-1]
        if _dir == ".": _dir = os.getcwd()
        (path,dirname) = os.path.split(_dir)
        ymlfilename = "%s_dirtree.yml" % dirname
        print ("Writing directory tree in %s !" % ymlfilename)
        ymlfile = open(ymlfilename,"w+")
        visitparse(_dir,dictree)
        yaml.safe_dump(dictree,ymlfile)
        ymlfile.close()
