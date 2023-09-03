class cube: #Abstração de uma estrutura tridimensional de dados
    #form : random/structure (formato aleatorio ou com dados especificos)
    #dimension: parâmetro de dimensionamento, por padrão gera com x=2 y=2 e z=3
    def __init__(self, dimension=(3,3,3),form="random",data="") -> None:

        functions ={
            "random":self.random_(dimension),
            "structure":self.structure(dimension,data)
        }

    def random_(self,dimension): #gera as layers com dados aleatorios entre 0 e 1 e 4 casas decimais
        import numpy.matlib as npr
        
        self.cube_ = {}
        for i in range(1,dimension[2]+1):
            self.cube_["layer"+str(i)] = npr.rand((dimension[0],dimension[1]))
        

    def structure(self,dimension,data): #gera as layes baseada em dados passados
        pass
    """     for i in range(1,dimension[2]+1):
            print(i) """
            #self.cube_["layer"+str(i)] = npr.rand((dimension[0],dimension[1]))
        

 
BIOMES = {
    "Desert":{
        "Ground":"Areia",
        "Compose":["Cacto","Flor","Duna","Pedra"]
    },
    "Forest":{
        "Ground":"Grama",
        "Compose":["Árvore","Flor","Cogumelo","cipó","Cachoeira","Rio"]
    },
    "Ice":{
        "Ground":"Neve",
        "Compose":["Iglu","Cubo de gelo","Estalagmite","Gelo"]
    },
    "Hills":{
        "Ground":"Stone",
        "Compose":["Árvores","Pedra","Neve","Minerais"]
    }
}

c = cube()
#print(c.cube_["layer1"])

coord_dict = {}
print(c.cube_)
print(c.cube_["layer1"][(2,(1+1))])

""" aux = []
mask=np.random.random((3, 3))

for i in BIOMES:
    aux.append(i)

a = random.choice(aux) """