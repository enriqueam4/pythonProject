import os, logging, time
logger = logging.getLogger(__name__)
class Cowboy:
    def __init__(self):
        logger.debug('Here we go')
        self.yeehaw()
        time.sleep(3)
        logger.debug('Loaded')
        
    def yeehaw(self,*args):
        print("""

     ____________________________
    /                           /\ 
   /   Hey, Jiamin            _/ /\ 
  /    How's it going?       / \/
 /                           /\     
/___________________________/ /     
\___________________________\/ 
 \ \ \ \ \ \ \ \ \ \ \ \ \ \ \
 """)
        return 'Here\'s ya server'  
