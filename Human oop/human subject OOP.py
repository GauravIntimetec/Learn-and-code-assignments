from abc import ABC, abstractmethod

# Abstract class representing body parts
class HumanBody(ABC):
    def __init__(self, skin_color):
        self.skin_color = skin_color

    @abstractmethod
    def task_they_perform(self):
        pass

# Concrete classes representing body parts
class Head(HumanBody):
    def task_they_perform(self):
        return "Thinking and Sensing"

class Torso(HumanBody):
    def task_they_perform(self):
        return "Protecting vital organs"

class Arms(HumanBody):
    def task_they_perform(self):
        return "Moving objects"

class Legs(HumanBody):
    def task_they_perform(self):
        return "Supporting and Moving"

# Abstract class representing digestive system
class DigestiveSystem(ABC):
    @abstractmethod
    def digest_food(self):
        pass

# Concrete class representing digestive system
class HumanDigestiveSystem(DigestiveSystem):
    def digest_food(self):
        return "Food is being digested"

# Human class representing a person
class Human:
    def __init__(self, name, skin_color):
        self.name = name
        self.skin = Skin(skin_color)
        self.head = Head(skin_color)
        self.torso = Torso(skin_color)
        self.arms = Arms(skin_color)
        self.legs = Legs(skin_color)
        self.digestive_system = HumanDigestiveSystem()

# Skin class representing the skin of a person
class Skin:
    def __init__(self, color):
        self.color = color

# Example usage
human = Human("garvit", "Fair")

print(f"{human.name}'s skin color: {human.skin.color}")
print(f"{human.name}'s head task_they_perform: {human.head.task_they_perform()}")
print(f"{human.name}'s torso task_they_perform: {human.torso.task_they_perform()}")
print(f"{human.name}'s arms task_they_perform: {human.arms.task_they_perform()}")
print(f"{human.name}'s legs task_they_perform: {human.legs.task_they_perform()}")
print(f"{human.name}'s digestive system: {human.digestive_system.digest_food()}")
