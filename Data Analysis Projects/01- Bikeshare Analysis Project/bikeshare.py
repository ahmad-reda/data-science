'''
General:	This project works on data of a bike share system provider to uncover bike share usage patters.
			Here we compare the system usage between three US large cities: Chicago, New York City, and Washington, DC.

Arguments:	There are no arguments for this project, it interacts with the user through the command window.

Return:		It returns some statistics (refer to readme file) based on the chosen filters by the user and the selected city.
			It might give the raw data if needed by the user.
'''
import pandas as pd
import time
import random

def main():
	'''
	The main function interacts with the user first to choose the city, then filter the data based on month or day of the week or both.
	It prints the required statistics based on the user inputs.
	It asks the user to show raw data or not.
	It asks the user to restart or end the program.
	'''
	while True:
		# Welcome message
		print("\nWelcome to the data exploartion center. Let's get some insights about the US bike share system.")
		
		# Choose the city
		while True:
			# Prompt the user to input the chosen city
			city = input("\nPlease choose one of the following cities to continue: Chicago, New York City, or Washington, DC:\n")
			# Check if the input is correct
			if city.lower() == 'chicago':
				file_name = 'chicago.csv'
			elif city.lower() == 'new york city' or city.lower() == 'new york':
				file_name = 'new_york_city.csv'
			elif city.lower() == 'washington' or city.lower() == 'washington, dc' or city.lower() == 'washington dc':
				file_name = 'washington.csv'
			else:
				print("\nInvalid input! Please Check your input and try again.")
				continue
			break
		
		# Transform the file into a dataframe
		df_raw = pd.read_csv(file_name)
		# Change Start Time object to datetime
		df = df_raw.copy()
		df['Start Time'] = pd.to_datetime(df['Start Time'])
		# Explode datetime into three new columns using dt properties
		df.insert(1, 'Month', df['Start Time'].dt.month)
		df.insert(2, 'Day of Week', df['Start Time'].dt.weekday_name)
		df.insert(3, 'Hour', df['Start Time'].dt.hour)
		# Create new column for trip (start - end) just after end-station column position
		df.insert(9, 'Trip (Start - End)', df['Start Station'] + " - " + df['End Station'])
		
		# Filter the data by month if required
		while True:
			# Prompt the user to activate the month filter or not
			month_case = input("\nDo you want to filter the data by a specific month? Enter yes or no:\n")
			if month_case.lower() == 'yes':
				while True:
					# Prompt the user to enter the required month
					month = input("\nPlease enter the month name (e.g., January or jan):\n")
					# Filter the data using the function or return 0 if the input is invalid
					month, df_filtered  = filter_month(df, month)
					if month:
						df = df_filtered
						break
					else:
						print("\nInvalid input! Please Check your input and try again.\nPlease note that: The data is available only for the first six months.")
				break
			elif month_case.lower() == 'no':
				month = 0 # represent no month filter
				break
			else:
				print("\nInvalid input! Please Check your input and try again.")
			
		# Filter the data by day of week if required
		while True:
			# Prompt the user to activate the day filter or not
			day_case = input("\nDo you want to filter the data by a specific day of week? Enter yes or no:\n")
			if day_case.lower() == 'yes':
				while True:
					# Prompt the user to enter the required day
					day = input("\nPlease enter the day name (e.g., Sunday or sun):\n")
					# Filter the data using the function or return 0 if the input is invalid
					day, df_filtered  = filter_day(df, day)
					if day:
						df = df_filtered
						break
					else:
						print("\nInvalid input! Please Check your input and try again.")
				break
			elif day_case.lower() == 'no':
				day = 0 # represent no day filter
				break
			else:
				print("\nInvalid input! Please Check your input and try again.")
		
		# Start timer
		start = time.time()
		
		# Print a table to view the insights

		# Select month statment if exists
		if month == 0:
			month_sentence = ''
		else:
			month_sentence = " in " + month.title()
		# Select day statment if exists
		if day == 0:
			day_sentence = ''
		else:
			day_sentence = " of " + day.title() + "s only"
		# Print table title
		print("\nThe following table gives some insights about bike share system in {}{}{}:\n".format(city.title(), month_sentence, day_sentence))
		
		# Specify width of left table cell
		global CELL_WIDTH
		CELL_WIDTH = "35s"
		
		# Print table header
		print(format("Statistic", CELL_WIDTH), "|", "Value")
		
		#Print separator
		print("-"*90)
		
		# Print most common month, day of week, hour, start station, end station, and trip in the stated order
		order = [1, 2, 3, 7, 8, 9]
		for i in order:
			# Don't print month statistic if month filter is active
			if i == 1 and month != 0:
				continue
			
			# Don't print day statistic if day filter is active
			if i == 2 and day != 0:
				continue
			most_common(df, i)
			
		# Print total travel time and average
		i = 6 # Trip duration column position
		travel_time(df, i)
		
		# Determine number of columns of the dataframe
		number_columns = df.shape[1]
		
		# Print user details in the stated order
		order = [10, 11, 12]
		for i in order:
			# Check if the extra data exists (gender and birth day)
			if i < number_columns and i != 12:	# User types and gender
				users(df, i)
			elif i < number_columns: # Birth year
				birth_year(df, i)
				most_common(df, i)
		
		# Print separator
		print("-"*90)
		
		# Print time
		print("Time elapsed: {0:0.2f} seconds".format(time.time() - start))
		
		# Ask to show raw data
		while True:
			# Ask the user to show 5 random trips or not
			raw = input("\nDo you want to investigate the raw data of {}? Enter yes or no:\n".format(city.title()))
			if raw.lower() == 'yes':
				print("\nHere are the raw data of five random trips:")
				for i in range(5):
					# Generate random number as an index
					rand_index = random.randint(0, len(df_raw) - 1)
					dictionary = dict(df_raw.iloc[rand_index,:])
					print()
					# Print each item in a new line
					for key, value in dictionary.items():
						print(format(str(key) + ": ", "15s") + str(value))
			elif raw.lower() == 'no':
				break
			else:
				print("\nInvalid input! Please Check your input and try again.")
		
		# Ask to restart
		restart = input("\nWe have reached the end! Enter yes to restart or enter any other value to terminate:\n" )
		if restart.lower() == 'yes':
			continue
		else:
			print("\nGoodbye!")
			break

