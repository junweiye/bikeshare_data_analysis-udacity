import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': '/Users/junwei/Desktop/bikeshare-new/chicago.csv',
              'new york city': '/Users/junwei/Desktop/bikeshare-new/new_york_city.csv',
              'washington': '/Users/junwei/Desktop/bikeshare-new/washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Enter city_name: ")


    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("enter Month(all, january, february, ... , june): ")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("enter day of week (all, monday, tuesday, ... sunday): ")

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
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print("the most common month: ", popular_month)

    # TO DO: display the most common day of week
    popular_month = df['day_of_week'].mode()[0]
    print("the most common day of week: ",popular_month)
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("the most common start hour: ",popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
