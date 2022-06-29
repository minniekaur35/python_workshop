import logging
import logging.config


# ALL CAPS - Constants, First Cap - Classes. All Lower - Methods
LOG_FORMAT = "%(levelname)s - %(message)s - %(asctime)s"
# From logging, we'll call basicConfig method to change configurations for logs. for more use: print(dir(logging))
logging.basicConfig(filename = "./mylogs.log",
                        format = LOG_FORMAT,)
                        """ To overwrite messages use : filemode = 'w' """
# logger is class and to create object: call constructor or make method. 
# Since, Constructor is unavailable, we'll call method 
loga= logging.getLogger() 
# loga.setLevel(10)
loga.info("this  is diappointinng")
loga.debug("palpitating, hyperventilating, critical, monologue, epilogue and death")
loga.critical("!!!!DEATH!!!!")
loga.warning("Smoking is injurious to health")
loga.error("I am sick")

# print(dir(logging.config))
print(loga.level)
