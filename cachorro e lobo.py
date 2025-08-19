from random import randint 
 
class Cachorro: 
    def _init_(self, humor): 
        humores_validos = ["brincalhao", "docil", "ok", "estressado"] 
        if not (isinstance (humor, str) and humor in humores_validos): 
            print("Humor inválido. Instânciação cancelada") 
            return 
        self.fome = True 
        self.humor = humor 
         
    def comer(self): 
        if not self.fome: 
            return "O cachorro não está com fome!" 
        else: 
            self.fome = False 
            return "Você alimentou o cachorro! :)" 
         
         
    def brincar(self): 
        if self.fome: 
            return "Alimente o cachorro antes de brincar." 
        else: 
            x = randint(1,100) 
            if self.humor == "brincalhao": 
                return "Você brincou muito com o cachorro!!!" 
            elif self.humor == "docil": 
                if x <= 80: 
                    return "Você brincou com o cachorro!!!" 
                else: 
                    return "O cachorro não quer brincar. :(" 
            elif self.humor == "ok": 
                if x <= 50: 
                    return "Você brincou com o cachorro!!!" 
                else: 
                    return "O cachorro não quer brincar. :(" 
            elif self.humor == "estressado": 
                if x <= 20: 
                    return "Você brincou com o cachorro!!!" 
                else: 
                    return "O cachorro não quer brincar. :(" 
                 
    def exibir_informacao(self): 
        return f"Sobre o cachorro: \nFome: {self.comer()}\nHumor: {self.humor}\nBrincar: {self.brincar()}" 
     
     
'''class Lobo: 
     
    def comer(self): 
        if not self.fome: 
            return "O lobo não está com fome!" 
        else: 
            self.fome = False 
            return "O lobo se alimentou!"''' 
         
#cachorro = Cachorro()
cachorro01= Cachorro("ok") 
#print(cachorro01.exibir_informacao())
