import argparse
import pandas
import matplotlib
matplotlib.use('QtAgg')
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

figure, axes = plot.subplots(5, sharex = True)

# Altitude
alt = fdr['ADC1AltStdFt']

ax1 = axes[0]
ax1.plot(fdr.index / 60, alt, label='alt')
ax1.set_ylim(0, math.ceil(alt.max() / 1000) * 1000 + 1000)
ax1.set_ylabel('Ft')
ax1.legend()
ax1.set_title('Altitude')

# Speed
ias = fdr['ADC1IASKt']
gs = fdr['GPS1GSKt']

ax2 = axes[1]
ax2.plot(fdr.index / 60, ias, label='IAS')
ax2.plot(fdr.index / 60 , gs, label='GS')
ax2.set_ylim(0, gs.max() + 10)
ax2.set_ylabel('Kts')
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
ax3.set_ylim(0, 105)
ax3.set_ylabel('%')
ax3.legend()
ax3.set_title('N speed')

# Fuel flow
eng1ff = fdr['Eng1FFLbsHr']
eng2ff = fdr['Eng2FFLbsHr']

ax4 = axes[3]
ax4.plot(fdr.index / 60, eng1ff, label='Engine 1')
ax4.plot(fdr.index / 60, eng2ff, label='Engine 2')
maxff = max(eng1ff.max(), eng2ff.max())
ax4.set_ylim(0, math.ceil(maxff / 1000) * 1000)
ax4.set_ylabel('Lbs/Hr')
ax4.legend()
ax4.set_title('Fuel Flow')

# Fuel quantity
fuelleft = fdr['FSCU1LMainLbs']
fuelright = fdr['FSCU1RMainLbs']
fuelaux = fdr['FSCU1AuxLbs']
fueltail = fdr['FSCU1TailLbs']

ax5 = axes[4]
ax5.plot(fdr.index / 60, fuelleft, label='Left Main')
ax5.plot(fdr.index / 60, fuelright, label='Right Main')
maxfuel = max(fuelleft.max(), fuelright.max(), fuelaux.max(), fueltail.max())
ax5.set_ylim(0, math.ceil(maxfuel / 1000) * 1000)
ax5.set_ylabel('Lbs')
ax5.legend()
ax5.set_title('Fuel Quantity')

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
