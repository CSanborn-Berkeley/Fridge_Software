###########################################################
# Home to all the kivy declarations (aside from .kv files)#
# Most functions of the UI will also end up here          #
###########################################################
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('module://kivy.garden.matplotlib.backend_kivy')
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvas,\
                                                NavigationToolbar2Kivy
from kivy.garden import matplotlib
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.font_definitions import fonts
from kivymd.uix.tab import MDTabsBase
from kivymd.icon_definitions import md_icons
import matplotlib.pyplot as plt



class Tab(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''

class MeasurementTab(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab'''

class PressureGraph(MDBoxLayout):
    graph_settings = {'autoscale_x':True,'autoscale_y':True}
    pressure_data = pd.DataFrame()


    def __init__(self,**kwargs):
        super(PressureGraph,self).__init__(**kwargs)
        fig,ax = plt.subplots()
        canvas = fig.canvas
        xs = np.arange(0,10,0.1)
        ys = [x**2 for x in xs]
        ax.plot(xs,ys)
        ax.set_xlabel("Time")
        ax.set_ylabel("Pressure")
        canvas = fig.canvas
        self.add_widget(canvas)

    def rebuild_graph(self):
        pass

class FlowGraph(MDBoxLayout):
    graph_settings = {'autoscale_x':True,'autoscale_y':True}
    pressure_data = pd.DataFrame()


    def __init__(self,**kwargs):
        super(FlowGraph,self).__init__(**kwargs)
        fig,ax = plt.subplots()
        canvas = fig.canvas
        xs = np.arange(0,10,0.1)
        ys = [x**2 for x in xs]
        ax.plot(xs,ys)
        ax.set_xlabel("Time")
        ax.set_ylabel("Pressure")
        canvas = fig.canvas
        self.add_widget(canvas)

    def rebuild_graph(self):
        pass

class TemperatureGraph(MDBoxLayout):
    graph_settings = {'autoscale_x':True,'autoscale_y':True}
    pressure_data = pd.DataFrame()


    def __init__(self,**kwargs):
        super(TemperatureGraph,self).__init__(**kwargs)
        fig,ax = plt.subplots()
        canvas = fig.canvas
        xs = np.arange(0,10,0.1)
        ys = [x**2 for x in xs]
        ax.plot(xs,ys)
        ax.set_xlabel("Time")
        ax.set_ylabel("Pressure")
        canvas = fig.canvas
        self.add_widget(canvas)

    def rebuild_graph(self):
        pass

class FridgeCenter(MDApp):
    icons = list(md_icons.keys())[15:30]
    MeasurementN = 1

    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = '800'
        return Builder.load_file("FridgeCenter.kv")

    def on_measurement_tab_switch(self,MeasurementTabs,TabName,LabelObj,Ref):
        if TabName.icon == "plus":
            name_tab = "Measurement "+ str(self.MeasurementN)
            tab_text = f"{name_tab} [ref={name_tab}][font={fonts[-1]['fn_regular']}]{md_icons['close']}[/font][/ref]"
            NewTab = MeasurementTab(text=tab_text)
            MeasurementTabs.add_widget(NewTab)
            MeasurementTabs.switch_tab(tab_text)
            self.MeasurementN+=1


    def on_measurement_ref_press(self,MeasurementTabs,TabsLabel,MainTab,TabsBar,TabsCarousel):
        print("Ref Press")
        for instance_tab in TabsCarousel.slides:
            if instance_tab.text == TabsLabel.text:
                MeasurementTabs.remove_widget(TabsLabel)




FridgeCenter().run()
