import pandas as pd
from datetime import datetime
import os
import matplotlib.pyplot as plt

#TODO: Create a logo of the Program
logo  =''' 

  _____                                  _____               _             
 | ____|_  ___ __   ___ _ __  ___  ___  |_   _| __ __ _  ___| | _____ _ __ 
 |  _| \ \/ / '_ \ / _ \ '_ \/ __|/ _ \   | || '__/ _` |/ __| |/ / _ \ '__|
 | |___ >  <| |_) |  __/ | | \__ \  __/   | || | | (_| | (__|   <  __/ |   
 |_____/_/\_\ .__/ \___|_| |_|___/\___|   |_||_|  \__,_|\___|_|\_\___|_|   
            |_|                                                            
                          
'''
print(logo)
print("Welcome to Monthly Expenses manager 🎊🎉")

file_path = 'Monthly Expenses.csv'

#TODO: Create a function that will take user input to generate a new rows
def take_input():
    try:
        new_category = input("Enter category:")
        new_details = input("Enter details:")
        new_number_of_item = int(input('Enter no of item:'))
        new_per_price = float(input('Per product Price:'))
        new_total_bill = new_number_of_item * new_per_price
        while True:
            new_current_day = input("Enter date (dd-mm-yyyy): ")
            try:
                datetime.strptime(new_current_day, '%d-%m-%Y')  # Validate date format
                break
            except ValueError:
                print("Invalid date format. Please enter date in dd-mm-yyyy format.")
        new_rows = {'Category':new_category,
                'Details': new_details,
                'Date': new_current_day,
                'Quantity':new_number_of_item,
                'Price/Unit(in Rs)':new_per_price,
                'Total Bill':new_total_bill,
                }
        return new_rows
    except Exception as e:
        print(e)
        take_input()

#TODO: Create a function that will add new rows in the csv file
def add_expenses():
    content = pd.read_csv(file_path)
    new_row = pd.DataFrame([take_input()])
    content = pd.concat([content,new_row],ignore_index=True)
    content.to_csv(file_path,index=False)
    print('Data Inserted Successfully')

#TODO: Create a function that will view all the entries of the csv file
def view_expenses():
    content = pd.read_csv(file_path)
    pd.set_option('display.max_rows',None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)
    print(content)

#TODO: Create a function that will view all the entries per month
def filter_expenses():
    content = pd.read_csv(file_path)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)
    filter_option = int(input('How you want to filter you entries?\n1.Month\n2.Category\nEnter option(in number):'))
    match filter_option:
        case 1:
            content['Date'] = pd.to_datetime(content['Date'], format='%d-%m-%Y')
            try:
                # Take manual month and year input
                input_month = int(input("Enter month (1-12): "))
                input_year = int(input("Enter year (e.g. 2025): "))

                if 1>input_month>12 :
                    print("Invalid month. Please enter a value between 1 and 12.")
                    return

                # Filter data by the selected month and year
                filtered_data = content[(content['Date'].dt.month == input_month) &
                                        (content['Date'].dt.year == input_year)]

                if filtered_data.empty:
                    print(f"No expenses found for {input_month:02d}-{input_year}.")
                    return
                print(filtered_data)
            except ValueError:
                print("Invalid input. Please enter numeric values for month and year.")
        case 2:
            try:
                input_category = input("Enter Category:")
                filter_category = content[(content['Category']==input_category)]
                print(filter_category)
            except ValueError:
                print("Invalid category.Please enter valid Category")


#TODO: Create a function that will exit the command line
def exit_expenses():
    global running
    running = False

#TODO: Create a function that will remove a entry from CSV file
def remove_expenses():
    try:
        view_expenses()
        index_no = int(input('Enter the index you want to remove:'))
        content = pd.read_csv(file_path)
        content = content.drop(index = index_no)
        load_expenses(content)
    except Exception as e:
        print(e)
        remove_expenses()

#TODO: Create a function that will save the changes in the CSV file
def load_expenses(content):
    content.to_csv(file_path,index= False)
    print('Data loaded Successfully')

#TODO: Create a function that take index user want to edit, then edit that entry and Load the change in the CSV file
def edit_expenses():
    try:
        view_expenses()
        index_no = int(input('Enter the index you want to edit:'))
        content = pd.read_csv(file_path)
        content.loc[index_no] = take_input()
        load_expenses(content)
    except Exception as e:
        print(e)
        edit_expenses()


#TODO: Create a pie chart by filtering month and year
def plot_pie_chart():
    content = pd.read_csv(file_path)
    # Convert 'Date' column to datetime object
    content['Date'] = pd.to_datetime(content['Date'], format='%d-%m-%Y')

    try:
        # Take manual month and year input
        input_month = int(input("Enter month (1-12): "))
        input_year = int(input("Enter year (e.g. 2025): "))

        if 1>input_month>12 :
            print("Invalid month. Please enter a value between 1 and 12.")
            return

        # Filter data by the selected month and year
        filtered_data = content[(content['Date'].dt.month == input_month) &
                                (content['Date'].dt.year == input_year)]

        if filtered_data.empty:
            print(f"No expenses found for {input_month:02d}-{input_year}.")
            return

        # Group by category and plot pie chart
        category_totals = filtered_data.groupby('Category')['Total Bill'].sum()

        plt.figure(figsize=(8, 8))
        plt.pie(category_totals, labels=category_totals.index, autopct='%1.1f%%', startangle=140)
        plt.title(f'Expenses by Category for {input_month:02d}-{input_year}')
        plt.axis('equal')
        plt.show()

    except ValueError:
        print("Invalid input. Please enter numeric values for month and year.")

