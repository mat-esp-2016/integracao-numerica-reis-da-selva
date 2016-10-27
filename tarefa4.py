lista_N =[] #listas vazias onde serão adicionadas os valores das variáveis 
erro_retangulo = []
erro_trapezio = []
# Dessa vez vamos precisar da biblioteca matemática "math"
# Ela define funções como sin, cos, tan, exp e constantes como pi
import math
import matplotlib.pyplot as plt
inicio = 0
fim = math.pi/2 # Funções trigonométricas utilizam ângulos em radianos!
for N in range(10, 1010, 10): #geração dos valores de N e sequencias
    intervalo = (fim - inicio)/(N-1)
    dados = []
    tempos = []
    lista_N.append(N) #adição dos valores de N a lista_N
    for d in range(N): #geração dos dados
        t = inicio + d*intervalo #valores de tempo
        tempos.append(t) #adição dos valores de tempo
        dados.append(math.cos(t)) # adiçãos dos valores de tempo à lista
    soma1 = 0
    for r in range(0, N, 1): #Loop calculo da regra dos retângulos
        soma1 = soma1 + intervalo*dados[r] #cálculo da regra dos retângulos
        erro1 = abs(1-soma1) #cálculo do erro da regra dos retângulos
    erro_retangulo.append(erro1) # adição dos valores dos erros na lista de erro dos retângulos
    soma2 = 0
    for t in range(0, N-1, 1): #Loop calculo da regra dos trapézios
        soma2 = soma2 + intervalo*(dados[t]+dados[t+1])/2 #calculo da regra dos trapezios
        erro2 = abs(1-soma2) # calculo do erro da regra dos trapezios
    erro_trapezio.append(erro2) #adição dos valores dos erros na lista de erro dos trapézios

    plt.figure()
plt.plot(lista_N, erro_retangulo,'-b', label='Retângulos')
plt.plot(lista_N, erro_trapezio, '-r', label='Trapézios')
plt.title('Erro de integração numérica')
plt.xlabel('Número de Dados')
plt.yscale('log')
plt.ylabel('Erro')
legenda = plt.legend(loc = 'upper right', shadow = True, fontsize= 'x-large' )
plt.savefig('tarefa4.png')