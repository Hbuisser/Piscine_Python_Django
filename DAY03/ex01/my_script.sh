#!/bin/sh

pip3 --version

pip3 install --log file.log --target=local_lib/ --upgrade package_name git+https://github.com/jaraco/path.git > /dev/null
python3 my_program.py
