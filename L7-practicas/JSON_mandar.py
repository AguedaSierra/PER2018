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
data['people'].append({
    'nombre': 'María',
    'primer apellido': 'Sevilla',
    'segundo apellido': 'García'
})
data['people'].append({
    'nombre': 'Andreea',
    'primer apellido': 'Florea',
    'segundo apellido': ''
})

with open('data.json', 'w') as outfile:
    json.dump(data, outfile)
