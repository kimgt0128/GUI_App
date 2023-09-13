from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock

class Custompopup(Popup):
    def __init__(self, text, **kwargs):
        super(Custompopup, self).__init__(**kwargs)
        self.name1 = text
        self.initial_time = 10
        self.remaining_time = self.initial_time
        
        self.size_hint = (0.9, 0.95)
        self.auto_dismiss = False
        self.title = f"{self.name1} {text}업무 안내 ({self.remaining_time}초 후 종료됨)"
        self.title_font = 'myfont2-M.ttf'
        self.title_size = 65
        
        content_layout = BoxLayout(orientation='vertical',size_hint=(1, 0.7))
        label = Label(text="안내문", font_name='myfont1.ttf', font_size=20)
        content_layout.add_widget(label)
        
        button_layout = BoxLayout(orientation='horizontal', size_hint=(0.5, 0.3), pos_hint={'center_x': 0.5, 'center+y': 0.5})
        
        main_button = Button(size_hint=(0.5, 1), text="확인(처음으로)", font_name='myfont2-M.ttf', on_release=self.dismiss)
        button_layout.add_widget(main_button)
        
        content_layout.add_widget(button_layout)
        
        self.content = content_layout
        
        Clock.schedule_interval(self.update_time, 1)
        
    def update_time(self, dt):
        self.remaining_time -= 1
        self.title = f"{self.name1} {self.name1}업무 안내 ({self.remaining_time}초 후 종료됨)"
        if self.remaining_time == 0:
            self.dismiss()
