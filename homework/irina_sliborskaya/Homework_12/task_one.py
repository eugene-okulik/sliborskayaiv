import statistics


class Flower:
    def __init__(self, colour=None, freshness=0, cost=0, stem_length=0, lifetime=0):
        self.colour = colour
        self.freshness = freshness
        self.cost = cost
        self.stem_length = stem_length
        self.lifetime = lifetime

    def __str__(self):
        return (f"{self.__class__.__name__} {self.colour} {self.cost}$, freshness: {self.freshness},"
                f"stem length: {self.stem_length}, lifetime: {self.lifetime}.")


class Rose(Flower):
    def __init__(self, colour, freshness):
        super().__init__(colour=colour, freshness=freshness, cost=15, stem_length=40, lifetime=7)


class Peon(Flower):
    def __init__(self, colour, freshness):
        super().__init__(colour=colour, freshness=freshness, cost=5, stem_length=25, lifetime=15)


class Alstroemeria(Flower):
    def __init__(self, colour, freshness):
        super().__init__(colour=colour, freshness=freshness, cost=10, stem_length=30, lifetime=14)


class Lisianthus(Flower):
    def __init__(self, colour, freshness):
        super().__init__(colour=colour, freshness=freshness, cost=5, stem_length=30, lifetime=16)


rose1 = Rose('Red', 2)
rose2 = Rose('White', 1)
rose3 = Rose('Soft Pink', 2)

peon1 = Peon("Purple", 1)
peon2 = Peon("White", 2)
peon3 = Peon("Soft Pink", 2)

alstroemeria1 = Alstroemeria("White", 3)
alstroemeria2 = Alstroemeria("Soft Pink", 1)
alstroemeria3 = Alstroemeria("Soft Yellow", 1)

lisianthus1 = Lisianthus("Soft Yellow", 2)
lisianthus2 = Lisianthus("Soft Pink", 1)
lisianthus3 = Lisianthus("White", 2)


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flowers(self, flowers_to_add):
        self.flowers.extend(flowers_to_add)

    def calculate_total_cost(self):
        return sum(flower.cost for flower in self.flowers)

    def print_flowers(self):
        for flower in self.flowers:
            print(flower)

    def calculate_avg_lifetime(self):
        return statistics.mean(flower.lifetime for flower in self.flowers)

    def sort_by(self, parameter):
        try:
            self.flowers.sort(key=lambda flower: getattr(flower, parameter))
            print(f"Sorted by '{parameter}':")
            self.print_flowers()
        except AttributeError:
            print("error")

    def find_flower_by_colour(self, wanted_colour):
        found = [flower for flower in self.flowers if flower.colour == wanted_colour]
        if found:
            for flower in found:
                print(flower)
        else:
            print("No such a flower")
        return found


soft_bouquet = Bouquet()
soft_bouquet.add_flowers([rose3, peon2, peon3, alstroemeria2, alstroemeria1])

#cost of bouquet
print(f"Cost of soft bouquet: {soft_bouquet.calculate_total_cost()}$")

#how long this bouquet will live
print(f"Lifetime of the soft bouquet: {soft_bouquet.calculate_avg_lifetime()}")

#sorting
print("\nSection with sorting:")
soft_bouquet.sort_by('stem_length')
soft_bouquet.sort_by('cost')
soft_bouquet.sort_by('lifetime')

#search
print("\nSection with searching:")
soft_bouquet.find_flower_by_colour("Soft Pink")
