from pynput.keyboard import Key, Controller
import time
class principal:
    def __init__(self, tempo, ativa_ou_cancela):
        self.tempo = tempo
        self.ativa_ou_cancela = ativa_ou_cancela
            # 1= ativa
            # 0= desativa
        if(ativa_ou_cancela == 1):
            teclado = Controller()
            teclado.press(Key.cmd)
            teclado.press('r')
            teclado.release('r')
            teclado.release(Key.cmd)
            time.sleep(1)
            teclado.press(Key.enter)
            time.sleep(1)
            teclado.release(Key.enter)
            teclado.type(f'shutdown -s -t {tempo}')
            teclado.press(Key.enter)
            teclado.release(Key.enter)
            time.sleep(2)
            teclado.press(Key.alt)
            teclado.press(Key.f4)
            teclado.release(Key.f4)
            teclado.release(Key.alt)
        else:
            ativa_ou_cancela = 0
            teclado = Controller()
            teclado.press(Key.cmd)
            teclado.press('r')
            teclado.release('r')
            teclado.release(Key.cmd)
            time.sleep(1)
            teclado.press(Key.enter)
            time.sleep(1)
            teclado.release(Key.enter)
            teclado.type('shutdown -a')
            teclado.press(Key.enter)
            teclado.release(Key.enter)
            time.sleep(2)
            teclado.press(Key.alt)
            teclado.press(Key.f4)
            teclado.release(Key.f4)
            teclado.release(Key.alt)
traço = '-'
teclado = Controller()

print(traço*60 + '\n'*2 + "             TEMPORIZADOR DO MARCU              " +  '\n'*2 + traço*60)

try:
    opcao = int(input('Digite 1 para inciar o temporizador \n           Ou \nDigite 0 para cancelar um temporizador agendado \n : '))
    if(opcao == 0):
        tempo = 200
    else:
        tempo = int(input('Agora digite o tempo em segundos para desligar seu computador: \nOBS: 1h equivale a 3600s \n : '))
    
except ValueError as erro:
    print(
    '''
        ERRO:\n 
        Digite um numero inteiro e tente novamente!
    '''
    )
    print('fechando em 5 segundos')
    time.sleep(5)
    teclado.press(Key.alt)
    teclado.press(Key.f4)
    teclado.release(Key.f4)
    teclado.release(Key.alt)

processar = principal(tempo, opcao)