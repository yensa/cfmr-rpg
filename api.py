from API.Application import Application
from API.Window import Window


app = Application()

window = Window(config={"caption": "Hello World", "icon": "/home/romain/Documents/Projects/workspace/cfmr-rpg/resources/textures/icon.png"})
app.register_window(window)

app.run()