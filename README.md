# ant-dependency-viewer

## Introduction

ant-dependency-viewer is a Python script that visualizes the dependency graph of an Ant buildfile.

## Dependencies

1. Python 2.7
2. graphviz
3. Python graphviz package (```pip install graphviz```)

## Usage

```./ant-dependency-viewer.py -f BUILDFILE``` will print a textual
representation of your Ant buildfile to stdout.  If you would like a
graphical representation rendered with graphviz, use add the ```-t```
argument to specify the output format: ```./ant-dependency-viewer.py
-f BUILDFILE -t FORMAT```.  ```FORMAT``` can be one of ```pdf```,
```ps```, ```svg```, ```fig```, ```pcl```, ```png```, ```gif```, or
```dia```.  This will produce two files in the same directory as the
buildfile, the ```dot``` source and the rendered view of the
dependency graph.
