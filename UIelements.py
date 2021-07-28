###########################################################
# Home to all the kivy declarations (aside from .kv files)#
# Most functions of the UI will also end up here          #
###########################################################


from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.font_definitions import fonts
from kivymd.uix.tab import MDTabsBase
from kivymd.icon_definitions import md_icons

class Tab(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''
    def build(self):
        print("New Tab")


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
            NewTab = Tab(text=tab_text)
            MeasurementTabs.add_widget(NewTab)
            MeasurementTabs.switch_tab(tab_text)
            self.MeasurementN+=1


    def on_measurement_ref_press(self,MeasurementTabs,TabsLabel,MainTab,TabsBar,TabsCarousel):
        print("Ref Press")
        for instance_tab in TabsCarousel.slides:
            if instance_tab.text == TabsLabel.text:
                MeasurementTabs.remove_widget(TabsLabel)




FridgeCenter().run()
