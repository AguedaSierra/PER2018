import json

data = {}
data['people'] = []
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

with open('data2.json', 'w') as outfile:
    json.dump(data, outfile)
