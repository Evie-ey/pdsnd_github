import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday' 'saturday', 'all' ]

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
    city = input().lower()
    while(city not in  CITY_DATA):
      print("Please enter Chicago, New York City or Washington")
      city = input().lower()
    print(city)


    # TO DO: get user input for month (all, january, february, ... , june)
    print('Which month would you like to get data about--(all, january, february, ... , june)')
    month = input().lower()
    while (month not in months):
      print('Please enter all, january, february, ... , june')
      month = input().lower()
    print(month)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    print('Which day would you like to get data about--(all, Monday, Tuesday, ... , Sunday)')
    day = input().lower()
    while (day not in days):
      print('Please enter a day of the week, Sunday to Monday')
      day = input().lower()
    print(day)

#     if(day != 'all'):
#         day = days.index(day) + 1
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
    df['End Time'] = pd.to_datetime(df['End Time'])

    df['month'] = df['Start Time'].dt.month
    df['month'] = df['End Time'].dt.month

    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['day_of_week'] = df['End Time'].dt.weekday_name

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    most_common_month = df['month'].mode()[0]
    print('Most common month: {}'.format(months[most_common_month-1]))

    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    most_common_day = df['day_of_week'].mode()[0]
    print('Most common day: {}'.format(most_common_day))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print('Most start hour: {}'.format(most_common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('Commonly used start station: {}'.format(most_common_start_station))

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('Commonly used end station: {}'.format(most_common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    frequent_combination = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print('Frequent combination of start and finish: {} and {}'.format(frequent_combination[0],                     frequent_combination[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time: {}'.format(total_travel_time))
    # TO DO: display mean travel time
    total_mean_time = df['Trip Duration'].mean()
    print('Total mean time: {}'.format(total_mean_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()

    print('Counts of User Types:\n {}'.format(user_types))

    if (city != 'washington'):
        # TO DO: Display counts of gender
        gender = df['Gender'].value_counts()

        print('Counts of gender:\n {}'.format(user_types))

        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_year = df['Birth Year'].min()
        print("Earliest Year of Birth: {}".format(earliest_year))

        recent_year = df['Birth Year'].max()
        print("Recent Year of Birth: {}".format(recent_year))

        common_year = df['Birth Year'].mode()[0]
        print("Common Year of Birth: {}".format(common_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?")
    start_loc = 0
    while (True):
        if(view_data == 'yes'):
            print(df.iloc[start_loc: start_loc + 5])
            start_loc += 5
        else:
            break

        view_display = input("Do you wish to continue?: ").lower()
        view_data = view_display


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
