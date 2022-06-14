### YSEED

Stores the tree structure of some directory in a YAML file.
The command :
```
    python yseed.py <somedir>
```
will create a file `<somedir>_ditree.yml` in the file. In a case the directory name is not provided, it will be used the currente directory.

The script restore_tree.py will restore the dir tree in some dir (there is no need to create the root dir first).
