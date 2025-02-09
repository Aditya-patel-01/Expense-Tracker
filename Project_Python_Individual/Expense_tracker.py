from datetime import datetime
import matplotlib.pyplot as plt
import json

DATA_FILE = "expense_tracker.json"

class ExpenseTrackerApp:
    def __init__(self):
        self.categories = Category()
        self.expenses = Expense(self)
        self.income = Income()
        self.report = Report(self)
        self.visualization = Visualization()
        self.load_data()

    def save_data(self):
        data = {
            "categories": self.categories.Category_List,
            "expenses": self.expenses.Expense_List,
            "income": self.income.Income_List
        }
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, default=str)

    def load_data(self):
        try:
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
                self.categories.Category_List = data.get("categories", [])
                self.expenses.Expense_List = data.get("expenses", [])
                self.income.Income_List = data.get("income", [])
        except (FileNotFoundError, json.JSONDecodeError):
            print("No previous data found. Starting fresh.")

    def main_menu(self):
        choice = 0
        while choice != 8:
            print("\nExpense Tracker Main Menu")
            print("1. Manage Categories")
            print("2. Manage Expense")
            print("3. Manage Income")
            print("4. Manage Reports")
            print("5. Manage Visualization")
            print("6. Exit")
            
            try:
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    self.manage_categories()
                elif choice == 2:
                    self.manage_expenses()
                elif choice == 3:
                    self.manage_incomes()
                elif choice == 4:
                    self.manage_reports()
                elif choice == 5:
                    self.manage_visualization()
                elif choice == 6:
                    print("Exiting... Saving data... Goodbye!")
                    self.save_data()
                    break
                else:
                    print("Invalid choice. Please try again.")
            except ValueError as f:
                print(f)
                print("Invalid input. Please enter a number.")
            except Exception as e:
                print(f"An error occurred: {e}")

    @staticmethod
    def parse_date(date_str):
        try:
            return datetime.strptime(date_str, "%d-%m-%Y")
        except ValueError:
            print("Invalid date format. Please use dd-mm-yyyy.")
            return None

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
        while choice3!=7:
            print("1.Add Expense")
            print("2.Edit Expense")
            print("3.Delete Expense")
            print("4.View Expense by Category")
            print("5.View Expense by date range")
            print("6.View All Expenses")
            print("7.Exit manage expenses")
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
                self.expenses.view_all_expenses()

            elif choice3==7:
                print("Exiting manage expenses!")

    def manage_incomes(self):
        # call required methods from Income class
        choice4 = 0
        while choice4!=6:
            print("1.Add Income")
            print("2.Edit Income")
            print("3.Delete Income")
            print("4.View Income by date range")
            print("5.View All Income Sources")
            print("6.Exit manage income")
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
                self.income.view_all_income_sources()

            elif choice4==6:
                print("Exiting manage Income!")

   

    def manage_reports(self):
        # Call required methods from Report class

        print("1. Generate Expense Report")
        print("2. Generate Income Report")
        #print("3. Analyze Spending Trends")
        
        choice6 = int(input("Enter your choice: "))
        
        if choice6 == 1:
            start_date = input("Enter start date (dd-mm-yyyy): ")
            end_date = input("Enter end date (dd-mm-yyyy): ")
            # Convert to datetime format
            start_date = datetime.strptime(start_date, "%d-%m-%Y")
            end_date = datetime.strptime(end_date, "%d-%m-%Y")
            
            # Filter expenses based on date range
            self.report.generate_expense_report(start_date,end_date)
        
        elif choice6 == 2:
            start_date = input("Enter start date (dd-mm-yyyy): ")
            end_date = input("Enter end date (dd-mm-yyyy): ")

            # Convert to datetime format
            start_date = datetime.strptime(start_date, "%d-%m-%Y")
            end_date = datetime.strptime(end_date, "%d-%m-%Y")
            
            # Filter income based on date range
            self.report.generate_income_report(start_date,end_date)
        
        else:
            print("Invalid choice! Please select a valid option.")

    def manage_visualization(self):
        # Call required methods from `Visualization` 
        

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



