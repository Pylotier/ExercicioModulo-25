# 25.	Receba a hora de início e de final de um jogo (HH,MM), calcular o tempo do jogo em horas e minutos, sabendo que o tempo máximo é menor que 24 horas e pode começar num dia e terminar noutro.

#Declarar as váriaveis
HJ: int = 0
MJ: int = 0
minutosTotais: int = 0
terminoHJ: int = 0
terminoMJ: int = 0
minutosTotaisTermino: int = 0
preResultadoH: int = 0
resultadoHJ: int = 0
resultadoMJ: int = 0

#Inicio
def main():
    global HJ
    global MJ
    global terminoHJ
    global terminoMJ

    HJ = int(input("Digite as horas no começo do jogo: "))
    MJ = int(input("Digite os minutos no começo do jogo: "))
    terminoHJ = int(input("Digite as horas no termino do jogo: "))
    terminoMJ = int(input("Digite os minutos no termino do jogo: "))

    HorasParaMinutos()
    LogicaHorario()

def HorasParaMinutos():
    global minutosTotais
    global minutosTotaisTermino

    minutosTotais = HJ*60+MJ
    minutosTotaisTermino = terminoHJ*60+terminoMJ

def LogicaHorario():
    global minutosTotaisTermino
    global minutosTotais

    if (minutosTotaisTermino == minutosTotais):
        if ((minutosTotaisTermino + 1440) - minutosTotais >= 1440):
            print("Tempo limite de 24 horas atingido")
    else:
        if (minutosTotais > minutosTotaisTermino):
            SeHJMaior()
        elif (minutosTotais < minutosTotaisTermino):
            SeTermHJMaior()
        else:
            print("Erro")

def SeHJMaior():
    global preResultadoH
    global minutosTotais
    global minutosTotaisTermino
    global resultadoHJ
    global resultadoMJ

    preResultadoH = (minutosTotaisTermino + 1440) - minutosTotais
    resultadoMJ = preResultadoH%60
    resultadoHJ = (preResultadoH - resultadoMJ) / 60
    print("Horas de jogo:", resultadoHJ, ":", resultadoMJ)

def SeTermHJMaior():
    global preResultadoH
    global minutosTotais
    global minutosTotaisTermino
    global resultadoHJ
    global resultadoMJ

    preResultadoH = minutosTotaisTermino - minutosTotais
    resultadoMJ = preResultadoH % 60
    resultadoHJ = (preResultadoH - resultadoMJ) / 60
    print("Horas de jogo:", resultadoHJ, ":", resultadoMJ)

#Fim

if (__name__ == "__main__"):
    main();