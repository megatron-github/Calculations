"""
 *****************************************************************************
   FILE:        watch.py

   AUTHOR:		Truong Pham

   ASSIGNMENT:	Project 2: Part 3: Watch

   DATE:		9/5/18

   DESCRIPTION:	Program that tell real time when watch is upside down

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
