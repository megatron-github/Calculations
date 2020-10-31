"""
 *****************************************************************************
   FILE:          pool.py

   DESCRIPTION:	Given the pool's length, width, desired depth of water, and 
                  the speed of the water filling up the pool, the program
                  will tell you exactly how long it takes for the pool to be
                  filled up to your desired depth of water

 *****************************************************************************
"""

def main():
    """ This is the only function """
    length = float(input("Pool length (feet): "))
    width = float(input("Pool width (feet): "))
    desired_depth = float(input('Additional depth desired (inches): '))
    depth_rate = float(input('Water fill rate (gal/min): '))

    #length = length * 12 
    #width = width * 12
    desired_depth = desired_depth * 0.0833333
    volume = length * width * desired_depth
    #volume = volume * 0.004329 #this is from cubic inch to gal
    volume = volume * 7.48052   #this is from cubic feet to gal 
    time = (volume / depth_rate) * 60
   
    hour = int(time // 3600)
    minute = int((time % 3600) // 60)
    second = round((time % 3600) % 60)

    print('Time: {:02d}:{:02d}:{:02d}'.format(hour, minute, second))

# this invokes the main function.  It is always included in our
# python programs
if __name__ == "__main__":
    main()
