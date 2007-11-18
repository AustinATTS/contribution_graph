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


contribute(datetime(2007, 11, 18, 12, 12, 12))
contribute(datetime(2007, 11, 19, 12, 12, 12))
contribute(datetime(2007, 11, 20, 12, 12, 12))
contribute(datetime(2007, 11, 21, 12, 12, 12))
contribute(datetime(2007, 11, 22, 12, 12, 12))
contribute(datetime(2007, 11, 23, 12, 12, 12))
contribute(datetime(2007, 11, 24, 12, 12, 12))
contribute(datetime(2007, 12, 16, 12, 12, 12))
contribute(datetime(2007, 12, 17, 12, 12, 12))
contribute(datetime(2007, 12, 18, 12, 12, 12))
contribute(datetime(2007, 12, 19, 12, 12, 12))
contribute(datetime(2007, 12, 20, 12, 12, 12))
contribute(datetime(2007, 12, 21, 12, 12, 12))
contribute(datetime(2007, 12, 22, 12, 12, 12))
contribute(datetime(2007, 11, 26, 12, 12, 12))
contribute(datetime(2007, 12, 4, 12, 12, 12))
contribute(datetime(2007, 12, 12, 12, 12, 12))
