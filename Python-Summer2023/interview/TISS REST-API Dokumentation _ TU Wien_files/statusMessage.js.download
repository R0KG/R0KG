/**
  * Status message script
  * 
  * This script improves the visibility of status messages, i.e., of error or success 
  * messages displayed to the user. 
  * 
  * Technically, the script adds a listener for when a new status message is added into 
  * the browser's DOM. If the message is not visible because the user scrolled too far 
  * down, the script displays the message in a fixed position at the top of the browser 
  * window.
  *  
  * NOTE: 
  * In the future it is recommended to use the "DOM Level 4 mutation observer" interface,
  * once modern browsers provide support for it.
  */

(function($) {
	
	var messagesPositionFixed = false;
	var messageCounter = 0;
	var standardMessageTimeout = 5000;
	var messageTimeout = 5000;
	var animationTime = 300;
	var messageTimer;
	var averageWordSize=11;
	var wordsPerSecond=2
	var messagePanelOffset;
	var messagePanelHeight;
	var messagePanelTop;
	var scrollYThreshold;
	var jquery_helper;
	
	var removeFixedMessage = function(id) {
		
		// if element with class gmp exists
		if ( !($(".gmp" + id).length)) {
			return;
		}
		
		if( messagesPositionFixed === true) {
			$(".gmp" + id).animate({
    			  top: '-' + messagePanelTop
  
					}, animationTime,'linear', function() {
 					 $(".gmp" + id).remove();
				});
		
		messagesPositionFixed = false;
		clearTimeout(messageTimer);
		
		
		
		}
	};
	
	var toggleFixedMessage = function() {
		var mid = messageCounter;
		if( messagesPositionFixed === true) {
			
			
			$(".fixedMessagePanel").animate({
	      			  top: '-' + messagePanelTop
	    
	  					}, animationTime,'linear', function() {
	   					 $(".fixedMessagePanel").remove();
	  				});
			
			messagesPositionFixed = false;
			
			
	  		

		} else {
					
			jquery_helper=$("<ul class='fixedMessagePanel'></ul>").addClass("gmp" + mid).css("top","-" + messagePanelTop + "px").append($("#globalMessagesPanel li:not(.statusShown)").clone());
			$("#globalMessagesPanel li:not(.statusShow)").addClass("statusShown");
			jquery_helper.appendTo("body");
					
			
			
			$(".fixedMessagePanel").animate({
     			 top: '0px'
   
 					}, animationTime,'linear', function() {
  						 // Animation complete.
 				});
			messageTimer = setTimeout(function() { removeFixedMessage(mid);
				},messageTimeout);
			messagesPositionFixed = true;
		}
	};
	
	var isAboveScrollThreshold = function() {
		currentScrollY = $(window).scrollTop();
		if( currentScrollY < scrollYThreshold) {
			return false;
		} else {
			return true;
		}
	};
	
	var onScrollYChange = function() {
		if( messagesPositionFixed === true) {
			if( isAboveScrollThreshold() === false ) {
				toggleFixedMessage();
				$(window).unbind('scroll');
			}
		} else {
			$(window).unbind('scroll');
		}
		
	};
	
	var createFixedMessage = function() {
		
		messagePanelOffset = $("#globalMessagesPanel").offset();
		messagePanelHeight = $("#globalMessagesPanel").outerHeight(true);
		messagePanelTop = messagePanelHeight;

		//calculate scrollThreshold
		scrollYThreshold = messagePanelOffset.top + messagePanelHeight;


		if( isAboveScrollThreshold() === true) {
			if( messagesPositionFixed === true) {
				removeFixedMessage(messageCounter-1);
			
				
			}
			//get length of all status messages
			var textLength = $("#globalMessagesPanel").text().length;
			// time = textlength / average word size / average reading speed * 1000 milliseconds
			var time = textLength/averageWordSize/wordsPerSecond*1000;
			messageTimeout = ( standardMessageTimeout > time ) ? standardMessageTimeout : time;
			

			toggleFixedMessage();
			messageCounter=messageCounter+1;
			
			
			
			
			$(window).bind('scroll',onScrollYChange);
		} else {
			$("#globalMessagesPanel li:not(.statusShown)").addClass("statusShown");
		}
	};
	
	var newGlobalMessage = function(event)  {
		
			

			// is there an unregistered status message element
			if(  $("#globalMessagesPanel li:not(.statusRegistered)").length !== 0 ) {
				$("#globalMessagesPanel li:not(.statusRegistered)").addClass("statusRegistered");
				createFixedMessage();
			}
		
		
	};
	

	
	
	var newMessagesAvailable = function() {
		
		
		newGlobalMessage();
		
		setTimeout(newMessagesAvailable,1000);
		
	};
	
	var init = function() {
		   
				
				
				messagePanelOffset = $("#globalMessagesPanel").offset();
				messagePanelHeight = $("#globalMessagesPanel").outerHeight(true);
				messagePanelTop = messagePanelHeight;
				
				scrollYThreshold = messagePanelOffset.top + messagePanelHeight;
				newMessagesAvailable();
					
			
	};
	
	$(document).ready(init);
	
	
})(jQuery);
