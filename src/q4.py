"Ligar o primeiro interruptor e aguardar algum tempo" 
"desligar o primeiro interruptor e ligar o segundo interruptor" 
"A lâmpada acesa estará conectada ao segundo interruptor" 
"A lâmpada apagada e quente estará conectada ao primeiro interruptor"
"A lâmpada apagada e fria estará conectada ao terceiro interruptor"

def descobrir_interruptores_lampadas():
    # Inicializar os interruptores e lâmpadas
    interruptor1 = False
    interruptor2 = False
    interruptor3 = False

    # Primeira etapa
    interruptor1 = True
    interruptor1 = False
    interruptor2 = True

    # Segunda etapa (entrando na sala)
    lampada_acesa = None

    # Verificar qual lâmpada está acesa
    if interruptor2:
        lampada_acesa = 2
    elif interruptor1:
        lampada_acesa = 1

    # Imprimir os resultados
    print(f'O interruptor 1 controla a lâmpada {3 if lampada_acesa == 2 else 1}')
    print(f'O interruptor 2 controla a lâmpada {lampada_acesa}')
    print(f'O interruptor 3 controla a lâmpada {3 if lampada_acesa == 1 else 1}')

descobrir_interruptores_lampadas()
