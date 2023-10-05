from fastapi import FastAPI
from pydantic import BaseModel

# adiconando fast api
app = FastAPI()

# listas que usei duramte processo, "lista" para "banco de dados", "lixo" para remover os cursos para outra lista e nova lista para guardar apenas os cursos depois da modificação
lista = []
lixo = []
nova_lista = []

# criando classe + herança do basemodel
class Curso(BaseModel):
    id: int
    titulo: str
    aulas: str
    horas: int
    dia: str


# metodo get curso: path com um parametro de resposta para lista e depois retorna a lista
@app.get("/get_curso",response_model=lista)
async def get_curso():
    return lista, {'mensagem':'listagem completa'}


# path com parametro "achar id", função com o mesmo parametro com o tipo de dado para ajudar o fast api identificar mais facil.
# a função enumerate do python cosegue pegar o index[posição] e o valor do index ao mesmo tempo por isso a variavel "index" e "user", seguido por um loop que apenas
# adiciona a nova_lista apenas aqueles que tem o id especifico sendo buscado e depois os retorna.
@app.get("/get-curso_id/{achar_id}",response_model_include=lista)
async def get_curso_id(achar_id: int):
    for index, user in enumerate(lista):
        if user.id == achar_id:
            nova_lista = [usuario for usuario in lista if usuario.id == achar_id]
            return nova_lista


# path com resposta para lista, função carrega a instacia "cursinho" da clase "Curso", e depois é só dar um append na instancia e depois retornala
@app.post('/cadastrar_curso',response_model=lista)
async def cadastrar_curso(cursinho: Curso):
    lista.append(cursinho)
    return lista , {'mensage':'curso cadastrado'}


# ath com parametro "achar id", função com parametros "achar_id: int" e uma instancia "novo_curso: Curso"
# a função enumerate do python cosegue pegar o index[posição] e o valor do index ao mesmo tempo por isso a variavel "index" e "user", seguido por um loop que apenas.
# adiciona a posição "lista[index]" a nova instancia "novo_curso" e depois a retorna.
@app.put('/put_curso/{achar_id}')
async def put_curso(achar_id: int, novo_curso: Curso):
    for index, user in enumerate(lista):
        if user.id == achar_id:
            lista[index] = novo_curso
            return novo_curso, {'mensagem':'curso modificado'}


# path com parametro "achar_id" , função com parametro "achar_id: int"
# o mesmo esque,a do enumerate, "lista" recebe a lista "lixo" com a condição de que as unicas coisas que podem passar 
# são aquelas que não são o id especificado,
# o id specifico vai ser armazenado na lista lixo, assim "deletando", poderia usar as fuções .pop() ou .remove() 

@app.delete('/delete_curso/{achar_id}')
async def deletar_curso(achar_id: int):
    for index, user in enumerate(lista):
        if user.id == achar_id:
            lista[:] = lixo = [usuario for usuario in lista if usuario.id != achar_id]
            return lista, {'mensage':'deletado com sucesso, esses são os cursos restantes acima!'}
            