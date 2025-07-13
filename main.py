from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager ,Screen
Window.clearcolor=(100/255.0,0,1,1)
Window.size=(400,630)

class Mainscreen(Screen):
    pass

class SecondScreen(Screen):
    pass
class Python(Screen):
    pass
class Html(Screen):
    pass
class Cplus(Screen):
    pass
class Cs50(Screen):
    pass
class Perl(Screen):
    pass
class Css(Screen):
    pass
class Eroor(Screen):
    pass
class Myscreenmanager(ScreenManager):
    pass
ks=Builder.load_file('C:/Users/zacharia/Desktop/kivy/my.kv')
class Mykv(App):
    def build(self):
        self.title='zacharia'
        return ks
    
Mykv().run()

    


     
        


