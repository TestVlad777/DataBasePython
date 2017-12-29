"""
документирование
"""


from kivy.app import App

class WeatherApp(App):  # создаем подкласс класса App с именем WeatherApp (на протяжении уроков мы будем разрабатывать приложение связанное с погодой, это его начало)

    pass

if __name__ == "__main__":
    WeatherApp().run()





# BoxLayout:  # root widget
#     Label:
#         text: 'Hello'
#     Label:
#         text: 'Beautiful'
#     Label:
#         text: 'World'





# from kivy.app import App
# from kivy.clock import Clock, _default_time as time  # ok, no better way to use the same clock as kivy, hmm
# from kivy.lang import Builder
# from kivy.factory import Factory
# from kivy.properties import ListProperty

# MAX_TIME = 1/60.

# kv = '''
# BoxLayout:
#     ScrollView:
#         GridLayout:
#             cols: 1
#             id: target
#             size_hint: 1, None
#             height: self.minimum_height
#     BoxLayout:
#         orientation: 'vertical'
#         Button:
#             text: 'add 10'
#             on_press: app.consommables.extend(range(10))
#         Button:
#             text: 'add 100'
#             on_press: app.consommables.extend(range(100))
#         Button:
#             text: 'add 1000'
#             on_press: app.consommables.extend(range(1000))
#         Button:
#             text: 'clear'
#             on_press: target.clear_widgets()
# <MyLabel@Label>:
#     size_hint_y: None
#     height: self.texture_size[1]
# '''


# class ProdConApp(App):
#     consommables = ListProperty([])

#     def build(self):
#         Clock.schedule_interval(self.consume, 0)
#         return Builder.load_string(kv)

#     def consume(self, *args):
#         while self.consommables and time() < (Clock.get_time() + MAX_TIME):
#             item = self.consommables.pop(0)  # i want the first one
#             label = Factory.MyLabel(
#                 text='%s : %s : %s' % (item, Clock.get_time(), time()))
#             self.root.ids.target.add_widget(label)


# if __name__ == '__main__':
#     ProdConApp().run()









# import kivy
# kivy.require('1.0.6')  # replace with your current kivy version !

# from kivy.app import App
# from kivy.uix.button import Button


# class MyApp(App):

#     def build(self):
#         return Button(text='Hello World')


# if __name__ == '__main__':
#     MyApp().run()
















# import random
# import database
# import main_windows
# from tkinter import *


# WWW = ('111', '222', '333')
# print(random.choice(WWW))


# base = database.DataBase()
# base.test_func()



# #main_windows.set_text_button()




# root = Tk()
# root.title("GUI на Python")
# root.geometry("300x250")
# root.mainloop()

# print("end")