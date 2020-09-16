import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters(city,month,day):
    
    while True:
        city = str(input("specify a city for 'chicago', new york city or 'washington')\n")).lower()
        if city not in ('chicago','new york city','washington'):
            print("not approperiate input")
        else: 
            break    
    
    while True:
        month = str(input("specify a month  (all, january, february, ... , june)\n")).lower()
        if month not in ('all','january','february','march','april','may','june'):
            print("not approperiate input")
        else:
            break
    while True:
        day = str(input("specify a day  (all, monday, tuesday, ... sunday)\n")).lower()
        if day not in ('all','monday','tuesday','wednesday','thursday','friday','saturday','sunday'):
            print("not approperiate input")
        else:
            break
    
    print('-'*40)
    
    return city,month,day

    print('Hello! Let\'s explore some US bikeshare data!')

def load_data(city,month,day):
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) +1
        df = df[df['month'] == month]
    
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df  

def time_stats(df):
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = pd.to_datetime(df['Start Time']).dt.time

    popular_month = df['month'].mode()[0]
    popular_day = df['day_of_week'].mode()[0]
    popular_hour = df['hour'].mode()[0]
        
    print("most popular month is",popular_month) 
    print("most popular day is",popular_day)
    print("most popular hour is",popular_hour)
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def station_stats(df):
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    popular_start_sation = df['Start Station'].mode()[0]
    popular_end_station = df['End Station'].mode()[0]
    frequent_combination = df.groupby(['Start Station','End Station']).size().nlargest(1)
    
    print("most popular start station is:",popular_start_sation) 
    print("most popular end station is:",popular_end_station)
    print("most popular combination of start station and end station trip is \n",frequent_combination)

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_travel_time = df['Trip Duration'].sum()
    mean_travel_time = df['Trip Duration'].mean()
    
    print("Total travel time is",total_travel_time) 
    print("Average travel time is",mean_travel_time) 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #  Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Count of users types is:\n",user_types)


    # Display counts of gender
    if 'Gender' in df:
        gender_counts = df['Gender'].value_counts()
        print("Count of gender is:\n",gender_counts)
    else:
        print("No provided data about gender for this city")

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_date = df['Birth Year'].min()
        most_recent_date = df['Birth Year'].max()
        most_common_date = df['Birth Year'].mode()[0]
        
        print("earliest year of birth is", earliest_date)
        print("most recent year of birth is",most_recent_date)
        print("most common year of birth is", most_common_date)
    else:
        print("No provided data about birth year for this city")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40) 
    
    
def raw_data(df):
    data = 0
    while True:
        answer = str(input("would you like to see raw dara? yes or no \n")).lower()
        if answer not in {'yes','no'}:
            answer = str(input("your input is wrong , Enter only yes or no \n")).lower()
        elif answer == 'yes':
            data += 5
            print(df.iloc[data : data + 5])
            again = input("would you like to see more data ? yes or no \n").lower()
            if again == 'no':
                break
        elif answer == 'no':        
            break
       

def main():
    while True:
        #city, month, day = get_filters()
        city, month, day = get_filters('','','')
        df = load_data(city, month, day)

        raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()     