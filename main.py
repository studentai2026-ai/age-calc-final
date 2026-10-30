from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from datetime import datetime
import threading
import time

Window.clearcolor = get_color_from_hex('#1E1E2E')

class AgeCalculatorApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=30, spacing=15)
        
        self.title_label = Label(text='🎂 حاسبة العمر', font_size='26sp', color=get_color_from_hex('#CBA6F7'), size_hint_y=0.15)
        layout.add_widget(self.title_label)
        
        self.input = TextInput(hint_text='أدخل سنة ميلادك', multiline=False, font_size='20sp', size_hint_y=0.12, background_color=get_color_from_hex('#313244'), foreground_color=get_color_from_hex('#CDD6F4'), padding=[15, 15])
        layout.add_widget(self.input)
        
        self.btn = Button(text='احسب ✨', font_size='22sp', size_hint_y=0.12, background_color=get_color_from_hex('#89B4FA'), background_normal='')
        self.btn.bind(on_press=self.calculate)
        layout.add_widget(self.btn)
        
        self.progress = ProgressBar(max=100, value=0, size_hint_y=0.08)
        layout.add_widget(self.progress)
        
        self.result_label = Label(text='أدخل سنتك...', font_size='18sp', color=get_color_from_hex('#A6ADC8'), size_hint_y=0.53, halign='center')
        self.result_label.bind(size=self.result_label.setter('text_size'))
        layout.add_widget(self.result_label)
        return layout

    def calculate(self, instance):
        year_str = self.input.text.strip()
        if not year_str.isdigit():
            self.result_label.text = "⚠️ أدخل أرقاماً فقط"
            return
        year = int(year_str)
        current_year = datetime.now().year
        if year > current_year or year < 1900:
            self.result_label.text = "⚠️ سنة غير واقعية"
            return
            
        self.result_label.text = "⏳ جاري الحساب..."
        threading.Thread(target=self.logic, args=(year, current_year), daemon=True).start()

    def logic(self, year, current_year):
        for i in range(101):
            time.sleep(0.01)
            self.progress.value = i
        age = current_year - year
        self.progress.value = min((age / 100) * 100, 100)
        self.result_label.text = f"عمرك: {age} سنة\nستبلغ 100 عام في: {year + 100}"

if __name__ == '__main__':
    AgeCalculatorApp().run()
