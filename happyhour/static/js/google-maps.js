// Initialize google maps
var map;
var prev_infowindow;

function initGoogleMap() {
    var options={
        center: {lat: 49.25, lng: -123.1},
        zoom: 11
    };
    map = new google.maps.Map(document.getElementById('map'), options);
}

window.onload = function() {
  var startPos;
  var geoOptions = {
    enableHighAccuracy: true
  }

  var geoSuccess = function(position) {
    startPos = position;
    var lat = startPos.coords.latitude;
    var lon = startPos.coords.longitude;
    var myLatLng = {lat: lat, lng: lon};
    var pinImage = new google.maps.MarkerImage("http://maps.google.com/mapfiles/ms/icons/yellow-dot.png");
    var tooltip = "Your current location";
    var marker = new google.maps.Marker({
      position: myLatLng,
      map: map,
      icon: pinImage,
      title: tooltip
    });
  };
  var geoError = function(error) {
    console.log('Error occurred. Error code: ' + error.code);
    // error.code can be:
    //   0: unknown error
    //   1: permission denied
    //   2: position unavailable (error response from location provider)
    //   3: timed out
  };

  navigator.geolocation.getCurrentPosition(geoSuccess, geoError, geoOptions);
};

//attach the infowindow to marker
function bindInfoWindow(marker, map, infowindow, restaurant) {
    google.maps.event.addListener(marker, 'click', function() {
        closePreviousInfoWindow();
        if(prev_infowindow == infowindow) {
           prev_infowindow.close();
           prev_infowindow = null;
           return;
        }
        prev_infowindow = infowindow;
        infowindow.setContent(setInfo(restaurant));
        infowindow.open(map, marker);
    });

    google.maps.event.addListener(map, 'click', function() {
        infowindow.close();
    });

    /* This will likely be needed if we want to customize the ui of indowindow more
    google.maps.event.addListener(infowindow, 'domready', function() {
    var iwOuter = $('.gm-style-iw');
    iwOuter.parent().addClass('infowindow_parent');
    });
    */
}

function setInfo(restaurant) {
  console.log(userId);
  console.log(restaurant.id);
 return(
  '<div id="iw_container">' +
    '<div class="iw_title">'+ restaurant.name+'</div>' +
    '<div class="iw_content">' +
      '<img class="iw_pic" src="'+restaurant.image_url+'"></img>'+
      '<p class="iw_info">' +
          '<span class="col">Address : </span>' + restaurant.address +'<br>' +
          '<span class="col">Phone : </span>'+ restaurant.phone_number + '<br>' +
          '<span class="col">Rating : </span>'+restaurant.rating +
      '</p>'+
    '</div>' +
    '<div class="btn-group favorites-map">' +
      '<button id="map-fav-' + restaurant.id + '" type="button" class="btn btn-favorites" onclick="addUserFavorite(this.id, userId, ' + restaurant.id + ')">' +
        '<span class="glyphicon glyphicon-plus"></span><span>  </span><span id="btn-text">Favorite</span>' + 
      '</button>' +
    '</div>' +
    '<div class="btn-group">' +
    '<button id="tweetbtn" type="button" class="btn btn-favorites"' +
    '<span>' +
    '<a href="https://twitter.com/intent/tweet?button_hashtag=' + restaurant.name +'&text=My%20Happy%20Hour%20experience%20at ' + restaurant.name +'" class="twitter-hashtag-button">Tweet My Experience</a>' +
    '</span>' +
    '</button>' +
    '</div>' +
  '</div>');
}

function closePreviousInfoWindow(){
  if( prev_infowindow ) {
    prev_infowindow.close();
  }
}

// Mark all happy hour restaurants on map
function markPoint(){
    var restaurants = getData();
    var markers = [];
    for (key in restaurants){
        var restaurant = restaurants[key];
        var lat = restaurant.location_lat;
        var lng = restaurant.location_long;
        var latlng = new google.maps.LatLng(lat, lng);
        var options = {position: latlng, title: restaurant.name};
        var marker = new google.maps.Marker(options);
        var infowindow =  new google.maps.InfoWindow();
        // marker.setMap(map);

        bindInfoWindow(marker, map, infowindow, restaurant);
        markers.push(marker);
  };
    var cluster = new MarkerClusterer(map, markers);
}

// Get happy hour restaurant data
function getData(){
    var items = {};
    $.ajax({
        url: 'http://127.0.0.1:8000/v1/restaurants/',
        async: false,
        dataType: 'json',
        success: function (restaurants) {
            $.each( restaurants, function( key, data ) {
                items[key] = data;
            });
        }
    });
  return items;
}
