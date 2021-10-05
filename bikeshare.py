import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
city = ''
print(CITY_DATA)
def get_filters():
    month= 'all'
    day = 'all'
    months_data = ['january', 'february', 'march', 'april', 'may', 'june']
    days = [1,2,3,4,5,6,7]
    #days_data = ['sunday', 'monday', 'tuesday','wednesdy', 'thur', 'fri', 'sat']
    city = input("select a City: Chicago,new york city,Washington: \n").lower()
    while city not in CITY_DATA:
          print("invalid selection \n")

          city = input("please select a city: Chicago, new york city, Washington:  \n ").lower()
    if city in CITY_DATA:
       selection = input("would you like to filter by month, day, both or none: type month or day: \n").lower()
    while selection != "month" and selection != "day" and selection != "both" and selection !="none":
          print('make a selection \n')
          selection = input("would you like to filter by month or day: \n").lower()
          
    if selection == "month":
       month = input("select: January, February, March, April, May, June: \n").lower()
       while month not in months_data:
             month = input("select a valid month: January, February, March, April, May, June: \n").lower()
    if selection == "day":
       day = int(input("select a day of the week. eg,1 for Sun: \n"))
      # while day not in days_data:
       while day not in days:
             day = int(input("select a valid day of the week. eg,1 for Sun:\n "))
         
    if selection == "both":
       month = input('select a month: January february, March, April, May, June:\n ').lower()
       day = int(input('select a day of the week. eg 1 for Sun: '))
        
    if selection == 'none':
       print('Oops nothing to show ****')
                 
    print(city, month,day)  
    
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    # TO DO: get user input for month (all, january, february, ... , june)


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] =df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] =df['Start Time'].dt.hour
    
    if month != 'all':
       months = ['january', 'february', 'march', 'april', 'may', 'june']
   
       month = months.index(month)+1
       df = df[df['month'] == month]
       #return df['month']



    
    if day != 'all':
       df = df[df['day_of_week'] == day]

    #print(df)
    return df



  



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    #df =pd.read_csv(CITY_DATA[city])
    #print(df)
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('most common month.', common_month)

    # TO DO: display the most common day of week
    common_week = df['day_of_week'].mode()[0]
    print('most common day of the week.', common_week)

    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
    print('common hour.', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    #df['station'] = df['Start Station']
    common_station = df['Start Station'].mode()[0]
    print('most common start station.', common_station)
    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('most commonly used end station.', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    freq_start_end = df['Start Station'].mode()[0] and df['End Station'].mode()[0]
    #trip_duration = df['Trip Duration'].mode()[0]
    print('start and end trip duration.', freq_start_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    trip_duration = df['Trip Duration'].mode()[0]
    print('total time travel.', trip_duration)

    # TO DO: display mean travel time
    mean_calc = df['Trip Duration'].mean()
    print('mean travel time.', mean_calc)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print(user_type)

    # TO DO: Display counts of gender
   
    #if 'Gender' in df.columns:
    #print(df.head(4))
 
    if 'Gender' in df.columns:
       gender_type = df['Gender'].value_counts()
       print(gender_type)
    else:
        print('error ******* gender stats cannot be calculated because it does not appear in the data frame*****')
       
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
       most_resent_yob = df['Birth Year'].mode()[0]
       print('most resent, earliest and common year of birth.', most_resent_yob)
    else:
        print('***Sorry Birth year stats cannot be calculated because it does not appear in the data frame***')
        
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def display_data(df):
    view_data = input('would you like to view 5 rows of individual trip data?. Enter yes or no').lower()
    start_loc = 0
    end_loc = 5
    while (view_data == 'yes'):
        print(df.iloc[start_loc:end_loc])
        start_loc += 5
        end_loc += 5
        view_data = input('do you wish to continue').lower()
      
#view = display_data()
    


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
