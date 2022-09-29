import argparse
import pandas
import matplotlib
matplotlib.use('QtAgg')
import matplotlib.pyplot as plot
import mplcursors
import cartopy.crs as ccrs
import cartopy.feature as cfeature

parser = argparse.ArgumentParser(description='FDR')
parser.add_argument(
    '-f',
    '--file',
    nargs = 1,
    dest = 'file',
    required = True,
    help = 'FDR file'
)

args =  parser.parse_args()

fdr = pandas.read_csv(args.file[0])

ax = plot.axes(projection=ccrs.Robinson())

ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=':')
ax.add_feature(cfeature.LAKES, alpha=0.5)
ax.add_feature(cfeature.RIVERS)

plot.plot(fdr['FMC1LonDeg'], fdr['FMC1LatDeg'],
          color='purple',
          transform=ccrs.Geodetic()
          )

mplcursors.cursor(multiple=True).connect(
    'add',
    lambda sel: sel.annotation.set(
            text='{l:s}\n{y:.2f}\nt={x:.2f}'.format(
                l=sel.artist.get_label(), x=sel.target[0], y=sel.target[1]
            ),
            fontfamily='monospace',
            ma='right'
        )
)


plot.show()
