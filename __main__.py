import sys
from argparse import ArgumentParser

from core import CSVParser
from core import Plotter
from core import Figure

def validate_args(args):
    if args.path is None:
        print(f'{argparser.prog}: No filepath was supplied.', file=sys.stderr)
        parser.print_help()
        sys.exit()

    csvparser = CSVParser(args)
    w, a, c = csvparser.parse()
    plotter = Plotter(count=c)
    xs, ys = plotter.get_plots(w)
    figure = Figure(plotter)

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
