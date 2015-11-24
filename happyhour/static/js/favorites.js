// get csrf token for post method
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Upon click of favorite button, adds restaurant to user's list of favorites.
function addUserFavorite(markerId, user, restaurant){
	url = "/v1/favorites/user/" + user + "/"; 
	data = {'user': user, 'restaurant': restaurant, 'csrfmiddlewaretoken': getCookie('csrftoken')};
	var status = $.post(url, data, function(data, status){
		// if favorite addition was successful, make button reflect addition.
		if(status == 'success'){
			var elementId = "#%s";
			var element = elementId.replace('%s', markerId);
			var glyphType = jQuery(element).find('span.glyphicon').attr('class');
			if(glyphType.indexOf('plus') > -1){
				jQuery(element).css("background-color", "rgb(215, 222, 216)");
				jQuery(element).find('span.glyphicon').removeClass('glyphicon-plus').addClass('glyphicon-ok');
				jQuery(element).find('span#btn-text').text('Favorited');	
				jQuery(element).attr('onclick', "deleteUserFavorite(this.id, userId, " + restaurant + ")");
				restaurants.push(restaurant);
			}
			else if(glyphType.indexOf('ok') > -1){
				jQuery(element).css("background-color", "rgba(193, 220, 194, 0.75)");
				jQuery(element).find('span.glyphicon').removeClass('glyphicon-ok').addClass('glyphicon-minus');
				jQuery(element).find('span#btn-text').text('Unfavorite');	
				jQuery(element).attr('onclick', "deleteUserFavorite(this.id, userId, " + restaurant + ")");				
			}
		}
	});

}

function deleteUserFavorite(markerId, user, restaurant){
	$.ajax({
	    url: "/v1/favorites/user/" + user + "/restaurant/" + restaurant + "/",
	    type: 'DELETE',
		beforeSend: function(xhr) {
        	xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
    	}, 	    
    	success: function(result) {
	        var elementId = "#%s"; 
	        var element = elementId.replace('%s', markerId);
			var glyphType = jQuery(element).find('span.glyphicon').attr('class');
			// Distinguishing between fav button in favorites page or main page. 
			if(glyphType.indexOf('ok') > -1) { 
				jQuery(element).css("background-color", "rgba(193, 220, 194, 0.75)");
				jQuery(element).find('span.glyphicon').removeClass('glyphicon-ok').addClass('glyphicon-plus');
				jQuery(element).find('span#btn-text').text('Favorite');	
				jQuery(element).attr('onclick', "addUserFavorite(this.id, userId, " + restaurant + ")");
				var index = restaurants.indexOf(restaurant);
				restaurants.splice(index, 1);	        
			}
			else if(glyphType.indexOf('minus') > -1){
				jQuery(element).css("background-color", "rgb(215, 222, 216)");
				jQuery(element).find('span.glyphicon').removeClass('glyphicon-minus').addClass('glyphicon-ok');
				jQuery(element).find('span#btn-text').text('Unfavorited');	
				jQuery(element).attr('onclick', "addUserFavorite(this.id, userId, " + restaurant + ")");
			}
	    }
	});
}

// Get list of user's favorite restaurants
function getUserFavorites(user){
	url = "/v1/favorites/user/" + user + "/";
	var items = []; 
	$.ajax({
		url: url, 
		type: 'GET', 
		async: false, 
		dataType: 'json', 
		success: function (restaurants){
			$.each( restaurants, function( key, data ){
				items.push(data.restaurant);
			});
		}
	});
	return items; 
}

function triggerOptions(id){
	var element = "#" + id + "-info";
	if(jQuery(element).css('display') === 'none'){
		jQuery(element).show('slow');
	}
	else {
		jQuery(element).hide();
	}
}

$('#myModal').on('shown.bs.modal', function() {
	google.maps.event.trigger(favMap, "resize");
	var latLng = marker.getPosition()
	favMap.setCenter(latLng);
	renderCurrentPosition();
});


var favMap;
var directionsService = new google.maps.DirectionsService();
var directionsDisplay;
var myLatLng;
var latlng;
var marker;
// Trigger modal map in favorites page to load. 
function triggerMap(lat, lng, name) {
	directionsDisplay = new google.maps.DirectionsRenderer();
    var options={
        center: {lat: lat, lng: lng},
        zoom: 12
    	};
    favMap = new google.maps.Map(document.getElementById('dvMap'), options); 
    directionsDisplay.setMap(favMap);  
    latlng = new google.maps.LatLng(lat, lng);
    var markerOptions = {position: latlng, title: name};
    marker = new google.maps.Marker(markerOptions);
    marker.setMap(favMap);
    jQuery(".modal-title").text(name);
}

// Render current position on favorites map 
var currLocationMarker;
function renderCurrentPosition(){
    var pinImage = new google.maps.MarkerImage("http://maps.google.com/mapfiles/ms/icons/yellow-dot.png");
    if (navigator.geolocation) {
	    navigator.geolocation.getCurrentPosition(function(position) {
	      myLatLng = {
	        lat: position.coords.latitude,
	        lng: position.coords.longitude
	      };
			currLocationMarker = new google.maps.Marker({
				position: myLatLng, 
				icon: pinImage, 
				title: "Current location"
			});
			currLocationMarker.setMap(favMap);
	    });
	} 
}

function calcRoute(){
	calculateAndDisplayRoute(directionsService, directionsDisplay, latlng);
}




