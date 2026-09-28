
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
import random
import time

Window.clearcolor = get_color_from_hex("#0f111a")

class AviatorPredictor(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 15
        
        self.history = [1.23, 2.45, 1.05, 8.32, 1.11, 3.44, 1.89, 12.5, 2.1, 1.02]
        
        self.add_widget(Label(text="[b]AVIATOR PREDICTOR[/b]", markup=True, font_size='28sp', color=(1,0.2,0.2,1), size_hint_y=0.15))
        self.add_widget(Label(text="AI Pattern Analyzer v2.1", font_size='14sp', color=(0.6,0.6,0.7,1), size_hint_y=0.05))
        
        self.prediction_label = Label(text="2.15x", font_size='72sp', bold=True, color=(0,1,0.6,1), size_hint_y=0.3)
        self.add_widget(self.prediction_label)
        
        self.status_label = Label(text="Confidence: 87%\nSignal: STRONG BUY", markup=False, font_size='16sp', color=(0.8,0.8,0.8,1), size_hint_y=0.15)
        self.add_widget(self.status_label)
        
        history_text = "History: " + " | ".join([f"{x:.2f}x" for x in self.history[-6:]])
        self.history_label = Label(text=history_text, font_size='12sp', color=(0.5,0.5,0.6,1), size_hint_y=0.1)
        self.add_widget(self.history_label)
        
        btn_layout = BoxLayout(size_hint_y=0.2, spacing=10)
        self.predict_btn = Button(text="GET NEXT SIGNAL", background_color=(1,0.2,0.2,1), font_size='18sp', bold=True)
        self.predict_btn.bind(on_press=self.generate_prediction)
        btn_layout.add_widget(self.predict_btn)
        self.add_widget(btn_layout)
        
        self.add_widget(Label(text="Disclaimer: For entertainment only.\nAviator uses RNG - cannot be 100% predicted.\nPlay responsibly.", font_size='10sp', color=(0.5,0.5,0.5,1), size_hint_y=0.15, halign='center'))

    def generate_prediction(self, instance):
        self.predict_btn.text = "ANALYZING..."
        self.predict_btn.disabled = True
        Clock.schedule_once(self.show_result, 1.5)

    def show_result(self, dt):
        # Fake "AI" logic - weighted random based on history
        avg = sum(self.history)/len(self.history)
        if avg < 2.0:
            pred = random.uniform(2.0, 5.5)
            conf = random.randint(78, 92)
        else:
            pred = random.uniform(1.2, 3.8)
            conf = random.randint(65, 85)
        
        # Occasionally show high multiplier
        if random.random() < 0.15:
            pred = random.uniform(8.0, 25.0)
            conf = random.randint(55, 70)

        self.prediction_label.text = f"{pred:.2f}x"
        
        if pred > 5:
            self.prediction_label.color = (1,0.8,0,1)
            signal = "HIGH RISK / HIGH REWARD"
        elif pred > 2:
            self.prediction_label.color = (0,1,0.6,1)
            signal = "STRONG BUY"
        else:
            self.prediction_label.color = (1,0.5,0.2,1)
            signal = "WAIT - LOW"

        self.status_label.text = f"Confidence: {conf}%\nSignal: {signal}\nUpdated: {time.strftime('%H:%M:%S')}"
        
        self.history.append(pred)
        if len(self.history) > 20:
            self.history.pop(0)
        self.history_label.text = "History: " + " | ".join([f"{x:.2f}x" for x in self.history[-6:]])
        
        self.predict_btn.text = "GET NEXT SIGNAL"
        self.predict_btn.disabled = False

class AviatorApp(App):
    def build(self):
        return AviatorPredictor()

if __name__ == '__main__':
    AviatorApp().run()
