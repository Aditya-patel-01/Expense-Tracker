# Project_X_repo_2
Repository for indivdual python project for semester-III
Expense Tracker

Project Overview

The Expense Tracker is a Python-based personal finance management tool designed to help individuals efficiently track and manage their expenses and income. All transactions are recorded in INR, providing a clear view of financial health with insightful reports and visualizations.

Features
-------------------------------------------------------------------------------------------------
Core Features

1.Expense Categories
Add, edit, delete, and list categories (e.g., Food, Travel, Rent).
Assign expenses to specific categories for better organization.

2.Expense Management
Log daily expenses with details such as amount, date, payment method, and notes.
View, update, and delete expense entries.
Filter expenses by category or date range.

3.Income Tracking
Record income entries with source and date.
View income history within a selected date range.

4.Budget Setting 
Set monthly or weekly budgets for specific categories.
Track expenses against the budget and receive alerts when nearing the limit.

5.Reports and Analysis
Generate detailed reports for selected time periods.
Analyze spending patterns and trends.

6.Data Visualization
Display spending breakdowns using pie charts and bar graphs.
Compare income vs. expenses to assess financial balance.

7.Additional Features
Fixed Currency: All transactions are recorded in INR.
Simple User Interface: Easy-to-use console-based interface for seamless interaction.

-------------------------------------------------------------------------------------------------

Class Structure
1.Category
Manages expense categories.
Methods: add_category(), edit_category(), delete_category(), list_categories().

2.Expense
Handles expense entries.
Methods: add_expense(), edit_expense(), delete_expense(), view_expenses_by_category(), view_expenses_by_date_range().

3.Income
Manages income records.
Methods: add_income(), edit_income(), delete_income(), view_income_by_date_range().

4.Budget
Tracks and monitors budget limits for categories.
Methods: set_budget(), update_budget(), delete_budget(), check_budget_status().

5.Report
Generates financial reports.
Methods: generate_expense_report(), generate_income_report(), analyze_spending_trends().

6.Visualization
Creates visual representations of financial data.
Methods: generate_pie_chart(), generate_bar_graph(), compare_income_vs_expenses().

7.Settings
Manages configuration settings like default budget periods and notifications.
Methods: update_currency() (fixed to INR), set_default_budget_period().

-------------------------------------------------------------------------------------------------
Workflow
Add Categories
Create categories like Food, Travel, and Entertainment.

Log Expenses and Income
Record transactions with relevant details, all in INR.

Set Budgets
Allocate budgets for specific categories and monitor spending.

Generate Reports
View income and expense summaries for selected periods.

Visualize Data
Use charts to get insights into financial patterns.
-------------------------------------------------------------------------------------------------