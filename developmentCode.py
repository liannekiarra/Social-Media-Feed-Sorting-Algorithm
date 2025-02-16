import random
import datetime
from datetime import datetime


class User:
    name = ''
    contentTypePreference = None
    #default friends list - superset of close friends
    friends = ['Stacy','Erica','Jessica', 'Henry', 'Caleb','Michael', 'Chase', 'Carl', 'Finn', 'Calvin']
    #default close friends group - subset of friends list
    closeFriends = ['Finn','Chase','Henry','Calvin']
    
    
    def __init__(self, name: str, contentTypePreference: int):
        self.name = name
        self.contentTypePreference = contentTypePreference
        return
    
""" Date Generator is class that contains a function that sets a time stamp for a post object because the built in dateitme 
functionality of Python3 is extremely fast that building over 100 post objects happens within one second. Therefore to showcase 
the sorting algorithm's functionality, the Time Stamp of a single post should be generated in such a way that it would simulate the creation
of the posts in different ranges of time, more significant difference within one second. """

class DateGenerator:
    
    def generateDateTime(self):
        possibleMonths = list(range(1,13))
        possibleDays = list(range(1,29))
        possibleHours = list(range(0,24))
        possibleMinutes = list(range(0,60))
        possibleSeconds = list(range(0,60))
        month = random.choice(possibleMonths)
        day    = random.choice(possibleDays)
        hour = random.choice(possibleHours)
        minute = random.choice(possibleMinutes)
        second = random.choice(possibleSeconds)
        x = datetime(2025, month, day, hour,minute, second)
        return x #randomised datetime value for a post object


class Post:
    
    owner = None
    contentType = None
    engagementScore = None
    timeStamp = None
    falsetimestamp = None
    currentUser = None
    combinedDetails = None
    datetimeGenerator = None
    
    
    def __init__(self, currentUser: User, dateGenerator: DateGenerator):
        self.currentUser = currentUser
        self.datetimeGenerator = dateGenerator
        
    #getting the time stamp
    def getTimeStamp(self):
        self.timeStamp = datetime.now()
        return self.timeStamp
    
    def getFalseDateTime(self):
        self.falsetimestamp = self.datetimeGenerator.generateDateTime()
        return
    
    #randomised owner from friend's list
    def getOwner(self):
        #get friends list from user object
        friendsList = self.currentUser.friends
        #setting random owner of a post object
        self.owner = random.choice(friendsList)
        
        return self.owner
    
    #randomised content type of the post
    def getContentType(self):
        types = ["Image Post", "Video Clip Post", "Text Post"]
        self.contentType = random.choice(types)
        return self.contentType
    
    #randomised engagement score for the post
    def getEngagementScore(self):
        engagementScore = [1,2,3,4,5,6,7,8,9,10]
        self.engagementScore = random.choice(engagementScore)
        return self.engagementScore
    
    #this  function displays the information of a post object
    def getPostInformation(self):
        owner = self.owner
        timestamp = self.timeStamp
        contentType = self.contentType
        engagementScore = self.engagementScore
        print(owner, "shared one",contentType," on: ", timestamp, "(Engagement Score:",engagementScore,")")
        print("____________________________________________________________________________________________")
        return 
    #this function displays false varying time stamps
    def getPostInformationVaryTimeStamp(self):
        owner = self.owner
        falseTimeStamp = self.falsetimestamp
        contentType = self.contentType
        engagementScore = self.engagementScore
        print(owner, "shared one",contentType," on: ", falseTimeStamp, "(Engagement Score:",engagementScore,")")
        print("____________________________________________________________________________________________")
        return 
        
    #this builds posts with varying timestamp    
    def buildPost(self):
        #calling all fundamental functions to build a post and it's attributes
        self.getOwner()
        self.getFalseDateTime()
        self.getContentType()
        self.getEngagementScore()
        return 
    
    def buildPostTrueTimeStamp(self):
        #calling all fundamental functions to build a post and it's attributes
        self.getOwner()
        self.getTimeStamp()
        self.getContentType()
        self.getEngagementScore()
        return
        
      
        
