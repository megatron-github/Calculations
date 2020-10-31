"""
 *****************************************************************************
   FILE:        pizzas.py

   DESCRIPTION: Estimtating amount of non-standard pizza needed

 *****************************************************************************
"""
import math

def pizza_area(diameter):
    """this function will calculate the area of the pizza"""
    area = math.pi * (diameter / 2)**2 

    return float(area)

def main():
    """ This is the function that will tell you the number pizza needed """
    standard_diameter = float(input('What is the diameter of a' + 
                                    ' "standard" size pie? '))
    standard_slices = float(input('How many slices are in a' +
                                  ' standard size pie? '))
    wanted_slices = float(input('How many standard slices do' + 
                                ' you want? '))
    wanted_diameter = float(input('What is the diameter of the' + 
                                  ' pies you will buy? '))

    standard_area = pizza_area(standard_diameter)
    wanted_area = pizza_area(wanted_diameter)
    needed_area = int(math.ceil(standard_area / standard_slices * 
                                wanted_slices / wanted_area))

    print('You will need to buy', needed_area, '' + 
          '{:01d}-inch'.format(int(wanted_diameter)), 'diameter pies.')

# this invokes the main function.  It is always included in our
# python programs
if __name__ == "__main__":
    main()
