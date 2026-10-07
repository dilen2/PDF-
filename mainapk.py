from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton


class TestApp(MDApp):
    def build(self):
        screen = MDScreen()

        btn = MDRaisedButton(
            text="PDF智能工具箱",
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )

        screen.add_widget(btn)

        return screen


TestApp().run()