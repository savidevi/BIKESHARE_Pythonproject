import time
import pandas as pd
import numpy as np
import datetime

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # user input for city (chicago, new york city, washington). 
    # user input for month (all, january, february, ... , june)
    # user input for day of week (all, monday, tuesday, ... sunday)
    start='yes'
    while start=='yes':
        city=input("\nSelct the city from (chicago, new york city, washington):\n ").lower()
        if city in CITY_DATA:
            month=input("\nSelect month from january to june or all: \n").lower()
            day=input("\nSelect day(sunday, monday and so on) or select all:\n ").lower()
            break
        else:
            print("Maybe be some mistake:")
            start = input('\nWould you like to start again? Enter yes or no.\n')
            if start.lower() != 'yes':
                break
            
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df=pd.read_csv(CITY_DATA[city])
    
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month

    df['day of week']=df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
                                              
        df=df[df['month']==month]
    if day != 'all':
                         
        df=df[df['day of week']==day.title()]                     


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("Most common month is: ",df['month'].mode()[0])

    # display the most common day of week
    print("Most common day is: ",df["day of week"].mode()[0])

    # display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    print("Most common start hour: ",df['hour'].mode()[0])
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    df['start_time']=start_time
    
    # display most commonly used start station
    print("Most commonly used start station: ",df['Start Station'].mode()[0])                     
    
    # display most commonly used end station
    print("Most commonly used end station: ",df['End Station'].mode()[0])
    
    # display most frequent combination of start station and end station trip
    print("Most common combination of start station and end station trip: ",(df['Start Station']+' , '+df['End Station']).mode()[0])
     

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    
    total_time=pd.to_timedelta(df['Trip Duration'].sum(),unit='s')
        
    
    print("Total travel time: {}".format(total_time))

    # display mean travel time
    avg_time=df['Trip Duration'].mean()/60
    print("Avg. travel time: {} minutes".format(avg_time))
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_info(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User info..\n')
    start_time = time.time()

    # Display counts of user types
    user_type=df['User Type'].value_counts()
    print('Count of user:\n ',user_type)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def user_stats(df):
    """Displays statistics on bikeshare users gender and Birth Year."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
        
    # Display counts of gender
    gen=df['Gender'].value_counts()
    print("Count of gender(male/female):\n ",gen)
    print()

    # Display earliest, most recent, and most common year of birth
    print("Earliest year of birth: ", df['Birth Year'].min())
    print("Most recent year of birth: ",df['Birth Year'].max())
    print("Most common year of birth: ",df['Birth Year'].mode()[0])
        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def show_data(df):
    # To show raw data of current city(5 rows at a time)
    show=input("\nDo you like to see raw data for current city yes/no:\n").lower()
    start=0
    while show =='yes':
        print(df.iloc[start:start+5])
        start+=5
        show=input("\nDo you want to see more data for current city  yes/no:\n").lower()
        if show !='yes' or start >= len(df.index)-1:
            break
            

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_info(df)
        """ washingto city don't have 'Gender' and 'Birth Year' columns.
            and user_stats() perform opration on those column only.
            that's why its put under condition.
        """
        if city !='washington':
            user_stats(df)
        show_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
