class Usuario:
    def __init__(self, nome, email, cpf):
        if nome.isalpha():
            self.nome = nome
        if "@" in email:
            self.email = email
        self.__cpf = cpf


    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, valor):
        if len(valor) == 11 and str.isdigit(valor):
            self.__cpf = valor
        else:
            self.__cpf = None

    def __str__(self):
        return f'Nome: {self.nome}, Email: {self.email}'
    

class Aluno(Usuario):
    def __init__(self, nome, email, cpf):
        Usuario.__init__(self, nome, email, cpf)
        self.estado_matricula = 'ativa'
        self.cursos_inscritos = []


    def inscrever_curso(self,curso):
        if self.estado_matricula == 'ativa':
            self.cursos_inscritos.append(curso)
            print(f'O aluno foi inscrito no curso {curso}')

    def ver_cursos(self):
        if self.cursos_inscritos == []:
            print(f'O aluno {self.nome} não está inscrito em nenhum curso.')
        else:
            print(f'O aluno está inscrito em:')
            for i in self.cursos_inscritos:
                print(i)
        
    def __str__(self):
        if self.cursos_inscritos == []:
            return f'Nome: {self.nome} , Email: {self.email} , Cursos: Nenhum , Estado da Matrícula: {self.estado_matricula}'
        else:
            return f'Nome: {self.nome} , Email: {self.email} , Cursos: {self.ver_cursos} , Estado da Matrícula: {self.estado_matricula}'
        

class Coordenador(Usuario):
    def __init__(self, nome, email, cpf):
        Usuario.__init__(self, nome, email, cpf)
    

    def remover_curso(self, usuario, curso):
        #if usuario.nome == Aluno.nome:
        usuario.cursos_inscritos.remove(curso)
        print(f'O curso {curso} foi removido de {usuario.nome}')
        
    def suspender_aluno(self,aluno):
        if aluno.estado_matricula == 'ativa':
            print(f'A matricula de {aluno.nome} foi suspensa.')
            aluno.estado_matricula = 'suspensa'
        else:
            print(f'A matricula de {aluno.nome} foi ativa.')
            aluno.estado_matricula = 'ativa'
            
    def __str__(self):
        return f'Nome do Coordenador: {self.nome}, Email: {self.email}'



'''aluno1 = Aluno('Ana', 'ana@exemple.com', '12345678901')
coordenador1 = Coordenador('Carlos', 'carlos@exemple.com', '98765432100')
aluno1.inscrever_curso('Matemática')
aluno1.ver_cursos()
coordenador1.remover_curso(aluno1, 'Matemática')
coordenador1.suspender_aluno(aluno1)
print(aluno1)
print(coordenador1)'''
#aluno1.remover_curso(aluno1, 'Matemática')


class Student:
    def __init__(self):
        self.name = 'Seachlann Sara'
        self.__id = 12
obj = Student()
print(obj.name)      # Acessa o atributo público
 #print(obj.__private_attr_name)  # Levanta um AttributeError
 # Você ainda acessa o atributo através de name mangling
print(obj._Student__id)

