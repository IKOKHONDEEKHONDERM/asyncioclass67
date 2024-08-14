from flask import Flask , render_template
import httpx
import time
import random
from pypokemon.pokemon import Pokemon
import asyncio

app = Flask(__name__)

async def get_pokemon(client, url):
    print(f"{time.ctime()} - get {url}")
    resp = await client.get(url)
    pokemon = resp.json()
    return pokemon

async def get_pokemons():
    rand_list = []
    for i in range(5):
        rand_list.append(random.randint(1,151))
    #[random.randint(1, 151) for _ in range(5)]
    pokemon_data = []

    async with httpx.AsyncClient() as client:
        tasks = [get_pokemon(client, f'https://pokeapi.co/api/v2/pokemon/{number}') for number in rand_list]
        pokemons_json = await asyncio.gather(*tasks)

    for pokemon_json in pokemons_json:
        pokemon_object = Pokemon(pokemon_json)
        pokemon_data.append(pokemon_object)
        
    return pokemon_data

@app.route('/')
async def index():
    start_time = time.perf_counter()
    pokemons = await get_pokemons()
    end_time = time.perf_counter()
    print(f"{time.ctime()} - Get {len(pokemons)} pokemons. Time taken: {end_time-start_time} seconds")
    return  render_template('index.html', pokemons=pokemons, end_time=end_time, start_time=start_time)

if __name__ == '__main__':
    app.run(debug=True, port=50001)
