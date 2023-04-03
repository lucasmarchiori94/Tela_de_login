from PySimpleGUI import PySimpleGUI as sg

#layout
sg.theme('Reddit')
layout  = [
    [sg.Text('Usuário'),sg.Input(key='usuario',size=(20,1))],
    [sg.Text('Senha'),sg.Input(key='senha',password_char='*',size=(20,1))],
    [sg.Checkbox('salvar o login')],
    [sg.Button('Entrar')]
]
#Janela
janela = sg.Window('Tela de login',layout)
#Ler os Eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'lucas' and valores['senha']== '123456':
            print('Bem vindo')
