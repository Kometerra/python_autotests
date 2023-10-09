import requests
import pytest 

token = "1a8aabf5c07538dba884d25ca0aa6f33"
''''response = requests.post('https://api.pokemonbattle.me:9104/trainers/reg', json = {
    "trainer_token": token,
    "email": "kometerra@gmail.com",
    "password": "Iloveqa1"
}, headers = {"Content-Type":"application/json"})
print (response.text)

response_activation = requests.post ('https://api.pokemonbattle.me:9104/trainers/confirm_email',
json = {
    "trainer_token" : token
}, headers = {"Content-Type":"application/json"})

print(response_activation.status_code)

if response_activation.status_code == 200: 
    print('ok!')
else: 
    print('not ok!')
    
response = requests.post('https://api.pokemonbattle.me:9104/pokemons', json = {
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}, headers =  {"trainer_token" : token , "Content-Type":"application/json" })

print (response.text)

response = requests.put('https://api.pokemonbattle.me:9104/pokemons', json = {
    "pokemon_id": "12196",
    "name": "kometa"
}, headers =  {"trainer_token" : token , "Content-Type":"application/json" })

print (response.text)'''

response = requests.post('https://api.pokemonbattle.me:9104/trainers/add_pokeball', json = {
    "pokemon_id": "12196"
}, headers =  {"trainer_token" : token , "Content-Type":"application/json" })

print (response.text)

