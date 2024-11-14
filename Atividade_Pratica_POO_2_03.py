from abc import ABC, abstractmethod

class Drink(ABC):
    @abstractmethod
    def get_description(self):
        pass
    
    @abstractmethod
    def get_price(self):
        pass

class CaipiraBase(Drink):
    def get_description(self):
        return "Caipira base"
    
    def get_price(self):
        return 20.0

class CaipirinhaPronta(Drink):
    def get_description(self):
        return "Caipirinha (Cachaça, Limão, Gelo e Açúcar)"
    
    def get_price(self):
        return 25.0

class IngredientDecorator(Drink):
    def __init__(self, drink):
        self.drink = drink

class Saque(IngredientDecorator):
    def get_description(self):
        return f"{self.drink.get_description()}, Saquê"
    
    def get_price(self):
        return self.drink.get_price() + 5.0

class Abacaxi(IngredientDecorator):
    def get_description(self):
        return f"{self.drink.get_description()}, Abacaxi"
    
    def get_price(self):
        return self.drink.get_price() + 3.0

class Kiwi(IngredientDecorator):
    def get_description(self):
        return f"{self.drink.get_description()}, Kiwi"
    
    def get_price(self):
        return self.drink.get_price() + 4.0

class Adocante(IngredientDecorator):
    def get_description(self):
        return f"{self.drink.get_description()}, Adoçante"
    
    def get_price(self):
        return self.drink.get_price() + 1.0

class Acucar(IngredientDecorator):
    def get_description(self):
        return f"{self.drink.get_description()}, Açúcar"
    
    def get_price(self):
        return self.drink.get_price() + 2.0

def criar_drink():
    print("Bem-vindo ao Ressaca's Bar!")
    base = input("Escolha a base do seu drink (1: Caipira, 2: Caipirinha Pronta): ")
    
    if base == "1":
        drink = CaipiraBase()
    elif base == "2":
        drink = CaipirinhaPronta()
    else:
        print("Escolha inválida!")
        return

    while True:
        print(f"Seu drink até agora: {drink.get_description()} - Preço: R$ {drink.get_price()}")
        adicionar = input("Deseja adicionar um ingrediente? (s/n): ")
        
        if adicionar.lower() == "s":
            ingrediente = input("Escolha um ingrediente (saque, abacaxi, kiwi, acucar, adocante): ")
            if ingrediente == "saque":
                drink = Saque(drink)
            elif ingrediente == "abacaxi":
                drink = Abacaxi(drink)
            elif ingrediente == "kiwi":
                drink = Kiwi(drink)
            elif ingrediente == "acucar":
                drink = Acucar(drink)
            elif ingrediente == "adocante":
                drink = Adocante(drink)
            else:
                print("Ingrediente inválido!")
        elif adicionar.lower() == "n":
            break
        else:
            print("Escolha inválida!")

    print(f"Pedido finalizado: {drink.get_description()} - Preço: R$ {drink.get_price()}")

def main():
    print("Configuração do primeiro drink:")
    criar_drink()

    print("\nConfiguração do segundo drink:")
    criar_drink()

    print("\nConfiguração do terceiro drink:")
    criar_drink()

if __name__ == "__main__":
    main()

