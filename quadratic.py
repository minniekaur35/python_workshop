import logging
import math

# Create and configure logger
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename = "./quadfails.logs", 
                    level = logging.DEBUG,
                    format = LOG_FORMAT)

logger_class = logging.getLogger()

def quad_formula(a, b , c):
    """ Return the solutions to the equation ax**2 + bx + c = 0"""
    logger_class.info("quad_formula({0}, {1}, {2})".format(a, b, c))

    # compute the discriminant
    logger_class.debug("# Compute the discriminant")
    disc = b**2 - 4*a*c

    # compute the two roots
    logger_class.debug("# Compute the two roots")
    root1 = (-b + math.sqrt(disc)) / (2*a)
    root2 = (-b - math.sqrt(disc)) / (2*a)

    # Return the roots
    logger_class.debug("# Return the roots")
    return (root1, root2)

roots = quad_formula(1, 0, -4)
print(roots)