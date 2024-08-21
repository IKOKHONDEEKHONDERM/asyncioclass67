from pypokemon.pokemon import Pokemon
import httpx
import asyncio
import time

async def get_ability_pokemon(client, ability_url):
    print(f"Fetching ability data from {ability_url}")
    try:
        resp = await asyncio.wait_for(client.get(ability_url), timeout=2.0)
        ability_data = resp.json()
        pokemon_urls = [poke['pokemon']['url'] for poke in ability_data['pokemon']]
        return pokemon_urls
    except asyncio.TimeoutError:
        print(f"Request to {ability_url} timed out")
        return []

async def get_pokemon(client, url):
    print(f"Fetching Pokemon data from {url}")
    try:
        resp = await asyncio.wait_for(client.get(url), timeout=2.0)
        pokemon = resp.json()
        return pokemon
    except asyncio.TimeoutError:
        print(f"Request to {url} timed out")
        return None

async def get_pokemons_from_ability(client, ability_url):
    pokemon_urls = await get_ability_pokemon(client, ability_url)
    tasks = [asyncio.create_task(get_pokemon(client, url)) for url in pokemon_urls if url]
    pokemons = await asyncio.gather(*tasks)
    return [pokemon for pokemon in pokemons if pokemon]

async def index():
    ability_urls = {
        "battle-armor": "https://pokeapi.co/api/v2/ability/battle-armor",
        "speed-boost": "https://pokeapi.co/api/v2/ability/speed-boost"
    }

    start_time = time.perf_counter()

    async with httpx.AsyncClient() as client:
        tasks = [get_pokemons_from_ability(client, url) for url in ability_urls.values()]
        results = await asyncio.gather(*tasks)

    battle_armor_pokemons = results[0]
    speed_boost_pokemons = results[1]

    end_time = time.perf_counter()

    print(f"Number of Pokémon with ability 'battle-armor': {len(battle_armor_pokemons)}")
    print("Pokémon with ability 'battle-armor':")
    for pokemon in battle_armor_pokemons:
        print(pokemon['name'])
    
    print(f"Number of Pokémon with ability 'speed-boost': {len(speed_boost_pokemons)}")
    print("Pokémon with ability 'speed-boost':")
    for pokemon in speed_boost_pokemons:
        print(pokemon['name'])
    
    print(f"Time taken = {end_time - start_time} seconds")

if __name__ == "__main__":
    asyncio.run(index())
