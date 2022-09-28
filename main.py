import argparse
import pandas
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plot
import mplcursors
import math

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

print(fdr.index)

figure, axes = plot.subplots(4, sharex = True)

# Altitude
alt = fdr['ADC1AltStdFt']

ax1 = axes[0]
ax1.plot(fdr.index / 60, alt, label='alt')
ax1.set_ylim(0, math.ceil(alt.max() / 1000) * 1000 + 1000)
ax1.legend()
ax1.set_title('Altitude')

# Speed
ias = fdr['ADC1IASKt']
gs = fdr['GPS1GSKt']

ax2 = axes[1]
ax2.plot(fdr.index / 60, ias, label='IAS')
ax2.plot(fdr.index / 60 , gs, label='GS')
ax2.set_ylim(0, gs.max() + 10)
ax2.legend()
ax2.set_title('Speed')

# N speed
eng1n1 = fdr['Eng1N1']
eng2n1 = fdr['Eng2N1']
eng1n2 = fdr['Eng1N2']
eng2n2 = fdr['Eng2N2']

ax3 = axes[2]
ax3.plot(fdr.index / 60, eng1n1, label='Engine 1 N1')
ax3.plot(fdr.index / 60, eng2n1, label='Engine 2 N1')
ax3.plot(fdr.index / 60, eng1n2, label='Engine 1 N2')
ax3.plot(fdr.index / 60 , eng2n2, label='Engine 2 N2')

ax3.legend()
ax3.set_ylim(0, 105)
ax3.set_title('N speed')

# Fuel flow
eng1ff = fdr['Eng1FFLbsHr']
eng2ff = fdr['Eng2FFLbsHr']

ax4 = axes[3]
ax4.plot(fdr.index / 60, eng1ff, label='Engine 1 Fuel Flow')
ax4.plot(fdr.index / 60, eng2ff, label='Engine 2 Fuel Flow')
maxff = max(eng1ff.max(), eng2ff.max())
ax4.set_ylim(0, math.ceil(maxff / 1000) * 1000)
ax4.set_title('Fuel Flow')

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

# plot.get_current_fig_manager().window.state('zoomed')

plot.show()
