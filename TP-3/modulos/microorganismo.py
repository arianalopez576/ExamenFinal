import random
from datos.parametros_de_simulacion import Parametros_de_Simulacion
from modulos.cromosoma import Cromosoma
from modulos.gestor_de_alimento import Gestor_de_Alimento

parametros_de_simulacion = Parametros_de_Simulacion()
class Microorganismo:
    # _energia_maxima = Parametros_de_Simulacion.energia_max 
    
    def __init__(self):
        self.__cromosoma = Cromosoma()
        self.__lista_cromosoma = []
        #fila y columna para la ubicación inicial aleatoria
        self.__fila = random.randint(0, parametros_de_simulacion.dic_parametros['max_filas']-1) 
        self.__columna = random.randint(0, parametros_de_simulacion.dic_parametros['max_columnas']-1)
        self.__energia = parametros_de_simulacion.dic_parametros['energia_inicial']
        self.__inteligencia = None #se define con el cromosoma
        self.__direccion_aleatoria = random.randint(0,7)
    
    def get_cromosoma(self):
        return self.__cromosoma
    
    def set_lista_cromosoma(self, cromosoma):
        self.__lista_cromosoma = cromosoma.devolver_cromosoma()
    
    def get_lista_cromosoma(self):
        return self.__lista_cromosoma
    
    def get_fila(self):
        return self.__fila

    def get_columna(self):
        return self.__columna
    
    def set_posicion_MO(self, p_fila, p_columna):
        self.__fila = p_fila
        self.__columna = p_columna
        
    def set_energia (self, energia):
        self.__energia = energia
    
    def disminuir_energia(self):
        self.__energia = self.__energia - parametros_de_simulacion.dic_parametros['energia_perdida'] #en caso de que se quiera modif y la energía perdida no sea 1 a 1
    
    def get_energia (self):
        return self.__energia
        
    
    def reproduccion(self, MO_padre):
        cromo_madre = self.__cromosoma
        cromo_padre = MO_padre.get_cromosoma()
        microorganismo_hijo = Microorganismo()
        microorganismo_hijo.set_lista_cromosoma(cromo_madre.cruzar(cromo_padre))
        return microorganismo_hijo
   
     
    def detectar_alimento(self, p_gestor_alimento):
        for pos in range(8):
            fila = self.__fila + parametros_de_simulacion.mov_relativo[pos][0]
            columna = self.__columna + parametros_de_simulacion.mov_relativo[pos][1]
            if p_gestor_alimento.retornar_alimento_en_posicion(fila, columna) > 0:
                return pos 
        return -1 
                        
    
    def comer(self, gestor_alimento): 
        energia_ganada = 0
        if gestor_alimento.retornar_alimento_en_posicion(self.__fila, self.__columna) > 0:
            if self.__energia < parametros_de_simulacion.dic_parametros['energia_max']:
                if self.__energia + gestor_alimento.quitar_alimento_en_posicion(self.__fila, self.__columna) > parametros_de_simulacion.dic_parametros['energia_max']:
                    energia_ganada = parametros_de_simulacion.dic_parametros['energia_max'] - self.__energia
                else:
                    energia_ganada = gestor_alimento.quitar_alimento_en_posicion(self.__fila, self.__columna)
                    self.__energia = self.__energia + energia_ganada               
                        
                
    def moverse(self, p_gestor_de_alimento):
        cromo = self.__cromosoma
        celda_alimento = self.detectar_alimento(p_gestor_de_alimento)
        
        if celda_alimento != -1:
            posicion_nueva = cromo.devolver_gen_en_posicion_dada(celda_alimento)
            fila_nueva = self.__fila + parametros_de_simulacion.mov_relativo[celda_alimento][0]
            columna_nueva = self.__columna + parametros_de_simulacion.mov_relativo[celda_alimento][1]
            ubicacion_en_rango = self.__verificar_ubicacion(fila_nueva, columna_nueva)
            if ubicacion_en_rango == True: 
                self.__fila = fila_nueva
                self.__columna = columna_nueva 
                hay_alimento = p_gestor_de_alimento.retornar_alimento_en_posicion(self.__fila, self.__columna)
                if celda_alimento == posicion_nueva or hay_alimento > 0 : 
                    self.comer(p_gestor_de_alimento)
                    
        if random.random()*100 < parametros_de_simulacion.dic_parametros['prob_cambio_MO']: #random.random da un num decimal aleatorio entre 0 y 100
            self.__direccion_aleatoria = random.randint(0,7)
            fila_nueva = self.__fila + parametros_de_simulacion.mov_relativo[self.__direccion_aleatoria][0]
            columna_nueva = self.__columna + parametros_de_simulacion.mov_relativo[self.__direccion_aleatoria][1]
            if self.__verificar_ubicacion(fila_nueva, columna_nueva) == True:
                self.__fila = fila_nueva
                self.__columna = columna_nueva
                hay_alimento = p_gestor_de_alimento.retornar_alimento_en_posicion(self.__fila, self.__columna)
                if hay_alimento > 0 :
                    self.comer(p_gestor_de_alimento)
        else:
            fila_nueva = self.__fila + parametros_de_simulacion.mov_relativo[self.__direccion_aleatoria][0]
            columna_nueva = self.__columna + parametros_de_simulacion.mov_relativo[self.__direccion_aleatoria][1]
            if self.__verificar_ubicacion(fila_nueva, columna_nueva) == True:
                self.__fila = fila_nueva
                self.__columna = columna_nueva
                hay_alimento = p_gestor_de_alimento.retornar_alimento_en_posicion(self.__fila, self.__columna)
                if hay_alimento > 0 :
                    self.comer(p_gestor_de_alimento)        
                    
        self.disminuir_energia()
        
        """
            ubicacion_en_rango = self.__verificar_ubicacion(fila_nueva, columna_nueva)
            if ubicacion_en_rango == True :
                nuevo_mov = False 
        """
        
    def __verificar_ubicacion(self, p_fila_nueva, p_columna_nueva):
        if (p_fila_nueva >= 0 and p_fila_nueva < parametros_de_simulacion.dic_parametros['max_filas']) and (p_columna_nueva >= 0 and p_columna_nueva < parametros_de_simulacion.dic_parametros['max_columnas']):
            return True 
        else: 
            False
    
            
    def verificar_vida(self):
        esta_vivo = False
        energia_total = self.retornar_nivel_energia()
        if energia_total > 0:
            esta_vivo = True
        return esta_vivo
            
    def retornar_nivel_energia(self):
        return self.__energia
    
    def devolver_inteligencia(self):
        cromo = self.__cromosoma
        genes = cromo.devolver_cromosoma()
        contador_inteligencia = 0
        for i in range(8):
            if(i == genes[i]):
                contador_inteligencia += 1
        return contador_inteligencia
   
