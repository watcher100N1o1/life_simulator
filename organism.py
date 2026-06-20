class Organism:
    def __init__(self, name: str, energy: int):
        self.name = name
        self.energy = energy
    
    def eat(self, food_enery: float):
        self.energy += food_enery
        print(f"{self.name} съел и получил {food_enery} энергии.")
    
    def is_alive(self) -> bool:
        return self.energy > 0
    