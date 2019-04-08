# socket_server.py
from aiohttp import web
from time import sleep
import socketio
# Cria um novo servidor Socket asyncrono
sio = socketio.AsyncServer()
# Cria uma nova aplicação Web Aiohttp
app = web.Application()

# Vincula nosso servidor Socket.IO a nossa apĺicação Web
sio.attach(app)
# Podemos definir os endpoints aiohttp normalmente
async def index(request):
    with open('index.html') as f:
        return web.Response(text=f.read(), content_type='text/html')

# Para criar um endpoint web socket, utilize este
# decorador, passando o nome do evento que desejamos observar
@sio.on('execute')
async def execute(sid, dataSet):
    # Nós recebemos uma novo evento chamado ‘message’
	# por meio de uma conexão socket
    # Escrevendos o Id da conexão e a mensagem enviada
    print("Iniciando a execução por: " , sid)
    print(dataSet)
    sleep(2)
    await sio.emit('progress', 20)
    sleep(2)
    await sio.emit('progress', 40)
    sleep(2)
    await sio.emit('progress', 60)
    sleep(2)
    await sio.emit('progress', 80)
    sleep(2)
    await sio.emit('progress', 100)


app.add_routes([web.static('/assets', './assets', show_index=True)])
# Agora nós vamos vincular nosso endpoint aiohttp
# ao roteamento da aplicação
app.router.add_get('/', index)

# Então é hora de servir a aplicação
if __name__ == '__main__':
    web.run_app(app)