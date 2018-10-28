import requests
poke=raw_input('enter pokemon name: ')
r = requests.get('http://pokeapi.co/api/v2/pokemon/'+poke+'/')
responseJson = r.json()
pokemonName = responseJson['name']
pokemonType = responseJson['types'][0]['type']['name']
#pokemonWeakness=responseJson['weaknesses'][0]['weakness']['name']
print("Pokemon Type: "+pokemonType)
