from kivy.lang import Builder
from kivy.garden import matplotlib
from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.font_definitions import fonts
from kivymd.uix.tab import MDTabsBase
from kivymd.icon_definitions import md_icons

import matplotlib
matplotlib.use('module://kivy.garden.matplotlib.backend_kivy')
from matplotlib.figure import Figure
from numpy import arange, sin, pi
from kivy.app import App
import pandas as pd
import numpy as np
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvas,\
                                                NavigationToolbar2Kivy
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from matplotlib.transforms import Bbox
from kivy.uix.button import Button
from kivy.graphics import Color, Line, Rectangle

import matplotlib.pyplot as plt

fig,ax = plt.subplots()
xs = np.arange(0,10,0.1)
ys = [x**2 for x in xs]
ax.plot(xs,ys)
canvas = fig.canvas

class Tab(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''

class PressureTab(Tab):
    def __init__(self,**kwargs):
        super(PressureTab,self).__init__(**kwargs)
        self.add_widget(canvas)

class PressureGraph(MDBoxLayout):
    graph_settings = {'autoscale_x':True,'autoscale_y':True}
    pressure_data = pd.DataFrame()

    def __init__(self,**kwargs):
        super(PressureGraph,self).__init__(**kwargs)
        self.add_widget(canvas)

    def initialize_dataframe():
        pass

    def rebuild_graph():
        pass


class Matplottest(MDApp):
    title = 'Matplotlib Test'

    def build(self):
        return Builder.load_file("Matplottest.kv")

if __name__ == '__main__':
    Matplottest().run()
