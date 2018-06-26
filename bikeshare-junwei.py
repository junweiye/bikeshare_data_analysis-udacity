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
    city = input("Enter city_name(chicago, new york city, washington): ").lower()
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("enter Month(all, january, february, ... , june): ").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("enter day of week (all, monday, tuesday, ... sunday): ").lower()

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


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station_types = df['Start Station'].value_counts().index.tolist()# https://stackoverflow.com/questions/35523635/extract-values-in-pandas-value-counts
    most_commonly_used_start_station = start_station_types[0]

    print("most_commonly_used_start_station: ",most_commonly_used_start_station)


    # TO DO: display most commonly used end station
    end_station_types = df['End Station'].value_counts().index.tolist()
    most_commonly_used_End_station = end_station_types[0]
    print("most_commonly_used_End_station: ",most_commonly_used_End_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['combined']=df['Start Station']+' to '+df['End Station']
    #https://stackoverflow.com/questions/39291499/how-to-concatenate-multiple-column-values-into-a-single-column-in-panda-datafram
    most_frequent_combination = df['combined'].value_counts().index.tolist()[0]
    print("most_frequent_combination: ",most_frequent_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("total_travel_time: ",total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("mean_travel_time: ",mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    while True:
        try:
            user_types = df['User Type'].value_counts()
            print('user_types:\n',user_types)
            # TO DO: Display counts of gender
            counts_of_gender = df["Gender"].value_counts()
            print('\ncounts_of_gender:\n',counts_of_gender)
            # TO DO: Display earliest, most recent, and most common year of birth
            earliest_year_of_birth = int(df['Birth Year'].min())
            most_recent_year_of_birth = int(df['Birth Year'].max())
            most_common_year_of_birth = int(df['Birth Year'].mode()[0])
            print("\nearliest_year_of_birth: ",earliest_year_of_birth)
            print("most_recent_year_of_birth: ",most_recent_year_of_birth)
            print("most_common_year_of_birth: ",most_common_year_of_birth)

            print("\nThis took %s seconds." % (time.time() - start_time))
            print('-'*40)
            break
        except KeyError:
            print('washington is lacking of gender & birth Year columns')
            break

def main():
    while True:
        try:
            city, month, day = get_filters()
            df = load_data(city, month, day)
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)

        except KeyError:
            print("city input unvalid，please re-enter city name in(chicago, new_york_city, washington)")
        except ValueError:
            print("month input unvalid,please re-enter month name in(all, january, february, ... , june)")
        except IndexError:
            print("day_of_week input unvalid,please re-enter month name in(all, monday, tuesday, ... sunday)")

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
