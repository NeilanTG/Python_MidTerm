#1
import scores
total = 0
for i in range (100):
    name = input("Please enter your name: ")
    total += scores.Get_score(name)
    
average = scores.Get_average(total, 100)

#2
import matplotlib.pyplot as plt

def read_steps_file(filename):
    """Reads the steps.txt file and returns a list of steps per day."""
    with open(filename, 'r') as file:
        steps = [int(line.strip()) for line in file]
    return steps

def get_steps_on_date(steps, month, day):
    """Returns the number of steps taken on a given date (MM/DD)."""
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_of_year = sum(days_in_months[:month-1]) + day
    return steps[day_of_year - 1]

def calculate_monthly_averages(steps):
    """Calculates the average number of steps taken for each month."""
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    averages = []
    index = 0
    for days in days_in_months:
        month_steps = steps[index:index+days]
        averages.append(sum(month_steps) / days)
        index += days
    return averages

def plot_steps(steps):
    """Plots the number of steps taken each day of the year."""
    plt.figure(figsize=(10, 5))
    plt.plot(range(1, 366), steps, label='Steps per day', color='blue')
    plt.xlabel('Day of the Year')
    plt.ylabel('Number of Steps')
    plt.title('Daily Steps in 2019')
    plt.legend()
    plt.grid()
    plt.show()

def main():
    filename = 'steps.txt'
    steps = read_steps_file(filename)
    
    # Task 2.1: Display steps taken on March 1st (03/01)
    march_first_steps = get_steps_on_date(steps, 3, 1)
    print(f"Steps taken on March 1st: {march_first_steps}")
    
    # Task 2.2: Display average number of steps taken each month
    monthly_averages = calculate_monthly_averages(steps)
    for i, avg in enumerate(monthly_averages, start=1):
        print(f"Average steps in month {i:02d}: {avg:.2f}")
    
    # Task 2.3: Plot daily steps for the year
    plot_steps(steps)

#3
def primes(n=1):
    for i in range (n,101):
        if isPrime(i):
            yield i
        
      

def isPrime(n):
    if n==1:
        return False
    for t in range (2,n):
        if n % t == 0 :
            return False
    return True

x=primes()
print(next(x))
print(next(x))
print(next(x))


#4
def read_temperature_data(date_file, min_temp_file, max_temp_file, avg_temp_file):
    """Reads data from the files and stores it in a 2D list."""
    with open(date_file, 'r') as df, open(min_temp_file, 'r') as minf, open(max_temp_file, 'r') as maxf, open(avg_temp_file, 'r') as avgf:
        dates = [line.strip() for line in df]
        min_temps = [int(line.strip()) for line in minf]
        max_temps = [int(line.strip()) for line in maxf]
        avg_temps = [int(line.strip()) for line in avgf]

    temp_data = [[dates[i], min_temps[i], max_temps[i], avg_temps[i]] for i in range(len(dates))]
    return temp_data

def find_hottest_day(temp_data):
    hottest_day = max(temp_data, key=lambda x: x[2])
    return hottest_day[0]

def find_coldest_day(temp_data):
    coldest_day = min(temp_data, key=lambda x: x[1]) 
    return coldest_day[0]

def find_avg_temp_on_date(temp_data, date):
    for record in temp_data:
        if record[0] == date:
            return record[3]  
    return None

def main():
    date_file = 'dateFile.txt'
    min_temp_file = 'minTempFile.txt'
    max_temp_file = 'maxTempFile.txt'
    avg_temp_file = 'avgTempFile.txt'

    temp_data = read_temperature_data(date_file, min_temp_file, max_temp_file, avg_temp_file)

    hottest_day = find_hottest_day(temp_data)
    coldest_day = find_coldest_day(temp_data)
    avg_temp = find_avg_temp_on_date(temp_data, '02/01/2016')

    print(f"Hottest day in the year was {hottest_day}")
    print(f"Coldest day in the year was {coldest_day}")
    print(f"Average temperature on 02/01/2016 was {avg_temp}")

#OR 

# Read data from files (assuming lists are already created)
dates = ["01/01/2016", "01/02/2016", "01/03/2016", "12/19/2016", "08/12/2016"]
min_temps = [32, 30, 28, 10, 25]
max_temps = [50, 45, 48, 20, 100]  # 100 is the highest max temp
avg_temps = [41, 38, 37, 15, 62]

# Find index of the hottest day
hottest_index = max_temps.index(max(max_temps))  # Finds index of highest max temp

# Get the corresponding date
hottest_day = dates[hottest_index]

print(f"Hottest day in the year was {hottest_day}")

#5
import random

class Coin:
    """A class representing a coin that can be tossed."""
    
    def __init__(self):
        """Initialize the coin with a default side up."""
        self.__sideup = "Heads"
    
    def toss(self):
        """Randomly set the side up to Heads or Tails."""
        if random.randint(0, 1) == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"
    
    def get_sideup(self):
        """Return the current side up."""
        return self.__sideup
    

#6
