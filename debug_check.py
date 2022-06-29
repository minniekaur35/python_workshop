import logging 
import math

# format the log
FORMAT_THIS_LOG = "%(levelname)s -- %(asctime)s --  %(message)s -- %(pathname)s"    
logging.basicConfig(filename = "./mylogs.log", level = logging.DEBUG, format = FORMAT_THIS_LOG, filemode = 'w')
logger = logging.getLogger()


""" Surface area of cylinder = 2*pi*r*h + 2*pi*r**2 """
def surface_area(r, h):
    try:
        # Work on something
        lateral_surface =  pi * float(2 * r * h )
        two_circle_area =  pi * float( 2 * r**2 )
        logger.info("surface_area for radius {0} and height {1} was computed succesfully".format(r, h))
    except:
        logger.error("Surface_area issues: input value is missing -- the code failed !")
    return lateral_surface + two_circle_area


def safe_int(value):
    if value: # if it is defined or not empty(spaces are not considered empty here) or value != 0 or value != False
        try:
            output = int(value)
            logger.info("Converted to integer - " + value)
        except:
            logger.error("Conversion to integer failed for -  "+ value + " returned default value 0")
            output = 0
    else:
        logger.warning("Returned default value for safe execution - " + value)
        output = 0
    return output


pi = 3.14
r = safe_int(input("Please enter the value of the radius of the cylinder : "))
h = safe_int(input("Please enter the value of the height of the cylinder: "))

print(surface_area(r, h))