# Filter data by month
def filter_month(df, month):
	'''
	This function checks if the input is valid and filters the data according to the selected month
	The input is valid by either entering the full name of the month or the appreviated name without dot (Not case-sensitive)
	Args: df is a dataframe, month is a string
	Outputs: returns 0 and {} if the input is invalid or returns the month name and the filtered dataframe is the input was valid
	'''
	month = month.title()
	months = ['January', 'February', 'March', 'April', 'May', 'June']
	months_abbreviated = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
	if month in months:
		month = months.index(month) + 1
	elif month in months_abbreviated:
		month = months_abbreviated.index(month) + 1
	else:
		return 0, {}
	return months[month - 1], df[df['Month']==month]

# Filter data by day
def	filter_day(df, day):
	'''
	This function checks if the input is valid and filters the data according to the selected day
	The input is valid by either entering the full name of the day or the appreviated name without dot (Not case-sensitive)
	Args: df is a dataframe, day is a string
	Outputs: returns 0 and {} if the input is invalid or returns the month name and the filtered dataframe is the input was valid
	'''
	day = day.title()
	days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
	days_abbreviated = ['Sat', 'Sun', 'Mon', 'Tues', 'Wed', 'Thurs', 'Fri']
	if day in days:
		pass
	elif day in days_abbreviated:
		day = days_abbreviated.index(day)
		day = days[day]
	else:
		return 0, {}
	return day, df[df['Day of Week']==day]
		
# General function for any "Most common"
def most_common(df, i):
	'''
	This function prints the most common statistic (mode) for any label.
	Args: df is a dataframe, i is an integer that represents the position of the required label.
	Outputs: prints a new row in the table by showing the mode or modes (for multimodal statistic) along with the relative frequency (percentage).
	'''
	popular = df.iloc[:,i].mode()
	frequency = df[df.iloc[:,i] == popular[0]].iloc[:,i].count()
	count = df.iloc[:,i].count()
	# Print all mode(s) as it might by bimodal or multimodal
	for j in range(len(popular)):
		sentence = "Most common " + list(df.columns)[i].lower()
		# Add custom settings for birth year
		if i == 12:
			additional_sentence = " of users"
			value = str(int(popular[j]))
		else:
			additional_sentence = ''
			value = str(popular[j])
		# Add mode index for multimodal statistic
		if j != 0:
			mulit_modal_sentence = ' ' + str(j + 1)
		else:
			mulit_modal_sentence = ''
		print(format(sentence + additional_sentence + mulit_modal_sentence, CELL_WIDTH) + " | " + value + " (" + format(frequency/count, ".1%") + ")")

# Calculate total and average travel time
def travel_time(df, i):
	'''
	This function prints the statistics about the travel time.
	Args: df is a dataframe, i is an integer that represents the position of the required label.
	Outputs: prints a new row in the table by showing the sum of the travel time in seconds (and hours, minutes and, remaining seconds))
	and the average time is printed in a new row.
	'''
	total_time = df.iloc[:,i].sum()
	remaining_seconds = total_time % 60
	total_minutes = total_time // 60
	remaining_minutes = total_minutes % 60
	total_hours = total_minutes // 60
	sentence = "({0:0.0f} hours, {1:0.0f} minutes, and {2:0.0f} seconds)".format(total_hours, remaining_minutes, remaining_seconds)
	avg_time = df.iloc[:,i].mean()
	print(format("Total travel time", CELL_WIDTH) + " | " + format(total_time, "0.0f") + " seconds " +  sentence)
	print(format("Average travel time", CELL_WIDTH) + " | " + format(avg_time, "0.1f") + " seconds")

# Calculate number of users
def users(df, i):
	'''
	This function prints the statistics about the users.
	Args: df is a dataframe, i is an integer that represents the position of the required label.
	Outputs: prints the user types (each type in a separate row) along with the relative frequency (percentage).
	It also prints the user gener (each one in a separate row) along with the relative frequency (percentage).
	'''
	users_types = df.iloc[:,i].value_counts()
	count = df.iloc[:,i].count()
	for j in range(len(users_types)):
		frequency = users_types[j]
		print(format(list(users_types.keys())[j] + " users", CELL_WIDTH) + " | " + str(frequency) + " (" + format(frequency/count, ".1%") + ")")

# Determine the year of oldest and youngest users
def birth_year(df, i):
	'''
	This function prints the statistics about the birth year.
	Args: df is a dataframe, i is an integer that represents the position of the required label.
	Outputs: prints birth years of the eldest and the youngest each in a separate row.
	'''
	oldest = df.iloc[:,i].min()
	print(format("Birth year of eldest user", CELL_WIDTH) + " | " + format(oldest, ".0f"))
	youngest = df.iloc[:,i].max()
	print(format("Birth year of youngest user", CELL_WIDTH) + " | " + format(youngest, ".0f"))

main()