import datetime
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Core Employer Set Project - Task4A - Data - Summer 2022 1.csv')


def mainmenu():
    print("\t\t****Welcome to the Dashboard****")
    print("\t\t****Please select an option from the menu below****")
    print()
    print('1) Return all current data')
    print('2) Return data for a specific region')
    print('3) percentage increase for a specific region')
    print('4) average number of rooms for a specific region')
    print('5) Plot average number of rooms by region')
    print('6) property type by region')
    print('7) Exit')
    print("****current date and time is****")
    print(datetime.datetime.now())
    print()

    return int(input("Please select an option: "))

def plot_property_type_by_region():
    df2 = df.loc[:, 'Region Code':'Property Type']
    result = pd.concat([df2], axis=1, join='inner')
    result.dropna(inplace=True)
    property_type_by_region = result.groupby('Region')['Property Type'].value_counts()
    property_type_by_region.unstack().plot(kind='bar', stacked=True)
    plt.xlabel('Region')
    plt.ylabel('Count of Property Types')
    plt.title('Property Type Distribution by Region')
    plt.xticks(rotation=45)
    plt.legend(title='Property Type')
    plt.tight_layout()
    plt.show()

# Function to plot average number of rooms by region
def plot_average_rooms_by_region():
    df2 = df.loc[:, 'Region Code':'Rooms']
    result = pd.concat([df2], axis=1, join='inner')
    result.dropna(inplace=True)
    average_rooms = result.groupby('Region')['Rooms'].mean()
    average_rooms.plot(kind='bar')
    plt.xlabel('Region')
    plt.ylabel('Average Number of Rooms')
    plt.title('Average Number of Rooms by Region')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def alldata():
    print(df)

def rooms_per_region():
    df2 = df.loc[:, 'Region Code':'Rooms']
    result = pd.concat([df2], axis=1, join='inner')
    result = pd.DataFrame(result)
    result.dropna(inplace=True)
    print(result)

def region_check(region, startdate, enddate):  # region, startdate, enddate

    df1 = df.loc[:, startdate:enddate]
    df2 = df.loc[:, 'Region Code':'Rooms']

    result = pd.concat([df2, df1], axis=1, join='inner').where(df2["Region"] == region)
    result = pd.DataFrame(result)
    result.dropna(inplace=True)
    print(result)
    ave = df1.mean()
    ave.plot()
    plt.show()
    return result
    
def percentage_increse(start_value, end_value):
    if start_value == 0:
        return float('inf')  # Infinite percentage increase if the start value is zero
    else:
        return ((end_value - start_value) / start_value) * 100

choice = mainmenu()
while choice == 1 or choice == 2 or choice == 3 or choice == 4 or choice == 5 or choice == 6 or choice == 7:
    if choice == 1:
        alldata()

    elif choice == 2:
        while True:
            print()

            region = input("Please enter the name of the region you would like to check:")
            region = region.capitalize()
            if region in df.Region.values:
                while True:
                    startdate = input("PLEASE ENTER A START DATE AS MONTH-YEAR e.g. JAN-20")
                    startdate = startdate.capitalize()
                    if startdate not in df.columns:
                        print("Error start date not found")
                    else:
                        while True:
                            enddate = input("PLEASE ENTER AN END DATE AS MONTH-YEAR e.g. JAN-20")
                            enddate = enddate.capitalize()
                            if enddate not in df.columns:
                                print("Error end date not found")
                            else:
                                region_check(region, startdate, enddate)
                                break
                        break
                break
            else:
                print("Region not found")
    elif choice == 3:
        region = input("Please enter the name of the region you would like to check the precentage increse of:")
        region = region.capitalize()
        if region in df.Region.values:
            startdate = input("PLEASE ENTER A START DATE AS MONTH-YEAR e.g. JAN-20")
            startdate = startdate.capitalize()
            if startdate not in df.columns:
                print("Error start date not found")
            else:
                enddate = input("PLEASE ENTER AN END DATE AS MONTH-YEAR e.g. JAN-20")
                enddate = enddate.capitalize()
                if enddate not in df.columns:
                    print("Error end date not found")
                else:
                    df1 = df.loc[:, startdate:enddate]
                    df2 = df.loc[:, 'Region Code':'Rooms']
                    result = pd.concat([df2, df1], axis=1, join='inner').where(df2["Region"] == region)
                    result = pd.DataFrame(result)
                    result.dropna(inplace=True)
                    if len(result) > 0:
                        start_value = result[startdate].iloc[0]
                        end_value = result[enddate].iloc[0]
                        percentage_increase = percentage_increse(start_value, end_value)
                        print(f"The percentage increase for {region} from {startdate} to {enddate} is {percentage_increase:.2f}%")
                    else:
                        print("No data available for the specified region and date range.")
        else:
            print("Region not found")
    elif choice == 4:
        region = input("Please enter the name of the region you would like to check the average number of rooms for:")
        region = region.capitalize()
        if region in df.Region.values:
            df2 = df.loc[:, 'Region Code':'Rooms']
            result = pd.concat([df2], axis=1, join='inner').where(df2["Region"] == region)
            result = pd.DataFrame(result)
            result.dropna(inplace=True)
            if len(result) > 0:
                average_rooms = result['Rooms'].mean()
                print(f"The average number of rooms for {region} is {average_rooms:.2f}")
            else:
                print("No data available for the specified region.")
        else:
            print("Region not found")
    elif choice == 7:
        print("Thank you for using the dashboard, goodbye!")
        break
    elif choice == 5:
        plot_average_rooms_by_region()
    elif choice == 6:
        df2 = df.loc[:, 'Region Code':'Property Type']
        result = pd.concat([df2], axis=1, join='inner')
        result.dropna(inplace=True)
        property_type_by_region = result.groupby('Region')['Property Type'].value_counts()
        print(property_type_by_region)
    else:
        print("Invalid input, please try again")
        mainmenu()
    choice = mainmenu()