from datetime import datetime
import matplotlib.pyplot as plt

class ExpenseTrackerApp:
    def __init__(self):
        #creating a reference to each class upon creating an instance(Object)
        self.categories = Category()
        self.expenses = Expense()
        self.income = Income()
        self.budget = Budget()
        self.report = Report()
        self.visualization = Visualization()
        self.settings = Settings()

    def main_menu(self):
        choice=0
        while choice!=8:
            print("\nExpense Tracker Main Menu")
            print("1.Manage Categories")
            print("2.Manage Expense")
            print("3.Manage Income")
            print("4.Manage Budget")
            print("5.Manage Reports")
            print("6.Manage Visualization")
            print("7.Manage Settings")
            print("8.Exit")
            
            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid input. Please enter a number.")

            
            if choice == 1:
                self.manage_categories()
            elif choice == 2:
                self.manage_expenses()
            elif choice == 3:
                self.manage_incomes()
            elif choice == 4:
                self.manage_budgets()
            elif choice == 5:
                self.manage_reports()
            elif choice == 6:
                self.manage_visualization()
            elif choice == 7:
                self.manage_settings()
            elif choice == 8:
                print("Exiting... Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def manage_categories(self):
        # Call required methods from Category class
        choice2 = 0
        while choice2!=5:
            print("1.Add Category")
            print("2.Edit Category")
            print("3.Delete Category")
            print("4.List Categories")
            print("5.Exit manage categories")
            choice2 = int(input("Enter your choice : "))

            # i wanted reference to Category class so i used self.categories which was initialized by default upon creating an object of ExpenseTrackerApp
            if choice2==1:
                category_id = int(input("Enter a category's id : "))
                category_name = input("Enter category's name : ")
                category_description = input("Enter some description about the category : ")
                self.categories.add_category(category_id,category_name,category_description)

            elif choice2==2:
                category_id = int(input("Enter a category's id : "))
                new_category_name = input("Enter edited category's name : ")
                new_category_description = input("Enter edited description about the category : ")
                self.categories.edit_category(category_id,new_category_name,new_category_description)

            elif choice2==3:
                category_id = int(input("Enter a category's id : "))
                self.categories.delete_category(category_id)

            elif choice2==4:
                self.categories.list_categories()

            elif choice2==5:
                print("Exiting Manage Categories")
        

    def manage_expenses(self):
        # call required methods from Expense class
        choice3 = 0
        while choice3!=6:
            print("1.Add Expense")
            print("2.Edit Expense")
            print("3.Delete Expense")
            print("4.View Expense by Category")
            print("5.View Expense by date range")
            print("6.Exit manage expenses")
            choice3 = int(input("Enter your choice : "))

            if choice3==1:
                expense_id = int(input("Enter an expense ID : "))
                amount = float(input("Enter expense amount : "))
                category = input("Enter a category : ")
                date = input("Enter a date (dd-mm-yyyy): ")
                try:
                # Parse the input string into a datetime object
                    parsed_date = datetime.strptime(date, "%d-%m-%Y")
                except ValueError:
                    print("Invalid date format. Please enter the date in dd-mm-yyyy format.")
                description = input("Enter some description : ")
                self.expenses.add_expense(expense_id,amount,category,parsed_date,description)


            elif choice3==2:
                expense_id = int(input("Enter an expense ID to edit : "))
                new_amount = float(input("Enter new expense amount : "))
                new_category = input("Enter new category : ")
                new_date = input("Enter a date (dd-mm-yyyy): ")
                try:
                # Parse the input string into a datetime object
                    parsed_date = datetime.strptime(new_date, "%d-%m-%Y")
                except ValueError:
                    print("Invalid date format. Please enter the date in dd-mm-yyyy format.")
                new_description = input("Enter new description : ")
                self.expenses.edit_expense(expense_id,new_amount,new_category,parsed_date,new_description)

            elif choice3==3:
                expense_id = int(input("Enter an expense ID to delete : "))
                self.expenses.delete_expense(expense_id)

            elif choice3==4:
                category = input("Enter a category to view it's expenses : ")
                self.expenses.view_expenses_by_category(category)

            elif choice3==5:
                start_date = input("Enter a start date (dd-mm-yyyy): ")
                end_date = input("Enter an end date (dd-mm-yyyy): ")
                try:
                # Parse the input string into a datetime object
                    parsed_start_date = datetime.strptime(start_date, "%d-%m-%Y")
                    parsed_end_date = datetime.strptime(end_date, "%d-%m-%Y")
                except ValueError:
                    print("Invalid date format. Please enter the date in dd-mm-yyyy format.")
                self.expenses.view_expenses_by_date_range(parsed_start_date,parsed_end_date)

            elif choice3==6:
                print("Exiting manage expenses!")

    def manage_incomes(self):
        # call required methods from Income class
        choice4 = 0
        while choice4!=5:
            print("1.Add Income")
            print("2.Edit Income")
            print("3.Delete Income")
            print("4.View Income by date range")
            print("5.Exit manage income")
            choice4 = int(input("Enter your choice : "))

            if choice4==1:
                income_id = int(input("Enter an Income ID : "))
                amount = float(input("Enter Income amount : "))
                source = input("Enter a source of income : ")
                date = input("Enter a date (dd-mm-yyyy): ")
                try:
                # Parse the input string into a datetime object
                    parsed_date = datetime.strptime(date, "%d-%m-%Y")
                except ValueError:
                    print("Invalid date format. Please enter the date in dd-mm-yyyy format.")
                description = input("Enter some description : ")
                self.income.add_income(income_id,amount,source,parsed_date,description)


            elif choice4==2:
                income_id = int(input("Enter an expense ID to edit : "))
                new_amount = float(input("Enter new income amount : "))
                new_source = input("Enter new source : ")
                new_date = input("Enter a date (dd-mm-yyyy): ")
                try:
                # Parse the input string into a datetime object
                    parsed_date = datetime.strptime(new_date, "%d-%m-%Y")
                except ValueError:
                    print("Invalid date format. Please enter the date in dd-mm-yyyy format.")
                new_description = input("Enter new description : ")
                self.income.edit_income(income_id,new_amount,new_source,parsed_date,new_description)

            elif choice4==3:
                income_id = int(input("Enter an income ID to delete : "))
                self.income.delete_income(income_id)

            elif choice4==4:
                start_date = input("Enter a start date (dd-mm-yyyy): ")
                end_date = input("Enter an end date (dd-mm-yyyy): ")
                try:
                # Parse the input string into a datetime object
                    parsed_start_date = datetime.strptime(start_date, "%d-%m-%Y")
                    parsed_end_date = datetime.strptime(end_date, "%d-%m-%Y")
                except ValueError:
                    print("Invalid date format. Please enter the date in dd-mm-yyyy format.")
                self.income.view_income_by_date_range(parsed_start_date,parsed_end_date)
            
            elif choice4==5:
                print("Exiting manage Income!")

    def manage_budgets(self):
        # call required methods from Budget class
        choice5 = 0
        while choice5!=5:
            print("1.Set Budget")
            print("2.Update Budget")
            print("3.Delete Budget")
            print("4.Check Budget status")
            print("5.Exit manage Budget")
            choice5 = int(input("Enter your choice : "))

            if choice5==1:
                budget_id = int(input("Enter an Budget ID : "))
                amount = float(input("Enter Budget amount : "))
                category = input("Enter a category : ")
                start_date = input("Enter a start date (dd-mm-yyyy): ")
                end_date = input("Enter an end date (dd-mm-yyyy): ")
                try:
                # Parse the input string into a datetime object
                    parsed_start_date = datetime.strptime(start_date, "%d-%m-%Y")
                    parsed_end_date = datetime.strptime(end_date, "%d-%m-%Y")
                except ValueError:
                    print("Invalid date format. Please enter the date in dd-mm-yyyy format.")
                self.budget.set_budget(budget_id,amount,category,parsed_start_date,parsed_end_date)


            elif choice5==2:
                budget_id = int(input("Enter an budget ID to edit : "))
                new_amount = float(input("Enter new budget amount : "))
                new_category = input("Enter new category : ")
                new_start_date = input("Enter a new start date (dd-mm-yyyy): ")
                new_end_date = input("Enter a new end date (dd-mm-yyyy): ")
                try:
                # Parse the input string into a datetime object
                    parsed_start_date = datetime.strptime(new_start_date, "%d-%m-%Y")
                    parsed_end_date = datetime.strptime(new_end_date, "%d-%m-%Y")
                except ValueError:
                    print("Invalid date format. Please enter the date in dd-mm-yyyy format.")
                self.budget.update_budget(budget_id,new_amount,new_category,parsed_start_date,parsed_end_date)

            elif choice5==3:
                budget_id = int(input("Enter a budget ID to delete : "))
                self.budget.delete_budget(budget_id)

            elif choice5==4:
                self.budget.check_budget_status()
            
            elif choice5==5:
                print("Exiting manage Budget!")
        

    def manage_reports(self):
        # # Call required methods from Report class
        # pass

        print("1. Generate Expense Report")
        print("2. Generate Income Report")
        print("3. Analyze Spending Trends")
        
        choice6 = int(input("Enter your choice: "))
        
        if choice6 == 1:
            start_date = input("Enter start date (dd-mm-yyyy): ")
            end_date = input("Enter end date (dd-mm-yyyy): ")
            # Convert to datetime format
            start_date = datetime.strptime(start_date, "%d-%m-%Y")
            end_date = datetime.strptime(end_date, "%d-%m-%Y")
            
            # Filter expenses based on date range
            # filtered_expenses = [i for i in self.expenses.Expense_List if start_date <= i['date'] <= end_date]
            self.report.generate_expense_report(start_date,end_date)
        
        elif choice6 == 2:
            start_date = input("Enter start date (dd-mm-yyyy): ")
            end_date = input("Enter end date (dd-mm-yyyy): ")
            # Convert to datetime format
            start_date = datetime.strptime(start_date, "%d-%m-%Y")
            end_date = datetime.strptime(end_date, "%d-%m-%Y")
            
            # Filter income based on date range
            # filtered_income = [i for i in self.income.Income_List if start_date <= i['date'] <= end_date]
            self.report.generate_income_report(start_date,end_date)
        
        elif choice6 == 3:
            start_date = input("Enter start date (dd-mm-yyyy): ")
            end_date = input("Enter end date (dd-mm-yyyy): ")
            # Convert to datetime format
            start_date = datetime.strptime(start_date, "%d-%m-%Y")
            end_date = datetime.strptime(end_date, "%d-%m-%Y")
            
            # Filter both income and expenses based on date range
            #filtered_expenses = [i for i in self.expenses.Expense_List if start_date <= i['date'] <= end_date]
            #filtered_income = [i for i in self.income.Income_List if start_date <= i['date'] <= end_date]
            
            self.report.analyze_spending_trends(start_date,end_date)
        else:
            print("Invalid choice! Please select a valid option.")

    def manage_visualization(self):
        # Call required methods from `Visualization` 
        # pass

        print("1. Generate Pie Chart of Expenses")
        print("2. Generate Bar Graph of Expenses")
        print("3. Compare Income vs Expenses")
        
        choice7 = int(input("Enter your choice: "))
        
        if choice7 == 1:
            # Get all expense categories and their totals
            categories = [i['name'] for i in self.categories.Category_List]
            expenses = [sum(i['amount'] for i in self.expenses.Expense_List if i['category'] == category['name']) for category in self.categories.Category_List]
            self.visualization.generate_pie_chart(categories, expenses)
        
        elif choice7 == 2:
            # Get all expense categories and their totals
            categories = [i['name'] for i in self.categories.Category_List]
            expenses = [sum(i['amount'] for i in self.expenses.Expense_List if i['category'] == category['name']) for category in self.categories.Category_List]
            self.visualization.generate_bar_graph(categories, expenses)
        
        elif choice7 == 3:
            # Generate comparison of income and expenses
            income_data = [income['amount'] for income in self.income.Income_List]
            expense_data = [expense['amount'] for expense in self.expenses.Expense_List]
            self.visualization.compare_income_vs_expenses(income_data, expense_data)
        else:
            print("Invalid choice! Please select a valid option.")

    def manage_settings(self):
        # # Allow updates to settings (e.g., default budget period)
        # pass

        print("1. Update Currency")
        #print("2. Set Default Budget Period")
        
        choice8 = int(input("Enter your choice: "))
        
        if choice8 == 1:
            new_currency = input("Enter new currency (e.g., INR): ")
            self.settings.update_currency(new_currency)
        
        # elif choice8 == 2:
        #     start_date = input("Enter start date of budget period (dd-mm-yyyy): ")
        #     end_date = input("Enter end date of budget period (dd-mm-yyyy): ")
        #     # Convert to datetime format
        #     start_date = datetime.strptime(start_date, "%d-%m-%Y")
        #     end_date = datetime.strptime(end_date, "%d-%m-%Y")
        #     self.settings.set_default_budget_period(start_date, end_date)
        else:
            print("Invalid choice! Please select a valid option.")


class Category:

    Category_List = [] #{'id':1,'name':'food','description':'lorem'},{},{}

    #using nested dictionaries of categories that are going to be stored in list
    def add_category(self,category_id,category_name,category_description):
        if any(i['id'] == category_id for i in self.Category_List):
            raise ValueError(f"Category with ID : {category_id} already exists!")

        d = {
            'id':category_id,
            'name':category_name,
            'description':category_description
        }

        self.Category_List.append(d)

    def edit_category(self,category_id,new_category_name,new_category_description):
        flag = 0
        for i in self.Category_List:
            if i['id']==category_id:
                i['name']=new_category_name
                i['description']=new_category_description
                flag=1
        if flag==0:
            print("Category ID not found !")

    def delete_category(self,category_id):
        flag = 0
        for i in self.Category_List:
            #in order to delete a dictionary inside the list , use filter with help of lambda , there might be other simpler approaches
            if i['id']==category_id:
                self.Category_List = list(filter(lambda i: i["id"] != category_id, self.Category_List))
                flag=1
                print("deleted Category successfully")
        if flag==0:
            print("Category ID not found !")        

    def list_categories(self):
        print(self.Category_List)

class Expense:

    Expense_List = []

    def add_expense(self,expense_id,amount,category,date,description):

        # if any(i['id'] == expense_id for i in self.Expense_List):
        #     raise ValueError(f"Ex with ID : {expense_id} already exists!")

        for i in self.Expense_List:
            if i['id']==expense_id:
                raise ValueError(f"Expense with ID : {expense_id} already exists!")
            
        
        if not any(i['name'] == category for i in Category.Category_List):
             raise ValueError(f"Category '{category}' does not exist!")
            
        d = {
            'id':expense_id,
            'amount':amount,
            'category':category,
            'date':date,
            'description':description
        }

        self.Expense_List.append(d)

    def edit_expense(self,expense_id,new_amount,new_category,new_date,new_description):
        flag = 0

        if not any(i['name'] == new_category for i in Category.Category_List):
             raise ValueError(f"Category '{new_category}' does not exist!")
        
        for i in self.Expense_List:
            if i['id']==expense_id:
                i['amount']=new_amount
                i['category']=new_category
                i['date']=new_date
                i['description']=new_description
                flag = 1
        if flag==0:
            print("Expense ID not found !")

    def delete_expense(self,expense_id):
        flag=0
        for i in self.Expense_List:
            if i['id']==expense_id:
                self.Expense_List.remove(i)
                flag=1
                print("deleted Expense successfully")
        if flag==0:
            print("Expense ID not found !")

    def view_expenses_by_category(self,category_name):

        if not any(i['name'] == category_name for i in Category.Category_List):
             raise ValueError(f"Category '{category_name}' does not exist!")
        
        flag = 0
        for i in self.Expense_List:
            if i['category']==category_name:
                print(i)
                flag = 1
        if flag==0:
            print("This category doesn't exist in Expenses(List)")

    def view_expenses_by_date_range(self,start_date,end_date):
        flag = 0
        for i in self.Expense_List:
            if start_date <= i['date'] <= end_date:
                print(i)
                flag = 1
        if flag == 0:
            print("No recorded expenses between the given dates!")


class Income:

    Income_List = []

    def add_income(self,income_id,amount,source,date,description):
        # if any(i['id'] == income_id for i in self.Income_List):
        #     raise ValueError(f"Income with ID : {income_id} already exists!")

        for i in self.Income_List:
            if i['id']==income_id:
                raise ValueError(f"Income with ID : {income_id} already exists!")
            
        d = {
            'id':income_id,
            'amount':amount,
            'source':source,
            'date':date,
            'description':description
        }

        self.Income_List.append(d)

    def edit_income(self,income_id,new_amount,new_source,new_date,new_description):
        flag = 0
        for i in self.Income_List:
            if i['id']==income_id:
                i['amount']=new_amount
                i['source']=new_source
                i['date']=new_date
                i['description']=new_description
                flag = 1
        if flag==0:
            print("Income ID not found !")

    def delete_income(self,income_id):
        flag=0
        for i in self.Income_List:
            if i['id']==income_id:
                self.Income_List.remove(i)
                flag=1
                print("deleted Income successfully")
        if flag==0:
            print("Income ID not found !")

    def view_income_by_date_range(self,start_date,end_date):
        flag = 0
        for i in self.Income_List:
            if start_date <= i['date'] <= end_date:
                print(i)
                flag = 1
        if flag == 0:
            print("No recorded Income between the given dates!")


class Budget:

    Budget_List = []

    def set_budget(self,budget_id,amount,category,start_date,end_date):
        for i in self.Budget_List:
            if i['id']==budget_id:
                raise ValueError(f"Budget with ID : {budget_id} already exists!")
            
        if not any(i['name'] == category for i in Category.Category_List):
             raise ValueError(f"Category '{category}' does not exist!")
            
        d = {
            'id':budget_id,
            'amount':amount,
            'category':category,
            'start_date':start_date,
            'end_date':end_date
        }

        self.Budget_List.append(d)

    def update_budget(self,budget_id,new_amount,new_category,new_start_date,new_end_date):

        if not any(i['name'] == new_category for i in Category.Category_List):
             raise ValueError(f"Category '{new_category}' does not exist!")

        flag = 0
        for i in self.Budget_List:
            if i['id']==budget_id:
                i['amount']=new_amount
                i['category']=new_category
                i['start_date']=new_start_date
                i['end_date']=new_end_date
                flag = 1
        if flag==0:
            print("Budget ID not found !")

    def delete_budget(self,budget_id):
        flag=0
        for i in self.Budget_List:
            if i['id']==budget_id:
                self.Budget_List.remove(i)
                flag=1
                print("deleted Budget successfully")
        if flag==0:
            print("Budget ID not found !")

    def check_budget_status(self):
        print(self.Budget_List)


class Report(Expense,Income):
    # def generate_expense_report(self,start_date,end_date):
    #     pass

    # def generate_income_report(self,start_date,end_date):
    #     pass

    # def analyze_spending_trends(self,start_date,end_date):
    #     pass

    def generate_expense_report(self, start_date, end_date):
        expense_data = []
        for expense in self.Expense_List:
            if start_date <= expense['date'] <= end_date:
                expense_data.append(expense['amount'])

        if expense_data:
            total_expense = sum(expense_data)
            print(f"Total Expenses between {start_date} and {end_date}: {total_expense}")
        else:
            print("No expenses found for the given date range.")

    def generate_income_report(self, start_date, end_date):
        income_data = []
        for income in self.Income_List:
            if start_date <= income['date'] <= end_date:
                income_data.append(income['amount'])

        if income_data:
            total_income = sum(income_data)
            print(f"Total Income between {start_date} and {end_date}: {total_income}")
        else:
            print("No income found for the given date range.")

    def analyze_spending_trends(self, start_date, end_date):
        category_expenses = {category['name']: 0 for category in Category.Category_List}
        
        for expense in self.Expense_List:
            if start_date <= expense['date'] <= end_date:
                category_expenses[expense['category']] += expense['amount']
        
        categories = list(category_expenses.keys())
        expenses = list(category_expenses.values())
        
        self.generate_bar_graph(categories, expenses)

    def generate_bar_graph(self, categories, expenses):
        plt.figure(figsize=(10, 6))
        plt.bar(categories, expenses, color='orange')
        plt.title('Spending by Category')
        plt.xlabel('Categories')
        plt.ylabel('Amount Spent')
        plt.xticks(rotation=45)
        plt.show()

class Visualization:
    # #categories -> list of strings , expense -> list of float values
    # def generate_pie_chart(self,categories,expenses): 
    #     pass

    # #categories -> list of strings , expense -> list of float values
    # def generate_bar_graph(self,categories,expenses):
    #     pass

    # #income_data -> list of float values , expense_data -> list of float values
    # def compare_income_vs_expenses(self,income_data,expense_data):
    #     pass

    # categories -> list of strings , expense -> list of float values
    def generate_pie_chart(self, categories, expenses):
        plt.figure(figsize=(8, 8))
        plt.pie(expenses, labels=categories, autopct='%1.1f%%', startangle=140)
        plt.title('Expense Distribution by Category')
        plt.show()

    # categories -> list of strings , expense -> list of float values
    def generate_bar_graph(self, categories, expenses):
        plt.figure(figsize=(10, 6))
        plt.bar(categories, expenses, color='blue')
        plt.title('Expenses by Category')
        plt.xlabel('Categories')
        plt.ylabel('Amount Spent')
        plt.xticks(rotation=45)
        plt.show()

    # income_data -> list of float values , expense_data -> list of float values
    def compare_income_vs_expenses(self, income_data, expense_data):
        categories = ['Income', 'Expense']
        values = [sum(income_data), sum(expense_data)]
        
        plt.figure(figsize=(6, 6))
        plt.bar(categories, values, color=['green', 'red'])
        plt.title('Income vs Expenses')
        plt.ylabel('Amount')
        plt.show()
    

class Settings:
    # def update_currency(self,new_currency):
    #     pass

    # def set_default_budget_period(self,start_date,end_date):
    #     pass

    def update_currency(self, new_currency):
        # Simple placeholder logic for currency change
        self.currency = new_currency
        print(f"Currency updated to {self.currency}")

    def set_default_budget_period(self, start_date, end_date):
        try:
            # Validate date format and convert
            self.start_date = datetime.strptime(start_date, "%d-%m-%Y")
            self.end_date = datetime.strptime(end_date, "%d-%m-%Y")
            print(f"Default budget period set from {self.start_date} to {self.end_date}")
        except ValueError:
            print("Invalid date format. Please use dd-mm-yyyy format.")

obj = ExpenseTrackerApp()
obj.main_menu()