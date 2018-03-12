import json

data = {}
data['people'] = []
data['people'].append({
    'nombre': 'Águeda',
    'primer apellido': 'Sierra',
    'segundo apellido': 'Carreto'
})
data['people'].append({
    'nombre': 'Weam',
    'primer apellido': 'Moumouh',
    'segundo apellido': ''
})

with open('data1.json', 'w') as outfile:
    json.dump(data, outfile)
