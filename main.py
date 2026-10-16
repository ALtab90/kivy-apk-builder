__version__ = "1.0.0"

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class MyApp(App):
    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=20
        )

        layout.add_widget(
            Label(text="Hello! My First Android App")
        )

        button = Button(text="Click Me")
        button.bind(
            on_press=lambda instance:
            setattr(instance, "text", "It Works!")
        )

        layout.add_widget(button)
        return layout


MyApp().run()