class System:
    
    defaulNumberOfPost = None
    currentUser = None
    friendDatabase = None
    dateGenerator = None

    def __init__(self, newUser: User, dateGenerator: DateGenerator):
        self.currentUser = newUser
        self.dateGenerator = dateGenerator
        
        return
        
    def setDefaultPostsNumber(self, numberOfPost: int):
        self.defaulNumberOfPost = numberOfPost
        
        return
        
    #setting friend database
    def getFriendList(self):
        friendList = self.currentUser.friends
        closeFriends = self.currentUser.closeFriends
        
        return closeFriends, friendList
    
    def setFriendData(self):
        self.friendDatabase = self.getFriendList()
        return
        
    def generateDefaultFeed(self):
    
        
        #builds post objects
        #this generates a default feed that is not sorted based on user preference and friend partitioning
        #not using sorting algorithm
        numberOfPost = self.defaulNumberOfPost
        
        #generating default feed for current session
        defaultFeed = []
        
        #building all post objects and storing them in defaultFeed list
        x = 0
        while x < numberOfPost:
            newPost = Post(self.currentUser,self.dateGenerator)
            newPost.buildPost()
            defaultFeed.append(newPost)
            x = x+1
            
        return defaultFeed
    
    def showDefaultFeed(self):
        listOfPosts = []
        
        return
        
class SortingAlgorithm:
    defaultFeed = None
    
    def __init__(self, defaultFeedBySystem: list):
        self.defaultFeed = defaultFeedBySystem
        return
    #sorts posts by timestamp
    def sortTimeStamp():
        return
    #sorts posts by content type
    def sortContentType():
        return
    #sorts post by engagement score
    def sortEngagementScore():
        return
    #sort post by friend classification
    def sortCloserFriends():
        return
    #sort post by default friend
    def sortFriends():
        return
    
def swapElement(allObjects:list, x:int,y:int):
    allObjects[x],allObjects[y]= allObjects[y], allObjects[x]
    return


def partition(allObjects:list, low:int, high:int):
    timestamps = []
    for i in allObjects:
        temptime = i.falsetimestamp
        timestamps.append(temptime)
        
    pivotValue = timestamps[high]
    i = low-1
    for j in range(low, high):
        if timestamps[j]<pivotValue:
            i += 1
            swapElement(allObjects, i, j)
    swapElement(allObjects, i+1, high)
    return i+1

def engagementScorePartition(allObjects:list, low:int,high:int):
    engagementScores = []
    for i in allObjects:
        tempScore = i.engagementScore
        engagementScores.append(tempScore)
    pivotValue = engagementScores[high]
    i = low-1
    for j in range(low, high):
        if engagementScores[j]<pivotValue:
            i += 1
            swapElement(allObjects, i, j)
    swapElement(allObjects, i+1, high)
    return i+1

def quickSort(allObjects:list, x:int, y:int):
    if x<y:
        partitionReturn = partition(allObjects, x, y)
        quickSort(allObjects, x, partitionReturn-1)
        quickSort(allObjects, partitionReturn+1 , y)
    
