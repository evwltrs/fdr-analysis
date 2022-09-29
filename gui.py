import PySimpleGUI as sg
import pandas
import matplotlib
import matplotlib.pyplot as plot
import mplcursors
import math
from library import *

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
    [sg.Text("Choose a file: "), sg.Input(), sg.FileBrowse(key='-IN-'), sg.B('Plot'), sg.B('Exit'), sg.Radio('Data', "RADIO1", default=True, key='-IN2-'), sg.Radio('Map', "RADIO1", default=False)],
    [sg.Canvas(key='controls_cv')],
    [sg.T('Figure:')],
    [sg.Column(
        layout=[
            [sg.Canvas(key='fig_cv',
                       # it's important that you set this size
                       size=(500 * 2, 800)
                       )]
        ],
        background_color='#DAE0E6',
        pad=(0, 0)
    )]
]

window = sg.Window('fdr-analyze', layout, resizable=True)



while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):  # always,  always give a way out!
        break
    elif event == 'Plot' and values['-IN-'] != '':
        if values['-IN2-']:
            figure = graph(values['-IN-'])
        else:
            figure = maps(values['-IN-'])
        DPI = figure.get_dpi()
        figure.set_size_inches(504 * 2 / float(DPI), 1008 / float(DPI))
        draw_figure_w_toolbar(window['fig_cv'].TKCanvas, figure, window['controls_cv'].TKCanvas)

window.close()
