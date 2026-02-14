from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

        # Create button
        self.generate_btn = Button(
            text="Generate",
            font_size=24,
            size=(200, 60),
            size_hint=(None, None)
        )
        self.generate_btn.bind(on_press=self.on_generate)

        # Add button to layout
        self.add_widget(self.generate_btn)

    def on_generate(self, instance):
        print("Generate button clicked!")
        # Put your pipeline trigger here (audio, image, video generation)
        # call_your_pipeline_function()


class MyApp(App):
    def build(self):
        return MainLayout()


if __name__ == "__main__":
    MyApp().run()
