import time
import pandas as pd
import numpy as np

months = ['january', 'february', 'march', 'april', 'may', 'june']
days = ['monday', 'tuesday', 'wednesday',
        'thursday', 'friday', 'saturday', 'sunday']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    """
    getting all required user inputs to start the operations
    these inputs includes choosing the city, the type of fillter to use (day, month , both)
    """
    # add defult value for day and month so if the user didn't spicifiy the application wont break
    # adding new comment for github project
    # first change for refactoring branch
    month = 'all'
    day = 'all'
    while True:
        try:
            city = input(
                "Please choose one of the cities(chicago, new york city, washington): ").lower()
            if city == "chicago" or city == "new york city" or city == "washington":
                break
            else:
                print("sorry only one of the mentioned cities, please try again")
        except:
            print("something went wrong, please try again")

    while True:
        try:
            fillter = input(
                "Please choose filltering type (day, month, both): ").lower()
            if fillter == "day":
                while True:
                    try:
                        day = input(
                            "please input day of week (monday, tuesday, ... sunday):").lower()
                        if day in days:
                            break
                        else:
                            print("please choose the right day, please try again")
                    except:
                        print("something went wrong, please try again")
                break
            elif fillter == "month":
                while True:
                    try:
                        month = input(
                            "please input a month (january, february, ... , june):").lower()
                        if month in months:
                            break
                        else:
                            print("please choose the right month, please try again")
                    except:
                        print("something went wrong, please try again")
                break
            elif fillter == "both":
                while True:
                    try:
                        day = input(
                            "please input day of week (monday, tuesday, ... sunday):").lower()
                        if day in days:
                            break
                        else:
                            print("please choose the right day, please try again")
                    except:
                        print("something went wrong, please try again")
                while True:
                    try:
                        month = input(
                            "please input a month (january, february, ... , june)").lower()
                        if month in months:
                            break
                        else:
                            print("please choose the right month, please try again")
                    except:
                        print("something went wrong, please try again")
                break
            else:
                print("sorry only one of the mentioned types, please try again")
        except:
            print("something went wrong, please try again")

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
    df = pd.read_csv("{}.csv".format(city.replace(" ", "_")))

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month'] = df['Start Time'].apply(lambda x: x.month)
    df['day_of_week'] = df['Start Time'].apply(
        lambda x: x.strftime('%A').lower())

    if month != 'all':
        month = months.index(month) + 1
        df = df.loc[df['month'] == month, :]

    if day != 'all':
        df = df.loc[df['day_of_week'] == day, :]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("The most common month : {}".format(
        months[df['month'].mode()[0] - 1].title())
    )

    # display the most common day of week
    print("The most common day of the week: {}".format(
        df['day_of_week'].mode()[0].title())
    )

    # display the most common start hour
    df['start_hour'] = df['Start Time'].dt.hour
    print("The most common start hour: {}".format(
        str(df['start_hour'].mode()[0]))
    )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("The most common start station: {} ".format(
        df['Start Station'].mode()[0])
    )

    # display most commonly used end station
    print("The most common end station: {}".format(
        df['End Station'].mode()[0])
    )

    # display most frequent combination of start station and end station trip
    df['routes'] = df['Start Station'] + " " + df['End Station']
    print("The most common start and end routes: {}".format(
        df['routes'].mode()[0])
    )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    df['duration'] = df['End Time'] - df['Start Time']

    # display total travel time
    # using days format
    print("The total travel time is: {}".format(
        str(df['duration'].sum()))
    )

    # display mean travel time
    # using days format
    print("The mean travel time is: {}".format(
        str(df['duration'].mean()))
    )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("Here are the counts of various user types:")
    # just like in the project practise question
    print(df['User Type'].value_counts())

    if 'Gender' in df:
        # Display counts of gender
        print("Here are the counts of gender:")
        print(df['Gender'].value_counts())
    else:
        print("Sorry the gender information is not available.")

        # Display earliest, most recent, and most common year of birth
    if 'Birth_Year' in df:
        print("The earliest birth year is: {}".format(
            str(int(df['Birth Year'].min())))
        )
        print("The latest birth year is: {}".format(
            str(int(df['Birth Year'].max())))
        )
        print("The most common birth year is: {}".format(
            str(int(df['Birth Year'].mode()[0])))
        )
    else:
        print("Sorry the birthday information is not available.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    """
    Display contents of the CSV file to the display as requested by
    the user.

    this function works perfectly
    """

    start_loc = 0
    end_loc = 5
    while True:
        try:
            raw = input("Do you want to see the raw data?yes/no: ").lower()

            if raw == 'yes':
                    print(df.iloc[start_loc:end_loc, :])
                    start_loc += 5
                    end_loc += 5
            elif raw == 'no':
                break
        except:
            print("something went wrong, please try again")

def main():

    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_data(df)

        end = input("Do you wish to continue?yes/no: ").lower()
        if end == 'no':
            break


if __name__ == "__main__":
    main()
