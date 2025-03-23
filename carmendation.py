from experta import *

class CarPreference(Fact):
    """User preferences for car recommendation"""
    pass

class CarRecommendation(KnowledgeEngine):
    
    @Rule(Fact(budget='Low'), Fact(fuel_type='Petrol'), Fact(seating='5'), Fact(Adas='No'), Fact(speakers='Yes'))
    def budget_car(self):
        self.declare(Fact(recommendation='Hyundai Exter'))

    @Rule(Fact(budget='Medium'), Fact(fuel_type='Diesel'), Fact(seating='7'), Fact(Adas='Yes'), Fact(speakers='Yes'))
    def medium_car(self):
        self.declare(Fact(recommendation='Mahindra XUV-700'))

    @Rule(Fact(budget='High'), Fact(fuel_type='Diesel'), Fact(seating='5'), Fact(Adas='Yes'), Fact(speakers='Yes'))
    def high_car(self):
        self.declare(Fact(recommendation='Range Rover Velar'))

    @Rule(Fact(budget='E_medium'), Fact(fuel_type='Electric'), Fact(seating='5'), Fact(Adas='Yes'), Fact(speakers='Yes'))
    def e_medium(self):
        self.declare(Fact(recommendation='Tesla Model 3'))

    @Rule(Fact(budget='Very-High'), Fact(fuel_type='Petrol'), Fact(seating='2'), Fact(Adas='No'), Fact(speakers='Yes'))
    def very_high_car(self):
        self.declare(Fact(recommendation='Lamborghini SVJ'))

    @Rule(Fact(budget='F_high'), Fact(seating='7'), Fact(fuel_type='Diesel'), Fact(Adas='Yes'), Fact(speakers='Yes'))
    def f_high(self):
        self.declare(Fact(recommendation='Toyota Fortuner'))

    @Rule(Fact(budget='Hyper'), Fact(seating='2'), Fact(fuel_type='Petrol'), Fact(Adas='No'), Fact(speakers='Yes'))
    def hyper_car(self):
        self.declare(Fact(recommendation='Bugatti Chiron'))

engine = CarRecommendation()
engine.reset()

user_budget = input("Enter your budget (Low/Medium/High/E_medium/Very-High/F_high/Hyper): ").strip().capitalize()
user_fuel_type = input("Enter fuel type (Petrol/Diesel/Electric): ").strip().capitalize()
user_seating = input("Enter number of seats (2/5/7): ").strip()
user_Adas = input("Do you need ADAS? (Yes/No): ").strip().capitalize()
user_speakers = input("Do you need premium speakers? (Yes/No): ").strip().capitalize()

engine.declare(
    Fact(budget=user_budget),
    Fact(fuel_type=user_fuel_type),
    Fact(seating=user_seating),
    Fact(Adas=user_Adas),
    Fact(speakers=user_speakers)
)

engine.run()

# Get recommendation and display result
recommendation_found = False
for fact in engine.facts.values():
    if 'recommendation' in fact:
        print(f"\n Recommended Car: {fact['recommendation']}")
        recommendation_found = True

if not recommendation_found:
    print("\n No matching recommendation found. Try different inputs!")
from experta import *

class CarPreference(Fact):
    """User preferences for car recommendation"""
    pass

class CarRecommendation(KnowledgeEngine):
    
    @Rule(Fact(budget='Low'), Fact(fuel_type='Petrol'), Fact(seating='5'), Fact(Adas='No'), Fact(speakers='Yes'))
    def budget_car(self):
        self.declare(Fact(recommendation='Hyundai Exter'))

    @Rule(Fact(budget='Medium'), Fact(fuel_type='Diesel'), Fact(seating='7'), Fact(Adas='Yes'), Fact(speakers='Yes'))
    def medium_car(self):
        self.declare(Fact(recommendation='Mahindra XUV-700'))

    @Rule(Fact(budget='High'), Fact(fuel_type='Diesel'), Fact(seating='5'), Fact(Adas='Yes'), Fact(speakers='Yes'))
    def high_car(self):
        self.declare(Fact(recommendation='Range Rover Velar'))

    @Rule(Fact(budget='E_medium'), Fact(fuel_type='Electric'), Fact(seating='5'), Fact(Adas='Yes'), Fact(speakers='Yes'))
    def e_medium(self):
        self.declare(Fact(recommendation='Tesla Model 3'))

    @Rule(Fact(budget='Very-High'), Fact(fuel_type='Petrol'), Fact(seating='2'), Fact(Adas='No'), Fact(speakers='Yes'))
    def very_high_car(self):
        self.declare(Fact(recommendation='Lamborghini SVJ'))

    @Rule(Fact(budget='F_high'), Fact(seating='7'), Fact(fuel_type='Diesel'), Fact(Adas='Yes'), Fact(speakers='Yes'))
    def f_high(self):
        self.declare(Fact(recommendation='Toyota Fortuner'))

    @Rule(Fact(budget='Hyper'), Fact(seating='2'), Fact(fuel_type='Petrol'), Fact(Adas='No'), Fact(speakers='Yes'))
    def hyper_car(self):
        self.declare(Fact(recommendation='Bugatti Chiron'))

engine = CarRecommendation()
engine.reset()

user_budget = input("Enter your budget (Low/Medium/High/E_medium/Very-High/F_high/Hyper): ").strip().capitalize()
user_fuel_type = input("Enter fuel type (Petrol/Diesel/Electric): ").strip().capitalize()
user_seating = input("Enter number of seats (2/5/7): ").strip()
user_Adas = input("Do you need ADAS? (Yes/No): ").strip().capitalize()
user_speakers = input("Do you need premium speakers? (Yes/No): ").strip().capitalize()

engine.declare(
    Fact(budget=user_budget),
    Fact(fuel_type=user_fuel_type),
    Fact(seating=user_seating),
    Fact(Adas=user_Adas),
    Fact(speakers=user_speakers)
)

engine.run()

# Get recommendation and display result
recommendation_found = False
for fact in engine.facts.values():
    if 'recommendation' in fact:
        print(f"\n Recommended Car: {fact['recommendation']}")
        recommendation_found = True

if not recommendation_found:
    print("\n No matching recommendation found. Try different inputs!")
