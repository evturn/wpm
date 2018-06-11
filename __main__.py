import sys
from argparse import ArgumentParser

from core import CSVParser

def validate_args(args):
    if args.path is None:
        msg = 'No filepath was supplied.'
        print(f'{argparser.prog}: {msg}', file=sys.stderr)
        parser.print_help()
        sys.exit()

    csvparser = CSVParser(args)
    data = csvparser.parse()
    print(data.wpm, data.count)

argparser = ArgumentParser(
    prog='WPM',
    description='You gonna eat that or nah?'
)
argparser.add_argument(
    '-p',
    '--path',
    dest='path',
    help='Relative path to the input file.'
)

args = argparser.parse_args()
validate_args(args)