#verificar la  reproducción
if __name__ == "__main__":
    MO_madre = Microorganismo()
    cromo_madre = MO_madre.get_cromosoma()
    lista_genes_madre = []
    for i in range (8):
        gen = random.randint(0, 7)
        lista_genes_madre.append(gen)
    cromo_madre.agregar_gen_a_cromosoma(lista_genes_madre)
    MO_madre.set_lista_cromosoma(cromo_madre)
    
    MO_padre = Microorganismo()
    cromo_padre = MO_padre.get_cromosoma()
    lista_genes_padre = []
    for i in range (8):
        gen_padre = random.randint(0, 7)
        lista_genes_padre.append(gen_padre)
    cromo_padre.agregar_gen_a_cromosoma(lista_genes_padre)
    MO_padre.set_lista_cromosoma(cromo_padre)
    
    MO_hijo = MO_madre.reproduccion(MO_padre)
    print('cromosoma hijo', MO_hijo.get_lista_cromosoma())
    print('madre', MO_madre.get_lista_cromosoma())
    print('padre', MO_padre.get_lista_cromosoma())
    
#verificar la detección de alimento
if __name__ == "__main__":
    MO = Microorganismo()
    g_alim = Gestor_de_Alimento(parametros_de_simulacion)
    for x in range(100):
        for y in range(100):
            g_alim.agregar_alimento_en_posicion(x, y)
    p = MO.detectar_alimento(g_alim)
    print('posicion del alimento', p)
    