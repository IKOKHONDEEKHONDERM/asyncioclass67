from pypokemon.pokemon import Pokemon
import httpx
import asyncio
import random
import time

async def get_pokemon(client, url):
    print(f"time.client() = get {url}")
    resp = await client.get(url)
    pokemon = resp.json()

    return Pokemon(pokemon)

async def get_pokemons():
    async with httpx.AsyncClient() as client:
        tasks = []
        rand_list = []
        for i in range(151):
            rand_list.append(random.randint(1, 151))

        for number in rand_list:
            url = f"https://pokeapi.co/api/v2/pokemon/{number}"
            tasks.append(asyncio.create_task(get_pokemon(client, url)))

        pokemons = await asyncio.gather(*tasks)

    return pokemons

async def index():
    start_time = time.perf_counter()
    pokemons = await get_pokemons()
    end_time = time.perf_counter()
    print(f"time.client() = Asynchronous get {len(pokemons)} pokemons. Time taken = {end_time - start_time} seconds")
    return pokemons

if __name__ == "__main__":
    asyncio.run(index())
