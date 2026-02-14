from guizero import App, Text, TextBox, PushButton, Slider, Picture, Combo, CheckBox, ButtonGroup

def punch_line():
    message.value = "Because the sea weed!"

def change_text_size(slider_value):
    sample_text.size = int(slider_value)

def update_text():
    output_text.value = my_name.value

app = App(title = "Hello World")
welcome_message = Text(
        app, 
        text="Welcome to My App!",
        size = 40,
        color = "lightblue",
        font = "Arial"
    )
my_name = TextBox(app)
output_text = Text(app, text="???")
button = PushButton(app, text="Display it", command = update_text)
message = Text(app, text="Why did the starfish blush?")
update_text = PushButton(
        app,
        command = punch_line,
        text = "Answer"
    )
sample_text = Text(app, text="Sample Text")
text_size = Slider(
        app,
        command = change_text_size,
        start = 10,
        end = 80
    )

banner = Picture(app, image="documentingbanner.png")
film_choice = Combo(app, options=["Inception", "The Matrix", "Interstellar", "The Godfather"])
vip_seat = CheckBox(app, text="VIP Seat?")
row_choice = ButtonGroup(
        app,
        options=[["Front", "F"], ["Middle", "M"], ["Back", "B"]],
        selected="M",
        horizontal=True
    )
app.display()