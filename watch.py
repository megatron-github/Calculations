"""
 *****************************************************************************
   FILE:        watch.py

   DESCRIPTION:	Program that tell you what time is it when you look at the 
                  watch upside down

 *****************************************************************************
"""

def main():
    """ This is a time travelling program """
    time_read = input('What time does your upside-down watch' \
   	                  ' read (hours:minutes)? ')

    minutes = (int(time_read[time_read.find(':') + 1:]) + 30) % 60
    hour = (int(time_read[:time_read.find(':')]) - 1)
    hours = (hour + 6) % 12
    hourss = hours + 1

    print('The right-side-up time is: {:01d}:' \
          '{:02d}'.format(int(hourss), int(minutes)))

# this invokes the main function.  It is always included in our
# python programs
if __name__ == "__main__":
    main()
