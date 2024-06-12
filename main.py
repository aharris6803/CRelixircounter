from pynput import keyboard as pynput_keyboard
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image

time = 0
elixir = 7
gameover = False


def timer(dt):
    global time
    time += 1


def elixiradd(dt):
    global time, elixir
    elixir += 1 + int(time/120)
    if elixir > 10:
        elixir = 10


def display(dt, elixir_widgets):
    global elixir
    if not gameover:
        for widget in elixir_widgets:
            widget.source = f"image_{int(elixir)}.png"


class MyKeyboardListener(App):
    def build(self):
        elixir_layout = BoxLayout(orientation='horizontal')
        elixir_widgets = []

        for i in range(10):
            elixir_image = Image(source="", size_hint=(None, None), size=(800, 170), allow_stretch=True)
            elixir_layout.add_widget(elixir_image)
            elixir_widgets.append(elixir_image)

        Clock.schedule_interval(timer, 1)
        Clock.schedule_interval(elixiradd, 2.8)
        Clock.schedule_interval(lambda dt: display(dt, elixir_widgets), 0.5)

        listener = pynput_keyboard.Listener(on_press=self.on_press)
        listener.start()

        return elixir_layout

    def on_press(self, key):
        try:
            if key.char == '0':
                self.game_over()
            elif key.char.isdigit():
                self.decrease_elixir(int(key.char))
        except AttributeError:
            pass

    def game_over(self):
        global gameover
        gameover = True

    def decrease_elixir(self, amount):
        global elixir
        elixir -= amount
        if elixir < 0:
            elixir = 0
        print("Elixir Decreased. Current Elixir:", elixir)


if __name__ == "__main__":
    MyKeyboardListener().run()
