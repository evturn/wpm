import sys
from argparse import ArgumentParser

from core import CSVParser
from core import Figure

def validate_args(args):
    if args.path is None:
        print(f'{argparser.prog}: No filepath was supplied.', file=sys.stderr)
        parser.print_help()
        sys.exit()

    csvparser = CSVParser(args)
    wpms, accuracies, dates, count = csvparser.parse()
    figure = Figure(count=count)
    figure.plot(wpms, accuracies)

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
