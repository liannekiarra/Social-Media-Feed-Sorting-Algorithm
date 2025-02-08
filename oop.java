
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class sortFeed{
    public static void main(String args[]){
        LocalDateTime now = LocalDateTime.now();
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
        String formattedNow = now.format(formatter);
        System.out.println("Current TimeStamp: "+ formattedNow);

        
    }

}


class User{

    int sessionTimeStamp ; //this is time current time of the session


    //generates feed prioritising new posts
    void seeNewPosts(){

    }
    //generates feed prioritising older feed
    void seeOldPost(){

    }
    //generates feed prioritising image posts
    void seeImagePost(){

    }
    //generate feed prioritising video clips post
    void seeVideoPost(){

    }
    //generate feed prioritising text post
    void seeTextPost(){

    }



}


class Post{

    
    Boolean typeText = false;
    Boolean typeVideoClip = false;
    Boolean typeImage = false;

    LocalDateTime now = LocalDateTime.now();






    
}

