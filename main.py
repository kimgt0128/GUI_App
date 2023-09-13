# -*- coding: utf-8 -*-
"""_summary_
    1. 화면 전환 애니메이션 추가하기
    2. 7초 후 자동으로 main화면 전환 기능 - Done
    3. popup화면에서 글씨추가, 돌아가기 버튼 만들기 - Done
    4. dictionary를 이용하여 글씨 추가하기 
    5. 각 화면마다 자동 돌아가기 기능 설정하기 - Done
    6. 메인 화면에 음성 넣고, 주기 설정버튼 
    7. 소리 추가하기
    """

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.lang import Builder
from custompopup import Custompopup
from kivy.clock import Clock



class MainScreen(Screen, Label, BoxLayout):
    back = None
    def firstBtn(self):
        sm.current = "first"
        self.back = Clock.schedule_once(self.autoMain, 15)
        
    def secondBtn(self):
        sm.current = "second"
        self.back = Clock.schedule_once(self.autoMain, 15)
        
    def thirdBtn(self):
        sm.current = "third"
        self.back = Clock.schedule_once(self.autoMain, 15)
    
    def autoMain(self, dt):
        sm.current = "main"
        del self
    def cancel(self):
        self.back.cancel()
        
        
class FirstScreen(Screen):
    def __init__(self, **kwargs):
        super(FirstScreen, self).__init__(**kwargs)
        self.main_screen1 = None  # Store a reference to the MainScreen instance

    def set_main_screen(self, main_screen):
        self.main_screen1 = main_screen

        
    def showPopup(self):
        self.main_screen1.cancel()
        return showPopup(self.name)
        
    def mainBtn(self):
        sm.current = "main"
        
        
class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super(SecondScreen, self).__init__(**kwargs)
        self.main_screen2 = None  # Store a reference to the MainScreen instance
        
    def set_main_screen(self, main_screen):
        self.main_screen2 = main_screen
    
    def showPopup(self):
        self.main_screen2.cancel()
        return showPopup(self.name)
    
    def mainBtn(self):
        sm.current = "main"


class ThirdScreen(Screen):
    def __init__(self, **kwargs):
        super(ThirdScreen, self).__init__(**kwargs)
        self.main_screen3 = None  # Store a reference to the MainScreen instance
        
    def set_main_screen(self, main_screen):
        self.main_screen3 = main_screen
    
    def showPopup(self):
        self.main_screen3.cancel()
        return showPopup(self.name)
        
    def mainBtn(self):
        sm.current = "main"
        
    def autoMain(self, dt):
        sm.current = "main"


class WindowManager(ScreenManager):
     pass

sm = WindowManager()
def showPopup(name):
    popup = Custompopup(text=name)
    popup.open()

class MyApp(App):
    def build(self):
        
        Builder.load_file("mainscreen.kv")
        Builder.load_file("firstscreen.kv")
        Builder.load_file("secondscreen.kv")
        Builder.load_file("thirdscreen.kv")
    
        screens = [MainScreen(name="main"), FirstScreen(name="first"), SecondScreen(name="second"), ThirdScreen(name="third")]
        
        for screen in screens:
            sm.add_widget(screen)
            if screen.name is not "main":
                screen.set_main_screen(screens[0])
            
            

        sm.current = "main"
        
        return sm


if __name__ == "__main__":
    MyApp().run()
    
    