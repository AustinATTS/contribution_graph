#!/usr/bin/env python
import argparse
import os
from datetime import datetime
from datetime import timedelta
from random import randint
from subprocess import Popen
import sys


def contribute(date):
    with open(os.path.join(os.getcwd(), 'birth.txt'), 'a') as file:
        file.write(message(date) + '\n\n')
    run(['git', 'add', '.'])
    run(['git', 'commit', '-m', '"%s"' % message(date),
         '--date', date.strftime('"%Y-%m-%d %H:%M:%S"')])


def run(commands):
    Popen(commands).wait()


def message(date):
    return date.strftime('Contribution: %Y-%m-%d %H:%M')


contribute(datetime(2007, 10, 7, 12, 12, 12))
contribute(datetime(2007, 10, 8, 12, 12, 12))
contribute(datetime(2007, 10, 9, 12, 12, 12))
contribute(datetime(2007, 10, 10, 12, 12, 12))
contribute(datetime(2007, 10, 11, 12, 12, 12))
contribute(datetime(2007, 10, 12, 12, 12, 12))
contribute(datetime(2007, 10, 13, 12, 12, 12))
contribute(datetime(2007, 10, 14, 12, 12, 12))
contribute(datetime(2007, 10, 21, 12, 12, 12))
contribute(datetime(2007, 10, 23, 12, 12, 12))
contribute(datetime(2007, 10, 28, 12, 12, 12))
contribute(datetime(2007, 10, 30, 12, 12, 12))
contribute(datetime(2007, 10, 16, 12, 12, 12))
contribute(datetime(2007, 11, 5, 12, 12, 12))
contribute(datetime(2007, 11, 7, 12, 12, 12))
contribute(datetime(2007, 11, 8, 12, 12, 12))
contribute(datetime(2007, 11, 9, 12, 12, 12))
contribute(datetime(2007, 11, 10, 12, 12, 12))
