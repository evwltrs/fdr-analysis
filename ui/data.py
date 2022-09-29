import PySimpleGUI as sg
import pandas
import matplotlib
import matplotlib.pyplot as plot
import mplcursors
import math

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

_VARS = {'window': False}


def draw_figure_w_toolbar(canvas, fig, canvas_toolbar):
    if canvas.children:
        for child in canvas.winfo_children():
            child.destroy()
    if canvas_toolbar.children:
        for child in canvas_toolbar.winfo_children():
            child.destroy()
    figure_canvas_agg = FigureCanvasTkAgg(fig, master=canvas)
    figure_canvas_agg.draw()
    toolbar = Toolbar(figure_canvas_agg, canvas_toolbar)
    toolbar.update()
    figure_canvas_agg.get_tk_widget().pack(side='right', fill='both', expand=1)


class Toolbar(NavigationToolbar2Tk):
    def __init__(self, *args, **kwargs):
        super(Toolbar, self).__init__(*args, **kwargs)

AppFont = 'Any 16'
sg.theme('LightGrey')

layout = [
    [sg.Text("Choose a file: "), sg.Input(), sg.FileBrowse(key='-IN-')],
    [sg.B('Plot'), sg.B('Exit')],
    [sg.T('Controls:')],
    [sg.Canvas(key='controls_cv')],
    [sg.T('Figure:')],
    [sg.Column(
        layout=[
            [sg.Canvas(key='fig_cv',
                       # it's important that you set this size
                       size=(400 * 2, 800)
                       )]
        ],
        background_color='#DAE0E6',
        pad=(0, 0)
    )]
]

window = sg.Window('Graph with controls', layout, resizable=True)

def graph(file):

    fdr = pandas.read_csv(file)

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

    return figure




while True:
    event, values = window.read()
    print(event, values)
    if event in (sg.WIN_CLOSED, 'Exit'):  # always,  always give a way out!
        break
    elif event is 'Plot':
        figure = graph(values['-IN-'])
        DPI = figure.get_dpi()
        figure.set_size_inches(404 * 2 / float(DPI), 808 / float(DPI))
        draw_figure_w_toolbar(window['fig_cv'].TKCanvas, figure, window['controls_cv'].TKCanvas)

window.close()
