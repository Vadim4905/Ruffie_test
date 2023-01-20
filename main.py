# не забудь імпортувати необхідні елементи!
# програма з двома екранами
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen  
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.properties import NumericProperty, BooleanProperty, StringProperty
import instructions
import ruffier
import seconds 




Window.clearcolor = (0.8,0.6,0.2,0.5)


def check_int(str_num):
    try:
        return int(str_num)
    except:
        return False


class InstructionScreen(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.instruct_l = Label(text=instructions.txt_instruction,size_hint=(1,1),halign='left')
        self.button = Button(text='Начать',pos_hint={'center_x': 0.5, 'center_y': 0.5},size_hint=(0.3,0.2))
        self.button.on_press = self.next
        self.name_l = Label(text='Введите имя:')
        self.age_l = Label(text='Введите возраст:')
        self.name_ti = TextInput(multiline=False)
        self.age_ti = TextInput(multiline=False)
        # self.name_ti.set_disabled(True)
        
        self.layout1 =  BoxLayout(size_hint=(1,0.075),pos_hint={'center_x': 0.42, 'center_y': 0.5},padding=[100,0,120,0])
        self.layout1.add_widget(self.name_l)
        self.layout1.add_widget(self.name_ti)

        self.layout2 =  BoxLayout(size_hint=(1,0.075),pos_hint={'center_x': 0.42, 'center_y': 0.5},padding=[100,0,120,0])
        self.layout2.add_widget(self.age_l)
        self.layout2.add_widget(self.age_ti)

        self.main_layout = BoxLayout(orientation ='vertical',spacing=8,padding=6)
        self.main_layout.add_widget(self.instruct_l)
        self.main_layout.add_widget(self.layout1)
        self.main_layout.add_widget(self.layout2)
        self.main_layout.add_widget(self.button)

        self.add_widget(self.main_layout)

    def next(self):
        global name , age
        name = self.name_ti.text

        age = check_int(self.age_ti.text)
        if age == False or age < 7:
            age = 0
            self.age_ti.text = str(age)
            print('Inavalid data for age')
        else:
            self.manager.transition.direction = 'left'
            self.manager.current = 'PulseCheck1'


class PulseCheck1(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.next_screen = False

        self.instruct_l = Label(text=instructions.txt_test1,size_hint=(1,1),pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.lbl_sec = seconds.Seconds(15)
        self.lbl_sec.bind(done=self.sec_finished)
        self.btn = Button(text='Начать',pos_hint={'center_x': 0.5, 'center_y': 0.5},size_hint=(0.3,0.4))
        self.btn.on_press = self.next
        self.result_l = Label(text='Введите результат:')
        self.result_ti = TextInput(multiline=False,text='0')
        self.result_ti.set_disabled(True)
        
        self.layout1 =  BoxLayout(size_hint=(1,0.15),pos_hint={'center_x': 0.42, 'center_y': 0.5},padding=[100,0,120,0])
        self.layout1.add_widget(self.result_l)
        self.layout1.add_widget(self.result_ti)


        self.main_layout = BoxLayout(orientation ='vertical',spacing=8,padding=6)
        self.main_layout.add_widget(self.instruct_l)
        self.main_layout.add_widget(self.lbl_sec)
        self.main_layout.add_widget(self.layout1)
        self.main_layout.add_widget(self.btn)

        self.add_widget(self.main_layout)
    def sec_finished(self,*args):
        self.result_ti.set_disabled(False)
        self.btn.set_disabled(False)
        self.btn.text = 'Продолжить'
        self.next_screen = True
    
    def next(self):
        global P1
        if not self.next_screen:
            self.btn.set_disabled(True)
            self.lbl_sec.start()
        else:
            P1 = check_int(self.result_ti.text)
            if P1 == False or P1 <= 0:
                P1 = 0
                self.result_ti.text = str(P1)
                print('Inavalid data')
            else:
                self.manager.transition.direction = 'left'
                self.manager.current = 'SitsScreen'              


class SitsScreen(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.instruct_l = Label(text=instructions.txt_sits,size_hint=(1,1),pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.button = Button(text='Продолжить',pos_hint={'center_x': 0.5, 'center_y': 0.5},size_hint=(0.5,0.2))
        self.button.on_press = self.next

        self.main_layout = BoxLayout(orientation ='vertical',spacing=8,padding=6)
        self.main_layout.add_widget(self.instruct_l)
        self.main_layout.add_widget(self.button)

        self.add_widget(self.main_layout)
    
    def next(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'PulseCheck2'

class PulseCheck2(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.stage = 0
        self.instruct_l = Label(text=instructions.txt_test3,size_hint=(1,1),pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.lbl_task = Label(text='Считайте пульс')
        self.lbl_sec = seconds.Seconds(15)
        self.lbl_sec.bind(done=self.sec_finished)
        self.btn = Button(text='Начать',pos_hint={'center_x': 0.5, 'center_y': 0.5},size_hint=(0.3,0.5))
        self.btn.on_press = self.next
        self.result_l = Label(text='Результат:')
        self.after_rest_l = Label(text='Результат после отдыха:')
        self.result_ti = TextInput(multiline=False,text='0')
        self.after_rest_ti = TextInput(multiline=False,text='0')
        self.result_ti.set_disabled(True)
        self.after_rest_ti.set_disabled(True)
        
        self.layout1 =  BoxLayout(size_hint=(1,0.23),pos_hint={'center_x': 0.42, 'center_y': 0.5},padding=[100,0,120,0])
        self.layout1.add_widget(self.result_l)
        self.layout1.add_widget(self.result_ti)

        self.layout2 =  BoxLayout(size_hint=(1,0.23),pos_hint={'center_x': 0.42, 'center_y': 0.5},padding=[100,0,120,0])
        self.layout2.add_widget(self.after_rest_l)
        self.layout2.add_widget(self.after_rest_ti)

        self.main_layout = BoxLayout(orientation ='vertical',spacing=8,padding=6)
        self.main_layout.add_widget(self.instruct_l)
        self.main_layout.add_widget(self.lbl_task)
        self.main_layout.add_widget(self.lbl_sec)
        self.main_layout.add_widget(self.layout1)
        self.main_layout.add_widget(self.layout2)
        self.main_layout.add_widget(self.btn)

        self.add_widget(self.main_layout)

    def sec_finished(self,*args):
        if self.lbl_sec.done:
            if self.stage == 0:
                self.stage = 1
                self.lbl_sec.restart(30)
                self.result_ti.set_disabled(False)
                self.lbl_task.text = 'Отдохните 30 секунд'
            elif self.stage == 1:
                self.stage = 2
                self.lbl_sec.restart(15)
                self.lbl_task.text = 'Считайте пульс'
            elif self.stage == 2:
                self.btn.text = 'Завершить'
                self.after_rest_ti.set_disabled(False)
                self.btn.set_disabled(False)
    
    def next(self):
        global P2,P3
        if self.stage == 0:
            self.btn.set_disabled(True)
            self.lbl_sec.start()
        else:
            P2 = check_int(self.result_ti.text)
            P3 = check_int(self.after_rest_ti.text)
            if P2 == False or P2 <= 0:
                P2 = 0
                self.result_ti.text = str(P2)
                print('Inavalid data')
            elif P3 == False or P3 <= 0:
                P3 = 0
                self.after_rest_ti.text = str(P3)
                print('Inavalid data')
            else:
                self.manager.transition.direction = 'left'
                self.manager.current = 'Result'             


class Result(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        
        self.result_l = Label(text='')
        self.on_enter = self.before

        self.add_widget(self.result_l)
        
    
    def before(self):
        ruff_index,conclusion  = ruffier.main(P1,P2,P3,age)
        final_str =f"{name}\nВаш індекс Руф'є: {ruff_index}\n{conclusion}"
        self.result_l.text = final_str
    

class RuffieApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InstructionScreen(name='InstructionScreen'))
        sm.add_widget(PulseCheck1(name='PulseCheck1'))
        sm.add_widget(SitsScreen(name='SitsScreen'))
        sm.add_widget(PulseCheck2(name='PulseCheck2'))
        sm.add_widget(Result(name='Result'))
        return  sm

app = RuffieApp()
app.run()





# from kivy.uix.label import Label
# from kivy.uix.popup import Popup
# from kivy.app import App
# # create the popup
# popup = Popup(title='My Title',
#               content=Label(text='My Message'),
#               size_hint=(None, None), size=(400, 400))

# # open the popup
# popup.open()
# app = App()
# app.run()

