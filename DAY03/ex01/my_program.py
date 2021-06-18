#!/usr/bin/python3

from local_lib.path import Path

if __name__ == '__main__':
    d = Path("directory")
    d.mkdir_p()
    f = Path("directory/test.txt")
    f.touch()
    f.open()
    f.write_text("Helloowwwww\n")
    print(f.read_text())

