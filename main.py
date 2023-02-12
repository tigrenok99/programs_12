from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.app import App


Builder.load_file('Design.kv')

class MyLayout(Widget):
    def clear(self):
        pass

class playersssApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    playersssApp().run()