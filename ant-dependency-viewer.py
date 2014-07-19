#!/usr/bin/env python

from xml.etree import ElementTree
import argparse

def get_parser():
    parser = argparse.ArgumentParser(description='View dependencies of an Ant buildfile.')
    parser.add_argument('-f', '--buildfile', metavar='FILE', help='Path to the buildfile to visualize', required=True)
    parser.add_argument('-p', '--png', metavar='PNG', help='Location in which to produce a PNG view')

    return parser


def print_target(target, target_deps, depth=0):
    indent = '  ' * depth
    print indent + target
    for dep in target_deps[target]:
        print_target(dep, target_deps, depth+1)

    
def parse_build_file(build_file_path, png_output_file):
    root = ElementTree.parse(build_file_path)

    target_deps = {}

    for t in root.iter('target'):
        if 'depends' in t.attrib:
            deps = [d.strip() for d in t.attrib['depends'].split(',')]
        else:
            deps = []
        name = t.attrib['name']
        target_deps[name] = deps


    for t in target_deps:
        print
        print_target(t, target_deps)


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()

    parse_build_file(args.buildfile, args.png)
