from collections import namedtuple

fields = ['label', 'color', 'alpha', 'shape', 'edge']
Scatterplot = namedtuple('Scatterplot', fields)

scatterplots = [
    Scatterplot('100%', 'midnightblue', .9, 400, 'none'),
    Scatterplot('99%', 'dodgerblue', .9, 150, 'none'),
    Scatterplot('98%', 'cyan', .6, 100, 'none'),
    Scatterplot('97%', 'lime', .6, 100, 'none'),
    Scatterplot('96%', 'yellow', .9, 250, 'none'),
    Scatterplot('☠︎☠︎☠︎', 'red', .9, 350, 'none'),
]
