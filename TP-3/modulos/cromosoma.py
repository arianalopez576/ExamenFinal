from datos.parametros_de_simulacion import Parametros_de_Simulacion
import random

class Cromosoma:
    #composicion con microorganismo
    def __init__(self):
        self.__lista_genes = []
        #crea la lista aleatoria de genes
        for i in range(8):
            self.__lista_genes.append(random.randint(0,7))
        
    #agrega los genes a un nuevo cromosoma luego de la cruza    
    def agregar_gen_a_cromosoma(self, p_genes):
        for i in range(len(p_genes)):
            self.__lista_genes[i] = p_genes[i]
            
    #devuelve la lista de genes ya que es un atributo privado
    def devolver_cromosoma(self):
        return self.__lista_genes
    
    #devuelve el gen en determinado lugar de la lista
    def devolver_gen_en_posicion_dada (self, p_posicion):
        gen = self.__lista_genes[p_posicion]
        return gen
    
    def cruzar(self, otro_cromosoma):
        parametros_de_simulacion = Parametros_de_Simulacion()
        cromosoma_hijo = Cromosoma()
        genes = []
        posicion_inicio = random.randint(1,6) #para que ningun hijo sea igual al padre/madre
        
        for i in range(0, posicion_inicio):
            genes_madre = (self.__lista_genes[i])
            genes.append(genes_madre)
        for j in range(posicion_inicio, 8):
            genes_padre = otro_cromosoma.devolver_gen_en_posicion_dada(j)
            genes.append(genes_padre)
        
        #random.random float entre 0 y 100
        #random.randint int entre 0 y 7
        if random.random()*100 < parametros_de_simulacion.dic_parametros['prob_mutacion']:
            posicion_random = random.randint(0, 7)
            valor_gen_original = genes[posicion_random]
            genes[posicion_random] = random.randint(0, 7)
            #para que siempre cambie, incluso cuando el random de el mismo valor que ya tenia
            while valor_gen_original == genes [posicion_random]:
                    genes[posicion_random] = random.randint(0,7)
                    
        cromosoma_hijo.agregar_gen_a_cromosoma(genes)
        
        return cromosoma_hijo
    
    #halla las coincidencias entre el gen y la posicion a la que se debe mover 
    def devolver_inteligencia(self):
         genes = self.devolver_cromosoma()
         contador_inteligencia = 0
         for i in range(8):
             if(i == genes[i]):
                 contador_inteligencia += 1
         return contador_inteligencia
           
# if __name__ == '__main__':
#     c1 = Cromosoma()
#     lista_genes_c1 = []
#     for i in range (8): #no toma el 8
#         gen = random.randint(0, 7)
#         lista_genes_c1.append(gen)
#     c1.agregar_gen_a_cromosoma(lista_genes_c1)
#     info_cromo = c1.devolver_cromosoma()
#     print('cromosoma madre', info_cromo)
    
#     c2 = Cromosoma()
#     lista_genes_c2 = []
#     for i in range (8):
#         gen = random.randint(0, 7)
#         lista_genes_c2.append(gen)
#     c2.agregar_gen_a_cromosoma(lista_genes_c2)
#     info_cromo2 = c2.devolver_cromosoma()
#     print('cromo padre', info_cromo2)
    
#     cromo_hijo = Cromosoma()
#     cromo_hijo = c1.cruzar(c2)
#     print(cromo_hijo.devolver_cromosoma())
    