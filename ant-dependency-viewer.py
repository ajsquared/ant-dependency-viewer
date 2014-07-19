#!/usr/bin/env python

from xml.etree import ElementTree
import argparse
from graphviz import Digraph
import os

def get_parser():
    parser = argparse.ArgumentParser(description='View dependencies of an Ant buildfile.')
    parser.add_argument('-f', '--buildfile', metavar='FILE', help='Path to the buildfile to visualize', required=True)
    parser.add_argument('-t', '--render', metavar='FORMAT', help='Render the dependency graph with graphviz in the given format')

    return parser


def print_target(target, target_deps, depth=0):
    indent = '  ' * depth
    print indent + target
    for dep in target_deps[target]:
        print_target(dep, target_deps, depth+1)

    
def parse_build_file(build_file_path, render_format):
    root = ElementTree.parse(build_file_path)

    target_deps = {}

    for t in root.iter('target'):
        if 'depends' in t.attrib:
            deps = [d.strip() for d in t.attrib['depends'].split(',')]
        else:
            deps = []
        name = t.attrib['name']
        target_deps[name] = deps

    if render_format:
        dot = Digraph(build_file_path, format=render_format)
        
    for t in target_deps:
        print
        print_target(t, target_deps)
        if render_format:
            dot.node(t, t)
            for d in target_deps[t]:
                dot.edge(t, d)

    if render_format:
        dot.render(filename=os.path.splitext(build_file_path)[0], directory=os.path.dirname(build_file_path))

if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()

    parse_build_file(args.buildfile, args.render)
