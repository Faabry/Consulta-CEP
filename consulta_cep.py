import requests
import PySimpleGUI as sg
from PySimpleGUI import Push

sg.theme("Dark Amber")
cep = [
    [sg.Text("Consulta CEP", font="Times 40 bold")],
    [Push(),
     sg.Text("Informe um CEP"),
     Push()],

    [Push(),
     sg.Input(key="-cep-", size=8),
     Push()],

    [sg.Text("Logradouro:", size=9),
     sg.Input(key="-logradouro-", size=35)],

    [sg.Text("Bairro:", size=9), 
     sg.Input(key="-bairro-", size=(30, 2))],

    [sg.Text("Localidade:", size=9), 
     sg.Input(key="-local-", size=20)],

    [sg.Text("UF:", size=9),
     sg.Input(key="-uf-", size=2)],

    [sg.Text()],
    
    [
     sg.Button("Consultar", key="-consultar-", size=15),
     sg.Button("Sair", key="-sair-", size=10)
     ]
]


window = sg.Window("Developed By Airton Fabre", font="Times 25", size=(700, 600), border_depth=9,
                    layout=cep, grab_anywhere=True)

while True:
    events, values = window.read()

    if events == sg.WIN_CLOSED or events == "-sair-":
        break
    elif events == "-consultar-":
        try:
            cep = values["-cep-"]
            request = requests.get(f"http://viacep.com.br/ws/{cep}/json/")
            adress = request.json()
            window["-logradouro-"].update(adress["logradouro"])
            window["-bairro-"].update(adress["bairro"])
            window["-local-"].update(adress["localidade"])
            window["-uf-"].update(adress["uf"])
        except:
            window["-logradouro-"].update("CEP INVÁLIDO")