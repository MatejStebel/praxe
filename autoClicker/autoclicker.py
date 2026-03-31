from kivy.core.window import Window
from kivy.clock import Clock
from kivy.app import App
from kivy.uix.widget import Widget
import pyautogui

class AutoClicker(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.clicking = False
        self.click_interval = 0.1
        Window.bind(on_key_down=self.on_key_down)
        Window.bind(on_key_up=self.on_key_up)
        self.keys_pressed = set()
        self.clicks = 0
        self.label = self.ids.label
        self.interval = self.ids.click_interval
        self.button = self.ids.button
    
    def on_key_down(self, window, key, scancode, codepoint, modifiers):
        self.keys_pressed.add(key)

    def on_key_up(self, window, key, *args):
        self.keys_pressed.discard(key)
    
    def update(self, dt):
        if 273 in self.keys_pressed:  # Shift key
            self.clicking = True
        if 274 in self.keys_pressed:  # Control key
            self.clicking = False
            self.clicks = 0 

        if self.clicking:
            pyautogui.click(interval = self.click_interval)
            self.clicks += 1
            self.label.text = f"Mouse Position: \n{pyautogui.position()}\nClicks: {self.clicks}"
        
        if self.button.clicked:
            self.click_interval = float(self.interval.text)


class AutoClickerApp(App):
    def build(self):   
        game = AutoClicker()
        Clock.schedule_interval(game.update, 1.0 / 120.0)  # Run game at 60 FPS
        return game

if __name__ == "__main__":
    AutoClickerApp().run()