import PySimpleGUI as sg
import prediction

sg.theme('DarkAmber')  # Add a touch of color
# All the stuff inside your window.
layout = [
    [sg.Text('Enter the news you want to check : '), sg.InputText()],
    [sg.Button('Enter')],
    [sg.Text('Fake Image Detection'), sg.InputText()], [sg.FileBrowse('Upload Image')], [sg.Button('Cancel')]]

# Create the Window
window = sg.Window('Fake news/image Detection').Layout(layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()

    if event in (True, 'Enter'):
        print('You entered ', values[0])
        truth, prob = prediction.detecting_fake_news(values[0])
        sg.Popup("The given statement is ", truth,
                 "The truth probability score is ", prob)
    if event in (True, 'Upload Image'):
        print('Image entered ', values[1])
    if event in (None, 'Cancel'):  # if user closes window or clicks cancel
        break
sg.Popup(event, values)
window.close()