#TODO: Create a barchart by Category
def bar_chart_plot_per_category():
    content = pd.read_csv(file_path)
    category_summary = content.groupby('Category')['Total Bill'].sum()
    plt.figure(figsize=(10,6))
    plt.bar(category_summary.index,category_summary.values,color = 'lightgreen',edgecolor='black')
    plt.title('Total Expenses by Category')
    plt.xlabel('Category')
    plt.ylabel('Total Expenses(in Rs)')
    plt.xticks(rotation = 45)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()

    # Convert 'Date' column to datetime object
    content['Date'] = pd.to_datetime(content['Date'], format='%d-%m-%Y')

    try:
        # Take manual month and year input
        input_month = int(input("Enter month (1-12): "))
        input_year = int(input("Enter year (e.g. 2025): "))

        if 1 > input_month >12:
            print("Invalid month. Please enter a value between 1 and 12.")
            return

        # Filter data by the selected month and year
        filtered_data = content[(content['Date'].dt.month == input_month) &
                                (content['Date'].dt.year == input_year)]
        # Group by category and plot pie chart
        category_totals = filtered_data.groupby('Category')['Total Bill'].sum()

        plt.figure(figsize=(8, 8))
        plt.bar(category_totals.index,category_totals.values,color= 'lightblue',edgecolor= 'black')
        plt.title(f'Expenses by Category for {input_month:02d}-{input_year}')
        plt.xlabel("Category")
        plt.ylabel("Total Expenses(in Rs)")
        plt.xticks(rotation=45)
        plt.grid(axis='y')
        plt.tight_layout()
        plt.show()

    except ValueError:
        print("Invalid input. Please enter numeric values for month and year.")

#TODO: Show the per month expenses using Pie chart
def bar_chart_plot_per_month():
    content = pd.read_csv(file_path)
    content['Date'] = pd.to_datetime(content['Date'], format='%d-%m-%Y')
    content['Month-Year'] = content['Date'].dt.strftime('%B %Y')
    category_totals = content.groupby('Month-Year')['Total Bill'].sum()
    plt.figure(figsize=(4, 4))
    plt.bar(category_totals.index,category_totals.values,color= 'lightblue',edgecolor= 'black')
    plt.title(f'Expenses by month')
    plt.xlabel(f"Month")
    plt.ylabel("Total Expenses(in Rs)")
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()

#TODO: Display the total expenses of each month
def total_expenses():
    content = pd.read_csv(file_path)
    # Convert 'Date' column to datetime
    content['Date'] = pd.to_datetime(content['Date'], format='%d-%m-%Y')

    # Group by Year and Month
    content['Month-Year'] = content['Date'].dt.strftime('%B %Y')  # e.g., 'June 2025'
    monthly_totals = content.groupby('Month-Year')['Total Bill'].sum().reset_index()

    print("\n📅 Total Expenses Per Month:\n")
    for _, row in monthly_totals.iterrows():
        print(f"{row['Month-Year']}: ₹{row['Total Bill']:.2f}")

    expenses = content['Total Bill'].sum()
    print(f"Total Bill :{expenses}")

expenses = 0
running = True
while running:
    if not os.path.exists(file_path):
        print(f'Your total monthly expenses is {expenses}')
        category = input("Enter category:")
        details = input("Enter details:")
        number_of_item = int(input('Enter no of item:'))
        per_price = float(input('Per product Price:'))
        total_bill = number_of_item * per_price
        while True:
            current_day = input("Enter date (dd-mm-yyyy): ")
            try:
                datetime.strptime(current_day, '%d-%m-%Y')  # Validate date format
                break
            except ValueError:
                print("Invalid date format. Please enter date in dd-mm-yyyy format.")
        rows = {'Category': [category],
                'Details': [details],
                'Date': [current_day],
                'Quantity': [number_of_item],
                'Price/Unit(in Rs)': [per_price],
                'Total Bill': [total_bill]
                }
        df = pd.DataFrame(rows)
        df.to_csv(file_path,index=False)
        print("data has been saved successfully!")
        view_expenses()
    else:
        option = int(input("Select option:\n1.Add\n2.Edit\n3.Remove\n4.Display Total Entries\n5.Filter expenses\n6.Display Monthly Expense using pie chart\n7.Display Bar chart per category \n8.Display Bar chart per Month\n9.Total expenses\n10.Exit\nEnter option(number):"))
        match option:
            case 1:
                add_expenses()
            case 2:
                edit_expenses()
            case 3:
                remove_expenses()
            case 4:
                view_expenses()
            case 5:
                filter_expenses()
            case 6:
                plot_pie_chart()
            case 7:
                bar_chart_plot_per_category()
            case 8:
                bar_chart_plot_per_month()
            case 9:
                total_expenses()
            case 10:
                exit_expenses()


