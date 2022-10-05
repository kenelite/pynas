#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

path = "F://alidrive//"
to_be_delete = "XXXX"


class BatchRename(object):
    def __init__(self, file_path, delete_pattern):
        self.file_path = file_path
        self.delete_pattern = delete_pattern
        self.file_list = []
        self.scan_dir(self.file_path)

    def scan_dir(self, cur_dir):
        for f in os.listdir(cur_dir):
            t_file = cur_dir + os.sep + f
            if os.path.isdir(t_file):
                self.scan_dir(t_file)
            else:
                self.file_list.append(t_file)

    def batch_rename(self):
        for filename in self.file_list:
            if self.delete_pattern in filename:
                print(filename)
                new_filename = filename.replace(to_be_delete, '')
                os.rename(filename, new_filename)
                print(new_filename)

    def batch_remove(self):
        for filename in self.file_list:
            if self.delete_pattern in filename:
                print(filename)
                os.remove(filename)


def main():
    br = BatchRename(file_path=path, delete_pattern=to_be_delete)
    br.batch_rename()


if __name__ == "__main__":
    main()
