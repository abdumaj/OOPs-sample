from loguru import logger

class User:
    def __init__(self, ip, phone_number, location):
        self.ip=ip
        self.phone_number=phone_number
        self.location=location


    def sigunup(self):
        pass

    def login(self):
        pass


user1=User("192", "1234567890", "USA") # create an instance of User class

logger.info(f"User IP: {user.ip}") # get the IP address of the user
logger.info(f"User Location: {user.location}") # get the location of the user       
logger.info(f"User Phone Number: {user.phone_number}")  

logger.info(user.__dict__)# get the attributes of the user instance
logger.info(user.__class__) # get the class of the user instance

logger.info(dir(User))


# INSTANCE OF USER CLASS

# OBJECT IS A CLOLLECTION OF DATA AND ASSOCITED BEHAVIOUR
# CLASS DESCRIBES THE OBJECT
# oBJECT ARE INSTANCE OF A CLASS


'''
INSTNACE VARIABLES IS THE VARIABLE THAT BELONGS TO THE OBJECT
WHEENVE THE OBJECT GETS CREATED, THE INSTANCE VARIABLE GETS CREATED
INSTANCE VARIABLES BELONGS TO THE OBJECT
# CLASS VARIABLES BELONGS TO THE CLASS
SELF IS A REFERNEC TO THE OBJECT  THEY CAN BE USED INTERCHANGEBLY
# CLASS VARIABLES BELONGS TO THE CLASS

'''
