import sys
from argparse import ArgumentParser

def validate_args(args):
    print('Check out these arguments:', args)

parser = ArgumentParser(
    prog='WPM',
    description='You gonna eat that or nah?'
)
parser.add_argument(
    '-p',
    '--path',
    dest='path',
    help='Relative path to the input file.'
)

args = parser.parse_args()
validate_args(args)
