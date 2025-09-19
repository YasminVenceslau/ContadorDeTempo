import asyncio
from django.http import JsonResponse

# View assíncrona que conta de 1 a 5 com pausa de 1 segundo
async def contador_async(request):
    contagem = []  # lista para armazenar os números

    for i in range(1, 6):       # conta de 1 até 5
        await asyncio.sleep(1)  # espera 1 segundo sem travar o servidor
        contagem.append(i)      # adiciona o número à lista

    return JsonResponse({"contador": contagem})
