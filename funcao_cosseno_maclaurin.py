def funcao_cosseno_maclaurin(x, precisao_desejada):
    import numpy as np
    import math

    precisao_desejada_alcancada = False
    #Booleana que determina se a estimativa atual está dentro da precisão
    #desejada ou não


    k = 0
    # número de termos da série de Maclaurin considerados até o momento

    f = 0
    #Estimativa da função que queremos calcular, inicializada como 0

    n = 0
    #número de termos não nulos para cálculo da função cosx quando tiver k igual a par

    while not precisao_desejada_alcancada:          
 
        if(k%2==0): # k ímpar não satisfaz a condição, logo somente k par são consideradas
            f += (math.pow(-1,n)/math.factorial(2*n))*math.pow(x,2*n) # Valor da função cos(x) em MacLaurin
            n+=1
            
        if (1/math.factorial(k+1))* math.pow(np.abs(x),k+1)<= precisao_desejada:  
            precisao_desejada_alcancada = True       
            break ## Irá quebrar o laço while quando o Resto for menor à precisão desejada    
               
        print("Resto:", (1/math.factorial(k+1)) * math.pow(np.abs(x),k+1), "para k = ", k)         
        k += 1
        # Enquanto a precisão desejada não tiver sido alcançada, 
        # incrementamos o valor de k e adicionamos novos termos ao polinômio.

        
    return [f,k]