import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return FloatLayout(children=[Label(text='Hello, world!', pos_hint={'center_x': 0.5, 'center_y': 0.5})])

if __name__ == '__main__':
    MyApp().run()
