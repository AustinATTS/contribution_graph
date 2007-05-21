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


contribute(datetime(2007, 5, 21, 12, 12, 12))
contribute(datetime(2007, 5, 25, 12, 12, 12))
contribute(datetime(2007, 5, 27, 12, 12, 12))
contribute(datetime(2007, 5, 29, 12, 12, 12))
contribute(datetime(2007, 6, 2, 12, 12, 12))
contribute(datetime(2007, 6, 3, 12, 12, 12))
contribute(datetime(2007, 6, 5, 12, 12, 12))
contribute(datetime(2007, 6, 9, 12, 12, 12))
contribute(datetime(2007, 6, 10, 12, 12, 12))
contribute(datetime(2007, 6, 12, 12, 12, 12))
contribute(datetime(2007, 6, 16, 12, 12, 12))
contribute(datetime(2007, 6, 17, 12, 12, 12))
contribute(datetime(2007, 6, 20, 12, 12, 12))
contribute(datetime(2007, 6, 21, 12, 12, 12))
contribute(datetime(2007, 6, 22, 12, 12, 12))
