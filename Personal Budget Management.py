
class BudgetCategory:
    def __init__(self, category_name, allo_budget):
        self.__category_name = category_name
        self.__allo_budget = allo_budget
        self.expenses = 0

    def get_category_name(self):
        return self.__category_name
    
    def get_allo_budget(self):
        return self.__allo_budget
    
    def set_category_name(self):
        return self.__category_name
    
    def set_allo_budget(self):
        allo_budget += 0
        return self.__allo_budget

    def add_expenses(self, amount):
       if (amount > 0 and (self.get_allo_budget - self.expenses >= 0)): 
        self.expenses += amount
       else:
        print("Invalid expense amount")
       
    def display_budget(self, allo_budget, category_name, expenses):
        print(f"Category {category_name}, has a budget of {allo_budget} with a remaining budget of {allo_budget - expenses} after expenses.")
       
food_category = BudgetCategory("food", 800)
food_category.add_expenses(200)
food_category.display_budget()
print(food_category)