import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class main{
    public static void main(String args[] ){
        


    }
}

class TimeStamp{
    int year;
    int month;
    int day;
    int hour;
    int minute;
    int second;
}

class Post{


    Boolean imageType = false;
    Boolean textType = false;
    Boolean videoType = false;

    int engagementScore;

    TimeStamp TimeStamp;


    String dateTimeStamp;
    String timeTimeStamp;

    int realDateStamp;
    int realTimeStamp;

    
  

    void getTimeStamp(){

       LocalDateTime tempTimeStamp = LocalDateTime.now();
       DateTimeFormatter DateFormatter = DateTimeFormatter.ofPattern("yyyy-MM-dd");
       DateTimeFormatter TimeFormatter = DateTimeFormatter.ofPattern("HH:mm:ss");

       String dateFormat = tempTimeStamp.format(DateFormatter);
       String timeFormat = tempTimeStamp.format(TimeFormatter);
       this.dateTimeStamp = dateFormat;
       this.timeTimeStamp = timeFormat;

    }
    void convertTimeStamp(){
        DateTimeFormatter yearformatter = DateTimeFormatter.ofPattern("yyyy");
        DateTimeFormatter monthformatter = DateTimeFormatter.ofPattern("MM");
        DateTimeFormatter dayformatter = DateTimeFormatter.ofPattern("dd");
        DateTimeFormatter hourformatter = DateTimeFormatter.ofPattern("HH");
        DateTimeFormatter minutesformatter = DateTimeFormatter.ofPattern("mm");
        DateTimeFormatter secondsformatter = DateTimeFormatter.ofPattern("ss");

        String stringTime = this.timeTimeStamp;
        String stringDate = this.dateTimeStamp;
      
        
        
    
    }


}


class User{

void seeOldPosts(){

}

void seeNewPost(){

}

void seeImagePost(){

}

void seeVideoClips(){

}

void seeTextPost(){

}
}


