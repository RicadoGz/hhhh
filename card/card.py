import random
from enum import Enum
from other import *
import csv

class Suite(Enum):
    SPADE = 0
    HEART = 1
    CLUB = 2
    DIAMOND = 3

class Card:
    def __init__(self, suite: Suite, value=13):
        self.value = value
        self.suite = suite

    def __str__(self):
        suites = '♠♥♣♦'
        values = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return f'{suites[self.suite.value]}{values[self.value]}'

class Deck:
    def __init__(self, num_decks=1):
        self.cards = []
        self.current=0
        for _ in range(num_decks):
            for suite in Suite:
                for value in range(1, 14):
                    self.cards.append(Card(suite, value))
        self.shuffle()

    def __str__(self):
        return "\n".join(str(card) for card in self.cards)

    def shuffle(self):
        random.shuffle(self.cards)
        with open('cards.csv', 'w', encoding='utf-8') as file:
            for i in self.cards:
                file.write(f'{i.suite.name},{i.value}\n')
    def choice(self):
        with open('cards.csv', 'r', encoding='utf-8') as file:
            b=list(csv.reader(file))
            try:
                while True:
                    go_on = input("go on? y or n?")
                    if go_on == 'y':
                        card = b[self.current]
                        self.current += 1
                        print(card)
                        b.remove(card)
                        with open('cards.csv', 'w', encoding='utf-8') as file:
                            writer = csv.writer(file)
                            writer.writerows(b)
                    else:
                        break
            except IndexError:
                return "game over"
class People:
    def __init__(self,name,money=10000):
        self.name=name
        self.money=money
        self.pname=["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", 
                   "Davis", "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin"]
class Dealer(People):
    def __init__(self, name, money=10000):
        super().__init__(name, money)
    def name(self):
            if user=="Dealer":
                pass

class player(People):
    def __init__(self, name, money=10000):
        super().__init__(name, money)
    def name(self):
        if user=="player":
            pass
p=People("tx")
pname=random.sample(p.pname,int(n_user))
# d = Deck()
# d.choice()
for i in list(pname):
    print(f"{i} join the game")
    pname.remove(i)
    i=Deck()
    i.choice()

# itertools.combinations('ABCDE', 3)

