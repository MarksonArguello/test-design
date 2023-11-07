def banco(C,N,tempos):
    print('1 ', end='')
    if N < C:
        print('2 ', end='')
        return 0
    else:
        print('3 ', end='')
        cont = 0
        termina = [tempos[0][0]+tempos[0][1]]
        caixas = C - 1
        
        print('4 ', end='')
        for i in range(1,N):
            print('6 ', end='')
            termina.sort()
            
            print('7 ', end='')
            while termina[0] < tempos[i][0]:
                print('8 ', end='')
                del termina[0]
                caixas = caixas + 1
                if termina == []:
                    break

                print('9 ', end='')
                print('7 ', end='')

            print('10 ', end='')
            if caixas > 0:
                print('11 ', end='')
                caixas = caixas - 1
                termina = termina + [tempos[i][0]+tempos[i][1]]
                               
            else:
                print('12 ', end='')
                atendimento = min(termina)
                termina.remove(min(termina))
                termina =  termina + [atendimento+tempos[i][1]]
                if atendimento - tempos[i][0] >= 20:
                    print('13 ', end='')
                    cont = cont +1

            print('15 ', end='')
            print('4 ', end='')
        print('5 ', end='')
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
