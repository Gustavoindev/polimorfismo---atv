Sistema de Animais em Python
Este repositório contém uma atividade desenvolvida em Python com o objetivo de demonstrar os conceitos de Programação Orientada a Objetos (POO), especificamente herança e polimorfismo.

Objetivo da Atividade
Aplicar os conceitos de:
Classe base, herança, métodos, polimorfismo

Utilizando um exemplo simples de um sistema de animais, onde cada animal possui comportamentos próprios de movimento e emissão de som.
Estrutura do Projeto:
animal.py
ave.py
cachorro.py
macaco.py
main.py

Classes do Sistema
Classe Base: Animal
Define comportamentos genéricos comuns a todos os animais:
movimento()
emitir_som()

Classes Derivadas
As classes abaixo herdam de Animal e sobrescrevem seus métodos:
Cachorro, Ave, Macaco

Cada classe implementa seu próprio comportamento para:
Movimento
Emissão de som

Polimorfismo
O polimorfismo é aplicado por meio das funções:
movimentar(animal)
som(animal)
Essas funções recebem um objeto do tipo Animal, mas executam comportamentos diferentes dependendo da classe instanciada.

Execução do Programa
No arquivo principal (main.py), são criadas instâncias das classes:
Cachorro, Ave, Macaco

Em seguida, essas instâncias são passadas para as funções que demonstram o polimorfismo.
Para executar:
python main.py
