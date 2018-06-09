import sys
from argparse import ArgumentParser

def validate_args(args):
    if args.path is None:
        msg = 'No filepath was supplied.'
        print(f'{parser.prog}: {msg}', file=sys.stderr)
        parser.print_help()
        sys.exit()

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
