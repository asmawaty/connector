import os
import sys

#Constant for verify connection
FTRACK_CONNECTED = False

sys.path +=['C:/server/apps/3rdparty/ftrack-python']
#used address/url from  ftrack account  - administrator 
os.environ['FTRACK_SERVER'] ='https://cas.ftrackapp.com'
#get from personal API key (check your ftrack account - they will give you this number) - administrator 
#os.environ['FTRACK_APIKEY'] ='fcad98ce-3444-11e5-ac0b-42010af0f731' 

import ftrack
FTRACK_CONNECTED =True

class Connector (object):
    """info about Connector"""
    def __init__(self,user=None):
        super (Connector, self).__init__()

#set the user to None each time connected/ refresh user
        self.user =user
        self.userDetails = None
        selft.userTasks = None

        if not self.user:
            self.user=os.environ['USERNAME']

    def getUser(self):
        return self.user
        
    def setUser(self):
        self.user = value  #we can asign the user for any task

    def connect(self):
        os.environ['LOGNAME']=self.user
        if FTRACK_CONNECTED is True:
            print 'Connection Successful'

    def getUserDetails (self):
        self.userDetails = ftrack.getUser(self.user)
        return self.userDetails

    def getUserTasks (self):
        userDetails =self.userDetails()
        self.userTasks = userDetails.getTasks()
        return self.userTasks
