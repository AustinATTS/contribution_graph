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


contribute(datetime(2007, 7, 15, 12, 12, 12))
contribute(datetime(2007, 7, 16, 12, 12, 12))
contribute(datetime(2007, 7, 17, 12, 12, 12))
contribute(datetime(2007, 7, 18, 12, 12, 12))
contribute(datetime(2007, 7, 19, 12, 12, 12))
contribute(datetime(2007, 7, 20, 12, 12, 12))
contribute(datetime(2007, 7, 21, 12, 12, 12))
contribute(datetime(2007, 7, 22, 12, 12, 12))
contribute(datetime(2007, 7, 24, 12, 12, 12))
contribute(datetime(2007, 7, 28, 12, 12, 12))
contribute(datetime(2007, 7, 29, 12, 12, 12))
contribute(datetime(2007, 7, 31, 12, 12, 12))
contribute(datetime(2007, 8, 4, 12, 12, 12))
contribute(datetime(2007, 8, 5, 12, 12, 12))
contribute(datetime(2007, 8, 7, 12, 12, 12))
contribute(datetime(2007, 8, 11, 12, 12, 12))
contribute(datetime(2007, 8, 13, 12, 12, 12))
contribute(datetime(2007, 8, 15, 12, 12, 12))
contribute(datetime(2007, 8, 16, 12, 12, 12))
contribute(datetime(2007, 8, 17, 12, 12, 12))
