#!/usr/bin/env python3
import sys
import os
from string import Template

CPP_TEMPLATE = """#include "stdio.h"

int main(){
    printf("Hello World\\n");

    return 0;
}"""

SUB_CMAKE_TEMPLATE = """cmake_minimum_required(VERSION 3.17)
project($project_name)

set(CMAKE_CXX_STANDARD 20)

add_executable($sub_name $sub_file_name)"""


def make_sub_dir_path(project_name, sub_name):
    print('Project directory: ' + project_name)
    print('Subproject name: ' + sub_name)

    return os.path.join(project_name, sub_name)


def write_cpp(path, sub_name, template):
    print('Writing .cpp template...')

    file = open(sub_name + ".cpp", "x")
    file.write(template)
    file.close()


def create_dir(path):
    print('Making directory: ' + path)
    os.mkdir(path)


def write_sub_cmake(project_name, sub_name, template):
    print('Writing sub cmake...')

    d = {
        'project_name': project_name,
        'sub_name': sub_name,
        'sub_file_name': (sub_name + ".cpp")
    }

    src = Template(template).substitute(d)

    file = open("CMakeLists.txt", "x")
    file.write(src)
    file.close()


def write_cmake(sub_name):
    print('Writing outer cmake...')
    template = 'add_subdirectory(\"$project_dir/$sub_name\" \"$project_dir/$sub_name/output\")\n'
    d = {
        'project_dir': '${PROJECT_SOURCE_DIR}',
        'sub_name': sub_name
    }
    src = Template(template).substitute(d)

    file = open("CMakeLists.txt", "a")
    file.write(src)
    file.close()


def main(args):
    if len(args) == 2:
        sub_name = args[1]
        print(args[1])
    else:
        print('No subproject name specified. Exiting...')
        return

    project_name = os.getcwd()
    path = make_sub_dir_path(project_name, sub_name)
    create_dir(path)
    write_cmake(sub_name)
    os.chdir(path)
    write_cpp(path, sub_name, CPP_TEMPLATE)
    write_sub_cmake(project_name, sub_name, SUB_CMAKE_TEMPLATE)


if __name__ == '__main__':
    main(sys.argv)
