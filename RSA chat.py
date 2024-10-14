import PySimpleGUI as sg
from sympy import randprime

board = 225*"-"

def _onKeyRelease(event):
    ctrl  = (event.state & 0x4) != 0
    if event.keycode==88 and  ctrl and event.keysym.lower() != "x":
            event.widget.event_generate("<<Cut>>")

    if event.keycode==86 and  ctrl and event.keysym.lower() != "v":
        event.widget.event_generate("<<Paste>>")

    if event.keycode==67 and  ctrl and event.keysym.lower() != "c":
        event.widget.event_generate("<<Copy>>")

    if event.keycode==65 and  ctrl and event.keysym.lower() != "a":
        event.widget.event_generate("<<SelectAll>>")

def calc_d(e: int, fi: int) -> int:
    d = 10 
    while (d * e) % fi != 1:
        d += 1
    return d

def RSAalgorithm(key_name: str, text_name, func,  elem_name: str, sep=""):
    try:
        div, mod = values[key_name].split()
        div, mod = int(div), int(mod)

        l = values[text_name]
        if text_name == "text-to-translate":
            l = l.split()

        result = ""
        for el in l:
            result = result + func(el, div, mod) + sep
        window.FindElement(elem_name).Update(result)
    except Exception as e:
        window.FindElement(elem_name).Update(e)

layout = [  
    [sg.Button('Generate keys')],
    [sg.Text('Open key', size=(10,1)), sg.Text(key="gened-open-key")],
    [sg.Text('Close key', size=(10,1)), sg.Text(key="gened-close-key")],
    [sg.Text(board, font=("Helvetica", 4))],
    [sg.Text('Enter open key', size=(15,1)), sg.InputText(key='open-key')],
    [sg.Text('Enter text', size=(15,1)), sg.InputText(key="text-to-crypt")],
    [sg.Button('Crypte')],
    [sg.Text('Crypted text')], 
    [sg.Output(key='_crypte_', size=(61,1))],    
    [sg.Text(board, font=("Helvetica", 4))],
    [sg.Text('Enter close key', size=(15,1)), sg.InputText(key="close-key")],
    [sg.Text('Enter crypted text', size=(15,1)), sg.InputText(key="text-to-translate")],
    [sg.Button('Translate')],
    [sg.Text('Translated text')],
    [sg.Output(key='_translate_', size=(61,1))]
]

window = sg.Window('RSA chat', layout, use_default_focus=False, finalize=True)
window.TKroot.bind_all("<Key>", _onKeyRelease, "+")

while True:                             # The Event Loop
    event, values = window.read()
    # print(event, values) #debug

    if event in (None, 'Exit', 'Cancel'):
        break

    if event == 'Generate keys':  
        try : 
            p = randprime(10 ** 2, 10 ** 5)
            q = randprime(10 ** 2, 10 ** 5)
            n = p * q
            fi = (p-1) * (q-1)
            e = randprime(1000, fi)
            d = calc_d(e, fi)

            window.FindElement('gened-open-key').Update(str(e) + " " + str(n))        
            window.FindElement('gened-close-key').Update(str(d) + " " + str(n))    
        except Exception as e:
            window.FindElement('gened-open-key').Update(e)                    

    if event == 'Crypte' and values["open-key"] != "" and values["text-to-crypt"] != "":  
        RSAalgorithm("open-key", "text-to-crypt", lambda x, y, z: str(ord(x) ** y % z), "_crypte_", ' ')   

    if event == 'Translate' and values["close-key"] != "" and values["text-to-translate"] != "":    
        RSAalgorithm("close-key", "text-to-translate", lambda x, y, z: chr(int(x) ** y % z), "_translate_")   

window.close()