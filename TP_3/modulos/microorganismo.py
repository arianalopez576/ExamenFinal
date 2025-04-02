import random
from datos.parametros_de_simulacion import Parametros_de_Simulacion
from modulos.cromosoma import Cromosoma

ps = Parametros_de_Simulacion()

class Microorganismo:
    
    def __init__(self):
        self.__cromosoma = Cromosoma()
        self.__direccion_MO = random.randint(0, 7)
        self.__fila = random.randint(0, ps.dic_parametros['max_filas']-1) #valor para que no se vaya del rango del territorio
        self.__columna = random.randint(0, ps.dic_parametros['max_columnas']-1)
        self.__energia = ps.dic_parametros['energia_inicial']
        self.__mov_relativo = ps.mov_relativo #el mov relativo no esta dentro del dic, ¿se llama de la misma forma?
        self.__energia_perdida = ps.dic_parametros['energia_perdida']
        self.__prob_mutacion = ps.dic_parametros['prob_mutacion']
        self.__prob_cambio_MO = ps.dic_parametros['prob_cambio_MO']
        self.__max_alimento_ingerir = ps.dic_parametros['cant_max_alimento_ingerir']
        self.__energia_max = ps.dic_parametros['energia_max']
        self.__inteligencia = self.__cromosoma.devolver_inteligencia()
     
    def set_cromosoma(self, p_cromo):
        #p_cromo es una lista de genes
        self.__cromosoma.agregar_gen_a_cromosoma(p_cromo)
     
    def get_cromosoma(self):
        return self.__cromosoma
    
    def get_lista_genes(self):
        return self.__cromosoma.devolver_cromosoma()
    
    # def get_fila(self):
    #     return self.__fila

    # def get_columna(self):
    #     return self.__columna
    
    def get_posicion(self):
        return(self.__fila, self.__columna)
    
    def set_posicion_MO(self, p_fila, p_columna):
        self.__fila = p_fila
        self.__columna = p_columna
        
    def set_energia (self, p_energia):
        self.__energia = p_energia
        
    def get_energia (self):
        return self.__energia
    
    
    def __disminuir_energia(self):
        self.__energia = self.__energia - self.__energia_perdida #en caso de que se quiera modif y la energía perdida no sea 1 a 1
    
    def reproduccion(self, MO_padre):
        cromo_padre = MO_padre.get_cromosoma()
        MO_hijo = Microorganismo()
        cromo_hijo = self.__cromosoma.cruzar(cromo_padre)
        MO_hijo.set_cromosoma(cromo_hijo.devolver_cromosoma())
       
        return MO_hijo
   
     
    def detectar_alimento(self, p_gestor_alimento):
        for pos in range(8):
            fila = self.__fila + self.__mov_relativo[pos][0]
            columna = self.__columna + self.__mov_relativo[pos][1]
            if p_gestor_alimento.retornar_alimento_en_posicion(fila, columna) > 0:
                return pos 
        return -1 
    
    def comer(self, p_gestor_alimento): 
        #si la energia que puede obtener, supera la cantidad de alimento que puede ingerir, entonces la energia sera igual al max alimento
        if (self.__energia_max - self.__energia) >= self.__max_alimento_ingerir:
            alimento_quitar = self.__max_alimento_ingerir
        #si la energia es menor, es decir, puede seguir alimentadose
        else:
           alimento_quitar = self.__energia_max - self.__energia
       
        alimento_ingerido = p_gestor_alimento.quitar_alimento_en_posicion(self.__fila, self.__columna, alimento_quitar)
        self.__energia += alimento_ingerido
      
    def moverse(self, p_epoca, p_gestor_alimento):
        #verifico que tenga vida
        if self.get_energia() != 0:
            #detecta alimento
            celda_alimento = self.detectar_alimento(p_gestor_alimento)
            
            #si hay alimento en la celda
            if celda_alimento != -1:
                #el gen le indica la nueva posicion
                posicion_nueva = self.__cromosoma.devolver_gen_en_posicion_dada(celda_alimento)
                fila_nueva = self.__fila + self.__mov_relativo[posicion_nueva][0]
                columna_nueva = self.__columna + self.__mov_relativo[posicion_nueva][1]
                #si esta en rango, se mueve y come
                ubicacion_en_rango = self.__verificar_ubicacion(fila_nueva, columna_nueva)
                if ubicacion_en_rango == True: 
                    self.__fila = fila_nueva
                    self.__columna = columna_nueva 
                    self.__direccion_MO = posicion_nueva
                    
                #si la posicion esta fuera de rango, busca otra
                else:
                    #probabilidad de cambio de la direccion del MO
                    if p_epoca % ps.dic_parametros['prob_cambio_MO'] == 0: #random.random da un num decimal aleatorio entre 0 y 100
                       direccion_movimiento = random.randint(0,7)
                       fila_nueva = self.__fila + self.__mov_relativo[direccion_movimiento][0]
                       columna_nueva = self.__columna + self.__mov_relativo[direccion_movimiento][1]
                       ubicacion_en_rango = self.__verificar_ubicacion(fila_nueva, columna_nueva)
                       if ubicacion_en_rango == True:
                               self.__fila = fila_nueva
                               self.__columna = columna_nueva
                               self.__direccion_MO = direccion_movimiento   
                        #si la ubicacion esta fuera de rango, asegurar movimiento      
                       else:
                           self._asegurar_movimiento()
                    #si la direccion de movimiento se mantiene
                    else:
                        fila_nueva = self.__fila + self.__mov_relativo[self.__direccion_MO][0]
                        columna_nueva = self.__columna + self.__mov_relativo[self.__direccion_MO][1]
                        ubicacion_en_rango = self.__verificar_ubicacion(fila_nueva, columna_nueva)
                        if ubicacion_en_rango == True:
                                self.__fila = fila_nueva
                                self.__columna = columna_nueva
                        #si la ubicacion esta fuera de rango, asegurar movimiento
                        else:
                            self._asegurar_movimiento()
                              
            #si no encuentra alimento en la celda
            else:
                fila_nueva = self.__fila + self.__mov_relativo[self.__direccion_MO][0]
                columna_nueva = self.__columna + self.__mov_relativo[self.__direccion_MO][1]
                ubicacion_en_rango = self.__verificar_ubicacion(fila_nueva, columna_nueva)
                if ubicacion_en_rango == True:
                        self.__fila = fila_nueva
                        self.__columna = columna_nueva 
                else:
                    self._asegurar_movimiento()
            
            #al moverse, pierde energia
            self.__disminuir_energia()
        
        
    def _asegurar_movimiento(self):        
        se_movio = False
        
        while se_movio == False:
            direccion_movimiento = random.randint(0,7)
            fila_nueva = self.__fila + self.__mov_relativo[direccion_movimiento][0]
            columna_nueva = self.__columna + self.__mov_relativo[direccion_movimiento][1]
            ubicacion_en_rango = self.__verificar_ubicacion(fila_nueva, columna_nueva)
            if ubicacion_en_rango == True:
                    self.__fila = fila_nueva
                    self.__columna = columna_nueva
                    self.__direccion_MO = direccion_movimiento   
                    se_movio = True
        
            
            
        
    def __verificar_ubicacion(self, p_fila_nueva, p_columna_nueva):
        if (p_fila_nueva >= 0 and p_fila_nueva < ps.dic_parametros['max_filas']) and (p_columna_nueva >= 0 and p_columna_nueva < ps.dic_parametros['max_columnas']):
            return True 
        else: 
            False
   
            
    def verificar_vida(self):
        esta_vivo = False
        energia_total = self.get_energia()
        if energia_total > 0:
            esta_vivo = True
        return esta_vivo
            
    def devolver_inteligencia(self):
        return self.__inteligencia
    
