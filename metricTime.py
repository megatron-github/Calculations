"""
 *****************************************************************************
   FILE:        metricTime.py

   DESCRIPTION:	Build a program that convert military time to "metric" time

 *****************************************************************************
"""

def main():
    """ This program talks to Martian """
    
    military_time = input('Enter the time of day in military time' \
    					  ' (HH:MM:SS): ')
    location = military_time.find(':')
    
    hour = int(military_time[:location]) * 3600
    the_rest_of_time = military_time[location + 1:]
    minute = int(the_rest_of_time[:location]) * 60
    second = int(the_rest_of_time[location + 1:]) + hour + minute

    martian_second = second * (100000/86400)

    metric_second = ((martian_second % 1000) % 100)
    metric_minute = int(martian_second % 1000) // 100
    metric_hour = int(martian_second // 1000)

    #Source for learning how to create a float with leading zeros
    #Source: Print leading zeros of a floating point number
    #Cite: https://stackoverflow.com/questions/
    #39482902/print-leading-zeros-of-a-floating-point-number/39482977
    print('The "metric" time is:\n{:02d}:{:01d}:' \
    	  '{:05.2f}'.format(metric_hour, metric_minute, metric_second))

# this invokes the main function.  It is always included in our
# python programs
if __name__ == "__main__":
    main()
