# Str has format ##:##pm-##:##am
def counting_minutes(str):
	# Split up the input
	start_time = str.split('-')[0]
	end_time = str.split('-')[1]

	start_hour = int(start_time.split(':')[0])
	start_minutes = int(start_time.split(':')[1][0:2])

	end_hour = int(end_time.split(':')[0])
	end_minutes = int(end_time.split(':')[1][0:2])

	# Convert to military time
	if 'pm' in start_time and start_hour != 12:
		start_hour += 12

	if 'pm' in end_time and end_hour != 12:
		end_hour += 12


	# Weird corner case of midnight being 24 but time past that having hour of zero
	if 'am' in start_time and start_hour == 12:
		start_hour = 24

	if 'am' in end_time and end_hour == 12:
		end_hour = 24


	start_military = start_hour*60 + start_minutes
	end_military = end_hour*60 + end_minutes

	if start_military > end_military:
		return 1440 - (start_military - end_military) # 1440 is number of minutes in a day (1440 = 24 hours/day * 60 minutes/hour)
	else:
		return end_military - start_military