'''   
#verificar la  reproducción
if __name__ == "__main__":
    MO_madre = Microorganismo()
    cromo_madre = MO_madre.get_lista_genes()
    
    MO_padre = Microorganismo()
    cromo_padre = MO_padre.get_lista_genes()
   
    MO_hijo = MO_madre.reproduccion(MO_padre)
    print('cromosoma hijo', MO_hijo.get_lista_genes())
    print('madre', MO_madre.get_lista_genes())
    print('padre', MO_padre.get_lista_genes())
   '''
   
#verificar que se mueve
if __name__ == "__main__":
    ps = Parametros_de_Simulacion()
    ga = Gestor_de_Alimento(ps)
    MO = Microorganismo()
    MO.set_energia(190)
    MO.set_posicion_MO(99, 99)
    ga.agregar_alimento_en_posicion(98, 99)
    ga.agregar_alimento_en_posicion(98, 98)
    ga.agregar_alimento_en_posicion(99, 98)
    ga.quitar_alimento_en_posicion(99, 98, 45)
    ga.quitar_alimento_en_posicion(98, 99, 45)
    ga.quitar_alimento_en_posicion(98, 98, 45)
    print('pos1', MO.get_posicion())
    print('energia inicial', MO.get_energia())
    MO.moverse(ga)
    MO.comer(ga)
    print('pos2', MO.get_posicion())
    print('energia final', MO.get_energia())
    print('cant comida', ga.retornar_alimento_en_posicion(98, 99))
    print('cant comida', ga.retornar_alimento_en_posicion(98, 98))
    print('cant comida', ga.retornar_alimento_en_posicion(99, 98))
    