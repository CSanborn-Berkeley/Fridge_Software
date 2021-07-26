import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import Floatlayout
from kivy.uix.scatter import Scatter
from kivy.uix.TextInput import TextInput
from kivy.uix.boxlayout import BoxLayout


class Tutorial(App):
    def build(self):
        return Label(text="Hello World")

Tutorial().run()