class Category:

    Category_List = [] #{'id':1,'name':'food','description':'lorem'},{},{}

    #using nested dictionaries of categories that are going to be stored in list
    def add_category(self,category_id,category_name,category_description):
        if any(i['id'] == category_id for i in self.Category_List):
            raise ValueError(f"Category with ID : {category_id} already exists!")

        self.Category_List.append({"id": category_id, "name": category_name, "description": category_description})

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

    def __init__(self, app):
        self.app = app  #  Store reference to ExpenseTrackerApp
        self.Expense_List = []

    def add_expense(self,expense_id,amount,category,date,description):

        #print("Category List at time of expense addition:", self.app.categories.Category_List)
     
        for i in self.Expense_List:
            if i['id']==expense_id:
                raise ValueError(f"Expense with ID : {expense_id} already exists!")
            
        if not any(i['name'] == category for i in self.app.categories.Category_List):
             raise ValueError(f"Category '{category}' does not exist!")
            
        self.Expense_List.append({"id": expense_id, "amount": amount, "category": category, "date": date, "description": description})

    def edit_expense(self,expense_id,new_amount,new_category,new_date,new_description):
        flag = 0

        if not any(i['name'] == new_category for i in self.app.categories.Category_List):
             raise ValueError(f"Category '{new_category}' does not exist!")
        
        # Convert only if new_date is a string
        if isinstance(new_date, str):
            new_date = datetime.strptime(new_date, "%Y-%m-%d %H:%M:%S")
        
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

        if not any(i['name'] == category_name for i in self.app.categories.Category_List):
             raise ValueError(f"Category '{category_name}' does not exist!")
        
        flag = 0
        for i in self.Expense_List:
            if i['category']==category_name:
                print(i)
                flag = 1
        if flag==0:
            print("This category doesn't exist in Expenses(List)")

    def view_expenses_by_date_range(self, start_date, end_date):
        flag = 0
        for expense in self.Expense_List:
            # Convert only if date is a string
            if isinstance(expense["date"], str):
                try:
                    expense["date"] = datetime.strptime(expense["date"], "%Y-%m-%d %H:%M:%S")
                except ValueError:
                    print(f"Invalid date format in expense: {expense['date']}")  # 🚨 Debugging print

            if start_date <= expense["date"] <= end_date:
                print(expense)
                flag = 1
        if flag == 0:
            print("No recorded expenses between the given dates!")


    def view_all_expenses(self):
        print(self.Expense_List)




class Income:

    Income_List = []

    def add_income(self,income_id,amount,source,date,description):
        # if any(i['id'] == income_id for i in self.Income_List):
        #     raise ValueError(f"Income with ID : {income_id} already exists!")

        for i in self.Income_List:
            if i['id']==income_id:
                raise ValueError(f"Income with ID : {income_id} already exists!")
            
        self.Income_List.append({"id": income_id, "amount": amount, "source": source, "date": date, "description": description})


    def edit_income(self,income_id,new_amount,new_source,new_date,new_description):
        flag = 0
        # Convert only if new_date is a string
        if isinstance(new_date, str):
           new_date = datetime.strptime(new_date, "%Y-%m-%d %H:%M:%S")

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


    def view_income_by_date_range(self, start_date, end_date):
        flag = 0
        for income in self.Income_List:
            # Convert only if date is still a string
            if isinstance(income["date"], str):
                try:
                    income["date"] = datetime.strptime(income["date"], "%Y-%m-%d %H:%M:%S")
                except ValueError:
                    print(f"Invalid date format in income: {income['date']}")

            if start_date <= income["date"] <= end_date:
                print(income)
                flag = 1
        if flag == 0:
            print("No recorded income between the given dates!")


    def view_all_income_sources(self):
        print(self.Income_List)


class Report(Expense,Income):
    
    def __init__(self, app):
        Expense.__init__(self, app)  # Initialize Expense with app
        Income.__init__(self)  # Initialize Income separately
        self.app = app  # Store reference to ExpenseTrackerApp

    def generate_expense_report(self, start_date, end_date):
        expense_data = []
        for expense in self.app.expenses.Expense_List:
            # Convert only if date is still a string
            if isinstance(expense["date"], str):
                try:
                    expense["date"] = datetime.strptime(expense["date"], "%Y-%m-%d %H:%M:%S")
                except ValueError:
                    print(f"Invalid date format in expense: {expense['date']}")

            if start_date <= expense["date"] <= end_date:
                expense_data.append(expense['amount'])

        if expense_data:
            total_expense = sum(expense_data)
            print(f"Total Expenses between {start_date} and {end_date}: {total_expense}")
        else:
            print("No expenses found for the given date range.")



    def generate_income_report(self, start_date, end_date):
        income_data = []
        for income in self.app.income.Income_List:
            # Convert only if date is still a string
            if isinstance(income["date"], str):
                try:
                    income["date"] = datetime.strptime(income["date"], "%Y-%m-%d %H:%M:%S")
                except ValueError:
                    print(f"Invalid date format in income: {income['date']}")

            if start_date <= income["date"] <= end_date:
                income_data.append(income['amount'])

        if income_data:
            total_income = sum(income_data)
            print(f"Total Income between {start_date} and {end_date}: {total_income}")
        else:
            print("No income found for the given date range.")


class Visualization:

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
    
obj = ExpenseTrackerApp()
obj.main_menu()