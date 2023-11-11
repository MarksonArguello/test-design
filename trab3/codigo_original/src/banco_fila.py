def banco(C,N,tempos):
    if N < C:
        return 0
    else:
        cont = 0
        termina = [tempos[0][0]+tempos[0][1]]
        caixas = C - 1
        
        for i in range(1,N):
            termina.sort()
            
            while termina[0] < tempos[i][0]:
                del termina[0]
                caixas = caixas + 1
                if termina == []:
                    break


            if caixas > 0:
                caixas = caixas - 1
                termina = termina + [tempos[i][0]+tempos[i][1]]
                               
            else:
                atendimento = min(termina)
                termina.remove(min(termina))
                termina =  termina + [atendimento+tempos[i][1]]
                if atendimento - tempos[i][0] >= 20:
                    cont = cont +1

        return cont           
