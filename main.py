from cachorro import Cachorro
from ave import Ave
from macaco import Macaco

def movimentar(animal):
    print(f"\nTestando {animal.__class__.__name__}:")
    animal.movimento()
    

def som(animal):
    print(f"\nTestando {animal.__class__.__name__}")
    animal.emitir_Som()

if __name__ == "__main__":
    cachorro = Cachorro()
    ave = Ave()
    macaco = Macaco()

    movimentar(cachorro)
    movimentar(ave)
    movimentar(macaco)

    som(cachorro)
    som(ave)
    som(macaco)

