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
	url = "http://127.0.0.1:8000/v1/favorites/user/" + user + "/"; 
	data = {'user': user, 'restaurant': restaurant, 'csrfmiddlewaretoken': getCookie('csrftoken')};
	var status = $.post(url, data, function(data, status){
		// if favorite addition was successful, make button reflect addition.
		if(status == 'success'){
			var elementId = "#%s";
			var element = elementId.replace('%s', markerId);
			jQuery(element).css("background-color", "rgb(215, 222, 216)");
			jQuery(element).find('span.glyphicon').removeClass('glyphicon-plus').addClass('glyphicon-ok');
			jQuery(element).find('span#btn-text').text('Favorited');	
			jQuery(element).attr('onclick', "deleteUserFavorite(this.id, userId, " + restaurant + ")");
			restaurants.push(restaurant);
		}
	});

}

function deleteUserFavorite(markerId, user, restaurant){
	$.ajax({
	    url: "http://127.0.0.1:8000/v1/favorites/user/" + user + "/restaurant/" + restaurant + "/",
	    type: 'DELETE',
		beforeSend: function(xhr) {
        	xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
    	}, 	    
    	success: function(result) {
	        var elementId = "#%s"; 
	        var element = elementId.replace('%s', markerId);
			jQuery(element).css("background-color", "rgba(193, 220, 194, 0.75)");
			jQuery(element).find('span.glyphicon').removeClass('glyphicon-ok').addClass('glyphicon-plus');
			jQuery(element).find('span#btn-text').text('Favorite');	
			jQuery(element).attr('onclick', "addUserFavorite(this.id, userId, " + restaurant + ")");
			var index = restaurants.indexOf(restaurant);
			restaurants.splice(index, 1);	        
	    }
	});
}

// Get list of user's favorite restaurants
function getUserFavorites(user){
	url = "http://127.0.0.1:8000/v1/favorites/user/" + user + "/";
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
	console.log(items);
	return items; 
}