class QuickSortAlgorithm:
    
    listOfPosts = None 
    
    def __init__(self, listOfPosts:list):
        self.listOfPosts = listOfPosts
        return
    
    #function to swap elements
    def swapElement(self,listOfPost, firstValue, secondValue):
        listOfPost[firstValue], listOfPost[secondValue] = listOfPost[secondValue],listOfPost[firstValue]
        
        return
    
    def partition(self,listOfPosts,lowerValue, higherValue):
        timestamps = []
        for i in listOfPosts:
            temptime = i.falsetimestamp
            timestamps.append(temptime)
        
        pivot = timestamps[higherValue]#setting pivot
        
        i = lowerValue-1#setting index
        for j in range(lowerValue, higherValue):
            if timestamps[j]<pivot:#comparing element to pivot
                i += 1
                self.swapElement(listOfPosts,i,j)#swap elements after comparing with pivot
        self.swapElement(listOfPosts, i+1,j)
        return  i+1
    
    def quickSort(self,listOfPosts,lowerValue, higherValue):
        if lowerValue<higherValue:
            partition = self.partition(listOfPosts, lowerValue, higherValue)
            
            #recurssion calls for smaller elements
            self.quickSort(listOfPosts, lowerValue, partition-1)
            self.quickSort(listOfPosts, partition+1, higherValue)
        return 
    
    def sortObjects(self):
        return
    
class UserInterface:
    name = None
    contentType = None
    
    #asks for content type from user from the user interface 
    def getParameters(self):
        name = input('Enter your name: ')
        print("--------------- Welcome " ,name, "! ----------------------------")
        self.name = name
        print("Select a content type preference below: ")
        print("") 
        print(" [1] - Image Posts") 
        print(" [2] - Texts Posts") 
        print(" [3] - Video Clip Posts") 
        print(" ")
        print("----------------------------------------------------------------")
        contentPreference = int(input('Enter content preference (1/2/3): '))
        print("----------------------------------------------------------------")
        self.contentType = contentPreference
        
    def showingFeed():
        return



#RUNNING SPECIFIC FUNCTIONS TO SIMULATE THE SOCIAL MEDIA FEED
class Controller:
    
    #automating build of Social Media Feed by New User and their Preference
    #calling fundamental sequence to return list of Post Objects in a feed
    def originalFeed(self, numberOfPost: int):
        newInterface = UserInterface()
        newInterface.getParameters()
        currentUsername = newInterface.name
        userPreference = newInterface.contentType
        newUser = User(currentUsername, userPreference)
        newSystem = System(newUser)
        n = numberOfPost
        newSystem.setDefaultPostsNumber(n)
        sessionFeed = newSystem.generateDefaultFeed()
        

        return sessionFeed #get seesion feed
    
    
    

    def firstController(self):
        # Get Parameters from user
        
        # builds new user interface 
        newInterface = UserInterface()
        #calling getParameters for user input
        newInterface.getParameters()
        #all parameters are now retrieved to generate a feed.
        
        #create a new user
        currentUsername = newInterface.name
        userPreference = newInterface.contentType
        newUser = User(currentUsername, userPreference) #user object
        
        newSystem = System(newUser)
        newSystem.setDefaultPostsNumber(10)
        #use newSystem to generate default radomised feed
        sessionFeed = newSystem.generateDefaultFeed() #sessionFeed is the list of all post objects
        #printing unsorted feed
        for i in sessionFeed:
            i.getPostInformation()
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print("----------------------------------------------------------------------------- ")
            

    def secondController(self):
        #get parameters
        newInterface = UserInterface()
        newInterface.getParameters()
        #parameters
        currentUsername = newInterface.name
        userPreference = newInterface.contentType
        #building new user object using parameters
        newUser = User(currentUsername, userPreference)
        #build date generator
        dateGenerator = DateGenerator()
        
        #build the system object
        #building new system using new user object
        newSystem = System(newUser,dateGenerator)
        newSystem.setDefaultPostsNumber(10)
        #use newSystem to generate default radomised feed
        sessionFeed = newSystem.generateDefaultFeed() #sessionFeed is the list of all post objects
        #printing unsorted feed
        for i in sessionFeed:
            i.getPostInformationVaryTimeStamp()
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print("---------------------------------------------------------------------------------------------------------------")
        
    
        lengthOfFeed = len(sessionFeed)
        sortTimeStamp = QuickSortAlgorithm(sessionFeed)
        sortTimeStamp.quickSort(sessionFeed,0,lengthOfFeed-1)
        
        for i in sessionFeed:
            i.getPostInformationVaryTimeStamp()
            
        print(" ")
        print(" ")
        print("------------------------------ Running tests on the posts objects in sorted list--------------------")
        print(" ")
        print(" ")
        for i in sessionFeed:
            temptime = i.falsetimestamp
            print(temptime)
        return sessionFeed
            

