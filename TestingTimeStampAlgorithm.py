
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
        self.swapElement(listOfPosts, i,j)
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

class Controller:
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
    
    def checkAlgorithm(self,listOfObjects):
        #printing before algorithm
        print("---------Before Algorithm-----------")
        for i in listOfObjects:
            print (i.falsetimestamp)
        print("-----------------------------------")
        #using algorithm
        length = len(listOfObjects)
        sortingAlgorithm = QuickSortAlgorithm(listOfObjects)
        sortingAlgorithm.quickSort(listOfObjects, 0 ,length-1)
        
        for i in listOfObjects:
            print(i.falsetimestamp)

        return

        
        

newController = Controller()
exampleList = newController.secondController()
new = TestingAlgorithm()
new.checkAlgorithm(exampleList)




    
    
