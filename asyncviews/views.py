import asyncio                     # Biblioteca para lidar com programação assíncrona no Python
from time import sleep             # (não está sendo usado aqui, poderia ser removido)
import httpx                       # Biblioteca para fazer requisições HTTP de forma assíncrona
from django.http import HttpResponse  # Classe do Django usada para retornar respostas HTTP

# Função assíncrona que vai simular um processamento e depois fazer uma chamada HTTP
async def http_call_async():
    # Laço que conta de 1 até 5
    for num in range(1, 6):
        await asyncio.sleep(1)     # Aguarda 1 segundo de forma assíncrona (sem travar o loop)
        print(num)
    r = httpx.get('https://httpbin.org/')
    print(r)                

    # Cria um cliente HTTP assíncrono
    async with httpx.AsyncClient() as client:
        # Faz uma requisição GET para o site httpbin.org de forma assíncrona
        r = await client.get("https://httpbin.org")
        print(r)                   # Mostra a resposta no terminal (objeto de resposta do httpx)

# View assíncrona do Django
async def async_view(request):
    loop = asyncio.get_event_loop()             # Pega o loop de eventos atual do asyncio
    loop.create_task(http_call_async())         # Cria uma "tarefa" assíncrona sem bloquear a resposta
    return HttpResponse("Non-blocking HTTP request")  
    # Retorna a resposta imediatamente, enquanto a função http_call_async() roda em paralelo


def sync_view(request):
    http_call_async()
    return HttpResponse('Blocking HTTP request')