class TestingAlgorithm:
    #this function prints out the timestampst to display their sequence 
    def checkAlgorithm(self,listOfObjects):
        #printing before algorithm
        print("---------Before Algorithm-----------")
        for i in listOfObjects:
            print (i.falsetimestamp)
        print("---------Using Algorithm-------------")
        #using algorithm
        length = len(listOfObjects)
        sortingAlgorithm = QuickSortAlgorithm(listOfObjects)
        sortingAlgorithm.quickSort(listOfObjects, 0 ,length-1)
        
        for i in listOfObjects:
            print(i.falsetimestamp)

        return

class ErrorHandling:
    
    
    def checkName(userName: str):
        return
    
    
    def checkUserPreference(selectionNumber: int):
        return

    
    def __init__(self):
        return


class SortUserPreference:
    #Steps of sorting against user preferences
    #List is already sorted by timestamp (ascending order)
    # 1.) Gather all Posts that are made by close friends
    # 2.) Close Friends get priority regardless of timestamp
    # 3.) Content Type gets second priority regardless of timestamp
    # 4.)(CONCLUSION) Preferable content type by close friends gets ultimate priority regardless of timestamp
    user = None
    contentTypePreference = None
    allPostObjects = None
    listOfCloseFriends = None
    postsByCloseFriends = None
    
    def __init__ (self,userName: User, listOfPostObjects: list):
        self.user = userName
        self.allPostObjects = listOfPostObjects

        return
    
    def setCloseFriends(self):
        self.listOfCloseFriends = self.user.closeFriends
        
    def setUserContentTypePrefernece(self):
        self.contentType = self.user.contentTypePreference
        
    def sortEnagagementScore(self, listOfObjects: list):
        allPost = listOfObjects
        sorted = []
        for i in allPost:
            print(
        
            )
        return
       
        
    
    def findPostsByCloseFriends(self):
        closeFriends = self.listOfCloseFriends
        postObjects = self.allPostObjects
        postsByCloseFriends = []
        for i in postObjects:
            if i.owner in closeFriends:
                postsByCloseFriends.append(i)
        self.postsByCloseFriends = postsByCloseFriends
        
    def getMostPreferable(self):
        #post by close friend that is of content type preference and the most recent
        posts = self.postsByCloseFriends
        preference = self.contentTypePreference
        goodContent =[]
        
        #checking for posts the user prefers from close friends
        for i in posts:
            if i.contentType == preference:
                goodContent.append(i)
        
        #engagement score sort
        
        return
        
        

    def findCloseFriends(postObject):
        return
    
    def automateUserPreference(self):
        return #list of post objects sorted against user preference - Close Friends and Content Type
    

     
def main1():#function to test sorting of the objects by their timestamp attribute
    newController = Controller()
    exampleList = newController.secondController()
    y = len(exampleList)-1

    quickSort(exampleList,0,y)
    
    #loop to display object lsit
    for i in exampleList:
        i.getPostInformationVaryTimeStamp()
        
        
    return exampleList#sorted list 



#POSTS THAT ALIGN WITH USER PREFERENCE IS PRIORITISED REGARDLESS IF THEY HAVE OLDER TIMESTAMPS AND IF THEY HAVE LOW
#ENGAGEMENT SCORE
# This concludes, posts that are made by close friends and are the user's content preference choice, it will be prioritised
#first
def monday(listOfObjects:list):#attempting to build an algorithm that sorts the obejects by their content type
    example = listOfObjects
    for i in example:
        print(i.currentUser.closeFriends)

    return


#----------------------------------------------- TESTING REGION -----------------------------------------
main1()
