from datos.parametros_de_simulacion import Parametros_de_Simulacion
import random

class Cromosoma:
    
    def __init__(self):
        # self.__gen = 0
        self.__lista_genes = []
        for i in range(8): #y entonces para que es este for si despues lo agrega en agregar gen
            self.__lista_genes.append(random.randint(0,7))
        
        
    def agregar_gen_a_cromosoma(self, p_genes):
        for i in range(len(p_genes)):
            self.__lista_genes[i] = p_genes[i]
            
    def devolver_cromosoma(self):
        return self.__lista_genes
    
    def devolver_gen_en_posicion_dada (self, p_posicion):
        gen = self.__lista_genes[p_posicion]
        return gen
    
    def cruzar(self, otro_cromosoma):
        parametros_de_simulacion = Parametros_de_Simulacion()
        cromosoma_hijo = Cromosoma()
        genes = []
        posicion_inicio = random.randint(0, 7)
        #print(cromosoma_hijo.__lista_genes)
        for i in range(0, posicion_inicio):
            genes_madre = (self.__lista_genes[i])
            genes.append(genes_madre)
        for j in range(posicion_inicio, 8):
            genes_padre = otro_cromosoma.devolver_gen_en_posicion_dada(j)
            genes.append(genes_padre)
        
        if random.random()*100 < parametros_de_simulacion.dic_parametros['prob_mutacion']:
            posicion_random = random.randint(0, 7)
            valor_gen_original = genes[posicion_random]
            genes[posicion_random] = random.randint(0, 7)
            while(True):
                if(genes[posicion_random] == valor_gen_original):
                    genes[posicion_random] = random.randint(0,7)
                else:
                    break
                
        cromosoma_hijo.agregar_gen_a_cromosoma(genes)
        #print(cromosoma_hijo.__lista_genes)
        return cromosoma_hijo

           
if __name__ == '__main__':
    c1 = Cromosoma()
    lista_genes_c1 = []
    for i in range (8): #no toma el 8
        gen = random.randint(0, 7)
        lista_genes_c1.append(gen)
    c1.agregar_gen_a_cromosoma(lista_genes_c1)
    info_cromo = c1.devolver_cromosoma()
    print('cromosoma madre', info_cromo)
    
    c2 = Cromosoma()
    lista_genes_c2 = []
    for i in range (8):
        gen = random.randint(0, 7)
        lista_genes_c2.append(gen)
    c2.agregar_gen_a_cromosoma(lista_genes_c2)
    info_cromo2 = c2.devolver_cromosoma()
    print('cromo padre', info_cromo2)
    
    cromo_hijo = Cromosoma()
    cromo_hijo = c1.cruzar(c2)
    print(cromo_hijo.devolver_cromosoma())
    
'''
if __name__ == "__main__":
    c1 = Cromosoma()
    c2 = Cromosoma()
    c3 = c1.devolver_cruza_cromosoma()
'''   
    