def banco(C,N,tempos):
    if N < C:
        print('1-2 ', end='')
        return 0
    else:
        print('1-3 ', end='')
        cont = 0
        termina = [tempos[0][0]+tempos[0][1]]
        caixas = C - 1
        
        print('3-4 ', end='')
        for i in range(1,N):
            print('4-6 ', end='')
            termina.sort()
            
            print('6-7 ', end='')
            entrou = False
            while termina[0] < tempos[i][0]:
                entrou = True
                print('7-8 ', end='')
                del termina[0]
                caixas = caixas + 1
                if termina == []:
                    print('8-10 ', end='')
                    break

                print('8-9 ', end='')
                print('9-7 ', end='')

            if not entrou: 
                print('7-10 ', end='')

            ultimo = None
            if caixas > 0:
                print('10-11 ', end='')
                ultimo = '11'
                caixas = caixas - 1
                termina = termina + [tempos[i][0]+tempos[i][1]]
                               
            else:
                print('10-12 ', end='')
                ultimo = '12'
                atendimento = min(termina)
                termina.remove(min(termina))
                termina =  termina + [atendimento+tempos[i][1]]
                if atendimento - tempos[i][0] >= 20:
                    print('12-13 ', end='')
                    ultimo = '13'
                    cont = cont +1
            print(ultimo, end='')
            print('-15 ', end='')
            print('15-4 ', end='')
        print('4-5 ', end='')
        return cont           
    

def main():
    C, N = input().split()
    C = int(C)
    N = int(N)

    tempos = []
    for i in range(N):
        tempos = tempos + [input().split()]
        tempos[i][0] = int(tempos[i][0])
        tempos[i][1] = int(tempos[i][1])


    print()
    print('caminho: ', end='')        
    a = banco(C,N,tempos)
    print()
    print('resultado: ', a)


main()
