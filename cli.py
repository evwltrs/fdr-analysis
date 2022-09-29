import argparse
import pandas
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plot
import mplcursors
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from library import *


parser = argparse.ArgumentParser(description='FDR')
parser.add_argument(
    '-f',
    '--file',
    nargs = 1,
    dest = 'file',
    required = True,
    help = 'FDR filepath'
)

parser.add_argument(
    '-t',
    '--type',
    nargs = 1,
    dest = 'type',
    required = True,
    help = 'graph or map'
)

parser.add_argument(
    '-o',
    '--output',
    nargs = 1,
    dest = 'output',
    required = True,
    help = 'Path for output'
)


args =  parser.parse_args()

print('The program is not frozen. It may take some time to process.')

if args.type[0] == 'map':
    figure = maps(args.file[0])
    figure.savefig(args.output[0], dpi=300, bbox_inches='tight')
elif args.type[0] == 'graph':
    figure = graph(args.file[0])
    figure.savefig(args.output[0], dpi=300, bbox_inches='tight')
else:
    print('Invalid Type')

#plot.show()
