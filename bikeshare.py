# Author: Jiahao Lai
# Start Date: Oct 29 2022
# End Date: Nov 02 2022
# Credit: Udacity

import time
import pandas as pd
import numpy as np

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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print('Would you like to see data for Chicago, New York City or Washington? Please type out the full city name')
    city = input().lower()
    city_list = ['chicago','new york city','new york','washington']
    while city not in city_list:
        city = input('Invalid input, please type the correct city name:\n').lower()

    if city == 'new york city' or city == 'new york':
        city = 'new york city'

    # get user input for month (all, january, february, ... , june)
    print('Which month? January, February, March, April, May or June? If you want to see all months, type \'all\'. Please type out the full month name.')
    month = input().lower()
    month_list = ['january','february','march','april','may','june','all']
    while month not in month_list:
        month = input('Invalid input, please type the correct month:\n').lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    print('Which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday? If you want to see all days, type \'all\'. Please type out the full day name.')
    day = input().lower()
    day_list = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']
    while day not in day_list:
        day = input('Invalid input, please type the correct day:\n').lower()

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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['hour'] = df['Start Time'].dt.hour
    # display the most common month
    top_month = df['month'].mode()[0]
    print(f'the most commonly month is : {top_month}')

    # display the most common day of week
    top_day = df['day_of_week'].mode()[0]
    print(f'the most commonly day of week is : {top_day}')

    # display the most common start hour
    # extract hour from the Start Time column to create an hour column
    top_hour = df['hour'].mode()[0]
    print(f'the most commonly start hour is : {top_hour}')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    top_start = df['Start Station'].mode()[0]
    print(f'the most commonly used start station is : {top_start}')

    # display most commonly used end station
    top_end = df['End Station'].mode()[0]
    print(f'the most commonly used end station is : {top_end}')
    # display most frequent combination of start station and end station trip
    top_pair = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print(f'the most frequent combination of start station and end station is: from {top_pair[0]} to {top_pair[1]}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df['Trip Duration'].sum()
    print(f'total travel time is : {total_time}')

    # display mean travel time
    time_mean = df['Trip Duration'].mean()
    print(f'the mean travel time is : {time_mean}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats_with_gender_and_year(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(f'counts of user types: ')
    for i in range(user_types.size):
        print(f'{user_types.index[i]}:  {user_types.values[i]}')
    print()
    # Display counts of gender
    gender = df['Gender'].value_counts()
    print(f'counts of gender : ')
    for i in range(gender.size):
        print(f'{gender.index[i]}:  {gender.values[i]}')
    print()
    # Display earliest, most recent, and most common year of birth
    earliest = df['Birth Year'].min()
    most_recent = df['Birth Year'].max()
    top_year = df['Birth Year'].mode()[0]
    print(f'the earliest year of birth is : {int(earliest)}')
    print(f'the most recent year of birth is : {int(most_recent)}')
    print(f'the most common year of birth is : {int(top_year)}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# for washington data:
def user_stats_without(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(f'the counts of user types is :')
    for i in range(user_types.size):
        print(f'{user_types.index[i]}:  {user_types.values[i]}')
    print()
    print('Sorry, Washington currently has no data for user\'s gender and birth year.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """Ask user whether to show individual trip data"""
    print('Would you like to view individual trip data? Type \'yes\' or \'no\'.')
    choice = input().lower()

    i = 0
    while choice != 'no':
        for i in range(i,i+5):
            print(f'[\n {df.iloc[i]} \n]')
        i = i+5
        print('Would you like to view individual trip data? Type \'yes\' or \'no\'.')
        choice = input().lower()

def main():

    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)

        # Since washington dataset has no columns of gender and year, we separately deal with it
        if city != 'washington':
            user_stats_with_gender_and_year(df)
        else:
            user_stats_without(df)
            
        # Ask user if want to see raw data (5 lines per time)
        raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
