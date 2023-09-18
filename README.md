# 3D-Procedural

Este repositório contém um algoritmo que é capaz de gerar abstrações tridimensionais de dados de forma procedural. Essas abstrações são projetadas nãoe xclusivamente mas abrangendo a criação de mapas em jogos, proporcionando ambientes tridimensionais únicos e interessantes.

### Funcionalidades

- **Geração Procedural**: O algoritmo utiliza técnicas de geração procedural para criar abstrações tridimensionais de forma dinâmica e variada.

- **Personalização**: É possível personalizar diversos parâmetros do algoritmo para obter resultados específicos e atender às necessidades de diferentes tipos de jogos.

### Requisitos

- Python 3.x
- Numpy

### Repositório:

```bash
git clone git@github.com:MAIA332/3D-Procedural.git
```
### Utilização:
- **form** : 
    - random: formato aleatorio **(padrão)**
    - structure: formato que permite a passagem com dados especificos
- **dimension**: parâmetro de dimensionamento, por padrão gera com x=2 y=2 e z=3

#### Random:

```
c = cube(dimension=(4,4,3)) # Gera uma saida aleatorira passando uma dimensão especifica
```

**Output:**
```
{
    'layer1': array([[0.68360579, 0.05008707, 0.99132167, 0.54871132],
       [0.48491225, 0.50401007, 0.85212033, 0.51950698],
       [0.29735764, 0.00296726, 0.20771706, 0.34472857],
       [0.89563832, 0.86713778, 0.72867624, 0.35957644]]), 
       
       'layer2': array([[0.67960263, 0.8047252 , 0.52845158, 0.86705177],
       [0.26881716, 0.98338414, 0.19343491, 0.74235373],
       [0.65898398, 0.56740798, 0.14294138, 0.42032431],
       [0.01902887, 0.07170327, 0.15735957, 0.05054243]]), 
       
       'layer3': array([[0.1777136 , 0.96184222, 0.4719506 , 0.25326198],
       [0.28045551, 0.66921599, 0.64272846, 0.48373489],
       [0.43109597, 0.36318979, 0.72755329, 0.62706487],
       [0.22128505, 0.87316348, 0.1486591 , 0.82709615]])
}
```

### Baseado em dados:
```
BIOMES = {
    "Desert":{
        "layer1":["Areia"],
        "layer2":["Cacto","Flor","Duna","Pedra"],
        "layer3":["Sky"]
    },
    "Forest":{
        "layer1":["Grama"],
        "layer2":["Árvore","Flor","Cogumelo","cipó","Cachoeira","Rio"],
        "layer3":["Sky"]
    },
    "Ice":{
        "layer1":["Neve"],
        "layer2":["Iglu","Cubo de gelo","Estalagmite","Gelo"],
        "layer3":["Sky"]
    },
    "Hills":{
        "layer1":["Stone"],
        "layer2":["Árvores","Pedra","Neve","Minerais"],
        "layer3":["Sky"]
    }
}

import random

aux = []
for i in BIOMES:
    aux.append(i)

a = random.choice(aux)

c = cube(dimension=(4,4,3), form="structure",data=BIOMES[a])


print(c.cube_)
print(f"\n {c.cube_["layer2"][0][1+1]}")
```
### Output:

```
{'layer1': [['Grama', 'Grama', 'Grama', 'Grama'], ['Grama', 'Grama', 'Grama', 'Grama'], ['Grama', 'Grama', 'Grama', 'Grama'], ['Grama', 'Grama', 'Grama', 'Grama']], 'layer2': [['Cachoeira', 'Cogumelo', 'Cachoeira', 'Flor'], ['Árvore', 'Cachoeira', 'Árvore', 'Flor'], ['Árvore', 'Flor', 'Flor', 'Árvore'], ['Árvore', 'cipó', 'cipó', 'Cachoeira']], 'layer3': [['Sky', 'Sky', 'Sky', 'Sky'], ['Sky', 'Sky', 'Sky', 'Sky'], ['Sky', 'Sky', 'Sky', 'Sky'], ['Sky', 'Sky', 'Sky', 'Sky']]}

Cachoeira
```
