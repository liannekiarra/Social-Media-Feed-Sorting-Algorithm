#file to show selecting random for building post 

import random
import datetime 


class User:
    recency = None
    contenType = None
    preference = [None,None]
    #random owner of posts
    friends = ['John','Andy','Joe','Johnson','Smith','Williams','Kai','Kate','Harry','Daniel','Dimitri', 'Luan', 'Liam','Kevin']
    
    def __init__(self, recency: int, contentType: int ):
        return

class posts:
    
    owner = None
    
    def getRandomOwner(self,userFriends:list):
        self.owner = random.choice(userFriends)
        return self.owner
 
    

def UserInterface():
    print("--------------- Welcome to Social Media Feed ---------------")
    print(" ")
    print("Select an option of recency preference below: ")
    print(" [1] - Show Newest Post")
    print(" [2] - Show Older Posts")
    recency = int(input("Select preference (1/2): "))
    print("Select an option of content type preference below: ")
    print(" [1] - Image Posts")
    print(" [2] - Video Clips Posts ")
    print(" [3] - Texts Posts")
    contentType = int(input("Enter your preference of content type (1/2/3): "))
    choice = [recency,contentType]
    return choice

def main():
    choice = UserInterface()
    recency = choice[0]
    contentType = choice[1]
    userexample = User(recency, contentType)
    example = posts()
    name = example.getRandomOwner(userexample.friends)
    print(name)
    
    
main()
    

    
