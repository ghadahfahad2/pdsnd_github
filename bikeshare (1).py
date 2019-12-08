import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
valid_city=['chicago' ,'new york' , 'washington']
valid_month=['january', 'february', 'march', 'april', 'may', 'june','all']
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle  invalid inputs
    valid_city=['chicago' ,'new york' , 'washington']
    while True:
        city = input('Enter one of three city(chicago, new york, washington) >>')
        if city.lower() not in valid_city:
             print('Error >> Please choose one of the three cities')

        else:
             city=city.lower()
             break
    # TO DO: get user input for month (all, january, february, ... , june)

    valid_month=['january', 'february', 'march', 'april', 'may', 'june','all']
    while True:
        month = input('choose a month you want to filter by it ?(january, february, march, april, may, june ) >>')
        if month.lower() not in valid_month:
             print('Error >> Please choose one of valid day or all ')

        else:
             month=month.lower()
             break


    # TO DO: input user  for day of week (all, monday, tuesday, ... sunday)

    valid_day=['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday' ,'all']
    while True:
        day = input('choose a day of week you want to filter by it ?(monday, tuesday, wednesday,thursday,     friday, saturday,sunday) Or all >>')
        if day.lower() not in valid_day:
             print('Error >> Please choose one of valid day or all ')

        else:
             day=day.lower()
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
       # load data file
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        month =  valid_month.index(month) + 1
        df = df[ df['month'] == month ]

    if day != 'all':
        df = df[ df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_monnth=df['month'].mode()[0]
    print('The most common month is :'+valid_month[most_common_monnth].title()+'/n')

    # TO DO: display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print("The most common day of week is : " + common_day_of_week+'/n')
    # TO DO: display the most common start hour
    common_start_hour = df['hour'].mode()[0]
    print("The most common start hour is: " + str(common_start_hour)+'/n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station is: " + common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station is: " + common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    frequent_combination = (df['Start Station'] + "," + df['End Station']).mode()[0]
    print("The most frequent combination of start station and end station trip is : " +           str(frequent_combination.split(",")))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print("Total travel time :", total_travel)


    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("Mean travel time :", mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Counts of user types:\n")
    user_counts = df['User Type'].value_counts()

    # TO DO: Display counts of gender
    print("Counts of gender:\n")
    gender_counts = df['Gender'].value_counts()

    # TO DO: Display earliest, most recent, and most common year of birth
    print("\n earliest year of birth")
    print(max(df['Birth Year']))

    print("\n most recent year of birth")
    print(min(df['Birth Year']))

    print("\n most common year of birth")
    print(df['Birth Year'].mode())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
