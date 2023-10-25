from abc import ABC, abstractmethod

# Abstract class representing body parts
class HumanBody(ABC):
    def __init__(self, skin_color):
        self.skin_color = skin_color

    @abstractmethod
    def function(self):
        pass

# Concrete classes representing body parts
class Head(HumanBody):
    def function(self):
        return "Thinking and Sensing"

class Torso(HumanBody):
    def function(self):
        return "Protecting vital organs"

class Arms(HumanBody):
    def function(self):
        return "Moving objects"

class Legs(HumanBody):
    def function(self):
        return "Supporting and Moving"

# Human class representing a person
class Human:
    def __init__(self, name, skin_color):
        self.name = name
        self.skin = Skin(skin_color)
        self.head = Head(skin_color)
        self.torso = Torso(skin_color)
        self.arms = Arms(skin_color)
        self.legs = Legs(skin_color)

# Skin class representing the skin of a person
class Skin:
    def __init__(self, color):
        self.color = color

# Example usage
human = Human("John", "Fair")

print(f"{human.name}'s skin color: {human.skin.color}")
print(f"{human.name}'s head function: {human.head.function()}")
print(f"{human.name}'s torso function: {human.torso.function()}")
print(f"{human.name}'s arms function: {human.arms.function()}")
print(f"{human.name}'s legs function: {human.legs.function()}")
