pairs = set()

def banco(C,N,tempos):
    if N < C:
        print('1-2 ', end='')
        pairs.add('1-2')
        return 0
    else:
        print('1-3 ', end='')
        pairs.add('1-3')
        cont = 0
        termina = [tempos[0][0]+tempos[0][1]]
        caixas = C - 1
        
        print('3-4 ', end='')
        pairs.add('3-4')
        for i in range(1,N):
            print('4-6 ', end='')
            pairs.add('4-6')
            termina.sort()
            
            print('6-7 ', end='')
            pairs.add('6-7')
            entrou = False
            while termina[0] < tempos[i][0]:
                entrou = True
                print('7-8 ', end='')
                pairs.add('7-8')
                del termina[0]
                caixas = caixas + 1
                if termina == []:
                    print('8-10 ', end='')
                    pairs.add('8-10')
                    break

                print('8-9 ', end='')
                pairs.add('8-9') 
                print('9-7 ', end='')
                pairs.add('9-7')

            if not entrou: 
                print('7-10 ', end='')
                pairs.add('7-10')

            ultimo = None
            if caixas > 0:
                print('10-11 ', end='')
                pairs.add('10-11')
                ultimo = '11'
                caixas = caixas - 1
                termina = termina + [tempos[i][0]+tempos[i][1]]
                               
            else:
                print('10-12 ', end='')
                pairs.add('10-12')
                ultimo = '12'
                atendimento = min(termina)
                termina.remove(min(termina))
                termina =  termina + [atendimento+tempos[i][1]]
                if atendimento - tempos[i][0] >= 20:
                    print('12-13 ', end='')
                    pairs.add('12-13')
                    ultimo = '13'
                    cont = cont +1
            print(ultimo, end='')
            print('-15 ', end='')
            pairs.add(ultimo+ '-15')
            print('15-4 ', end='')
            pairs.add('15-4')
        print('4-5 ', end='')
        pairs.add('4-5')
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
    print('pares de arcos: ')
    arcos = [p for p in pairs]
    arcos.sort()

    for i in range(len(arcos) - 1):
      for j in range(i + 1, len(arcos)):
        print(f'({arcos[i]}, {arcos[j]}), ', end='')
          
    print()
    print('resultado: ', a)


main()
