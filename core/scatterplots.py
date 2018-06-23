from collections import namedtuple

fields = ['label', 'color', 'alpha', 'shape', 'edge']
Scatterplot = namedtuple('Scatterplot', fields)

scatterplots = [
    Scatterplot('100%', 'navy', .8, 250, 'none'),
    Scatterplot('99%', 'blue', .7, 175, 'none'),
    Scatterplot('98%', 'dodgerblue', .5, 175, 'none'),
    Scatterplot('97%', 'palegreen', .5, 125, 'none'),
    Scatterplot('96%', 'lime', .7, 175, 'none'),
    Scatterplot('95%', 'gold', .7, 175, 'navy'),
    Scatterplot('94%', 'yellow', .8, 225, 'black')
]
