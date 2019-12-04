   <head>
      <title>MoodBot😃</title></head>
   <body>
      <div class="container">
         <div class="widget">
            <div class="chat_header">
               <!--Add the name of the bot here -->
               <span style="color:white;margin-left: 5px;">Ordis</span>
               <span style="color:white;margin-right: 5px;float:right;margin-top: 5px;" id="close">
               <i class="material-icons">close</i>
               </span>
            </div>
            <!--Chatbot contents goes here -->
            <div class="chats" id="chats">
               <div class="clearfix"></div>
            </div>
            <!--user typing indicator -->
            <div class="keypad" >
               <input type="text" id="keypad" class="usrInput browser-default" placeholder="Type a message..." autocomplete="off">
           </div>
         </div>
         <!--bot widget -->
         <div class="profile_div" id="profile_div">
         <img class="imgProfile" src="includes/statics/img/Ordis.png"/>
         </div>
      </div>
      <!--JavaScript at end of body for optimized loading-->
      <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
      <script type="text/javascript" src="statics/js/materialize.min.js"></script>
      <!--Main Script -->
      <script type="text/javascript" src="statics/js/script.js"></script>
      <script>
      function startDictation() {

      	if (window.hasOwnProperty('webkitSpeechRecognition')) {

      	var recognition = new webkitSpeechRecognition();

      	recognition.continuous = false;
      	recognition.interimResults = false;

      	recognition.lang = "en-US";
      	recognition.start();

      	recognition.onresult = function(e) {
        	document.getElementById('keypad').value
                                 = e.results[0][0].transcript;
        	recognition.stop();
        	document.getElementById('labnol').submit();
      	};

      	recognition.onerror = function(e) {
        	recognition.stop();
      		}

    	   }
  	}

</script>
