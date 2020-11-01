"""
 *****************************************************************************
   FILE:        pizzas.py

   DESCRIPTION: You want to buy a pizza with a desired n-inch diameter and 
                a desired amount of slices. This program will tell you how 
                many n-inch diameter pizza do you need given the standard 
                pizza's diameter and amoun of slices.
                
                Here is a sample interaction with the program: 
                What is the diameter of a "standard" size pie? 16
                How many slices are in a standard size pie? 8
                How many standard slices do you want? 14
                What is the diameter of the pies you will buy? 4
                You will need to buy 28 4-inch diameter pies.

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
