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

KV = '''
MDBoxLayout:
    orientation: "vertical"


    MDTabs:
        id: tabs
        on_ref_press: app.on_ref_press(*args)


<Tab>

    MDIconButton:
        id: icon
        icon: app.icons[0]
        user_font_size: "48sp"
        pos_hint: {"center_x": .5, "center_y": .5}
'''

major_tab_keys = ['monitor','graph','file-settings']
major_tab_names = ['Monitor', 'Measure','Settings']


class Tab(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''


class FridgeCenter(MDApp):
    icons = list(md_icons.keys())[15:30]

    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        for name_tab, title_tab in zip(major_tab_keys,major_tab_names):
            self.root.ids.tabs.add_widget(Tab(icon = name_tab,title= title_tab))

    def on_ref_press(
        self,
        instance_tabs,
        instance_tab_label,
        instance_tab,
        instance_tab_bar,
        instance_carousel,
    ):
        '''
        The method will be called when the ``on_ref_press`` event
        occurs when you, for example, use markup text for tabs.

        :param instance_tabs: <kivymd.uix.tab.MDTabs object>
        :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>
        :param instance_tab: <__main__.Tab object>
        :param instance_tab_bar: <kivymd.uix.tab.MDTabsBar object>
        :param instance_carousel: <kivymd.uix.tab.MDTabsCarousel object>
        '''

        # Removes a tab by clicking on the close icon on the left.
        for instance_tab in instance_carousel.slides:
            if instance_tab.text == instance_tab_label.text:
                instance_tabs.remove_widget(instance_tab_label)
                break


FridgeCenter().run()
