# Expense Tracker

A comprehensive Python-based personal finance management application that helps users track expenses, manage income, and gain insights through detailed reports and visualizations.

## 🚀 Features

### Core Functionality
- **Category Management**: Create, edit, delete, and list expense categories
- **Expense Tracking**: Add, edit, delete, and view expenses with detailed information
- **Income Management**: Record and manage income sources with descriptions
- **Advanced Filtering**: View expenses by category or date range
- **Data Persistence**: Automatic saving and loading of data using JSON storage

### Reporting & Analytics
- **Expense Reports**: Generate detailed expense summaries for specific date ranges
- **Income Reports**: Track income patterns over selected periods
- **Data Visualization**: 
  - Pie charts showing expense distribution by category
  - Bar graphs displaying spending patterns
  - Income vs Expenses comparison charts

### User Experience
- **Console-based Interface**: Clean, intuitive menu-driven interface
- **Data Validation**: Robust error handling and input validation
- **Date Format Support**: Flexible date input using dd-mm-yyyy format

## 📋 Requirements

- Python 3.x
- matplotlib (for data visualization)
- datetime (built-in)
- json (built-in)

## 🛠️ Installation

1. Clone or download the project files
2. Install required dependencies:
   ```bash
   pip install matplotlib
   ```
3. Run the application:
   ```bash
   python Expense_tracker.py
   ```

## 🏗️ Project Structure

### Main Classes

#### `ExpenseTrackerApp`
The main application class that orchestrates all functionality:
- Manages the main menu and user interactions
- Handles data persistence (save/load from JSON)
- Coordinates between different modules

#### `Category`
Manages expense categories:
- `add_category(id, name, description)`: Create new categories
- `edit_category(id, new_name, new_description)`: Modify existing categories
- `delete_category(id)`: Remove categories
- `list_categories()`: Display all categories

#### `Expense`
Handles expense entries with category validation:
- `add_expense(id, amount, category, date, description)`: Add new expenses
- `edit_expense(id, amount, category, date, description)`: Modify expenses
- `delete_expense(id)`: Remove expenses
- `view_expenses_by_category(category)`: Filter by category
- `view_expenses_by_date_range(start_date, end_date)`: Filter by date range
- `view_all_expenses()`: Display all expenses

#### `Income`
Manages income records:
- `add_income(id, amount, source, date, description)`: Record income
- `edit_income(id, amount, source, date, description)`: Modify income entries
- `delete_income(id)`: Remove income records
- `view_income_by_date_range(start_date, end_date)`: Filter by date range
- `view_all_income_sources()`: Display all income

#### `Report`
Generates financial reports:
- `generate_expense_report(start_date, end_date)`: Expense summaries
- `generate_income_report(start_date, end_date)`: Income summaries

#### `Visualization`
Creates data visualizations using matplotlib:
- `generate_pie_chart(categories, expenses)`: Category distribution
- `generate_bar_graph(categories, expenses)`: Spending patterns
- `compare_income_vs_expenses(income_data, expense_data)`: Financial comparison

## 🎯 Usage Guide

### Getting Started
1. Launch the application
2. Start by adding expense categories (e.g., Food, Transportation, Entertainment)
3. Begin tracking your expenses and income

### Main Menu Options
1. **Manage Categories**: Create and organize expense categories
2. **Manage Expense**: Add, edit, delete, and view expenses
3. **Manage Income**: Track income sources and amounts
4. **Manage Reports**: Generate financial summaries
5. **Manage Visualization**: Create charts and graphs
6. **Exit**: Save data and close application

### Data Input Format
- **Dates**: Use dd-mm-yyyy format (e.g., 25-12-2024)
- **Amounts**: Enter as decimal numbers (e.g., 150.50)
- **IDs**: Use unique integer identifiers for each entry

## 💾 Data Storage

The application automatically saves all data to `expense_tracker.json` in the following format:
```json
{
  "categories": [...],
  "expenses": [...],
  "income": [...]
}
```

## 🔧 Key Features Explained

### Category Validation
- Expenses can only be added to existing categories
- Prevents orphaned expense entries
- Ensures data consistency

### Date Range Filtering
- View expenses and income for specific periods
- Useful for monthly/weekly financial reviews
- Supports flexible date range selection

### Data Visualization
- **Pie Charts**: Show percentage distribution of expenses by category
- **Bar Graphs**: Compare spending amounts across categories
- **Income vs Expenses**: Visual comparison of financial balance

### Error Handling
- Input validation for dates, amounts, and IDs
- Duplicate ID prevention
- Graceful handling of missing data files

## 🚨 Important Notes

- All data is automatically saved when exiting the application
- Categories must exist before adding expenses to them
- Date format must be dd-mm-yyyy for proper functionality
- Each expense and income entry requires a unique ID

## 🔮 Future Enhancements

Potential improvements for future versions:
- Budget setting and tracking
- Export functionality (CSV, PDF)
- Multiple currency support
- Web-based interface
- Mobile app integration
- Advanced analytics and forecasting

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Feel free to contribute to this project by:
- Reporting bugs
- Suggesting new features
- Submitting pull requests
- Improving documentation

---

**Happy Financial Tracking! 💰**
