// Initialize google maps
var map;
var prev_infowindow;

var directionsService;
var directionsDisplay;
var myLatLng;

function initGoogleMap() {
    var options={
        center: {lat: 49.25, lng: -123.1},
        zoom: 11
    };
    directionsService = new google.maps.DirectionsService;
    directionsDisplay = new google.maps.DirectionsRenderer;
    map = new google.maps.Map(document.getElementById('map'), options);
    directionsDisplay.setMap(map);
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
    myLatLng = {lat: lat, lng: lon};
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

 // link restaurant table rows to marker on map
 function triggerMarker(tableId) {
  var currentMarker = markers[tableId - 1];
  cluster.removeMarker(currentMarker);
  currentMarker.setMap(map);
  var infowindow = infowindows[tableId - 1];
  closePreviousInfoWindow();
  if(prev_infowindow == infowindow) {
    prev_infowindow.close();
    prev_infowindow = null;
  }
  if(typeof prev_marker !== 'undefined'){
    cluster.addMarker(prev_marker);
  }
  infowindow.open(map, currentMarker);
  prev_infowindow = infowindow;
  prev_marker = currentMarker;

   google.maps.event.addListener(map, 'click', function() {
     infowindow.close();
    cluster.addMarker(currentMarker);
   });
 }
//attach the infowindow to marker
function bindInfoWindow(marker, map, infowindow, restaurant, latlng) {
    infowindow.setContent(setInfo(restaurant, latlng));
    google.maps.event.addListener(marker, 'click', function() {
        //calculateAndDisplayRoute(directionsService, directionsDisplay,latlng);
        closePreviousInfoWindow();
        if(prev_infowindow == infowindow) {
           prev_infowindow.close();
           prev_infowindow = null;
           return;
        }
        prev_infowindow = infowindow;
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

function setInfo(restaurant, latlng) {
  var favoritesButton = setFavButton(restaurant);
  var routeButton = setRouteButton(latlng);
  var tweetButton = setTweetButton(restaurant);
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
    '</div>' + favoritesButton + routeButton + tweetButton + 
  '</div>');
}

function setFavButton(restaurant){
  var favoritesButton;
  if(typeof userId !== 'undefined'){
    if (restaurants.indexOf(restaurant.id) > -1){
      favoritesButton = '<div class="btn-group favorites-map">' + '<button id="map-fav-' + restaurant.id + 
          '" type="button" class="btn btn-favorites btn-favorited" onclick="deleteUserFavorite(this.id, userId, ' + restaurant.id + ')">' +
          '<span class="glyphicon glyphicon-ok"></span><span>  </span><span id="btn-text">Favorited</span>' + '</button>' + 
          '</div>';
    }
    else {
      favoritesButton = '<div class="btn-group favorites-map">' + '<button id="map-fav-' + restaurant.id + 
        '" type="button" class="btn btn-favorites" onclick="addUserFavorite(this.id, userId, ' + restaurant.id + ')">' +
        '<span class="glyphicon glyphicon-plus"></span><span>  </span><span id="btn-text">Favorite</span>' + '</button>' + 
        '</div>';
    }
  }
  else { 
    favoritesButton = ''; 
  }
  return favoritesButton;
}

function setRouteButton(latlng){
    var routeDiv;
      routeDiv =  '<div class="btn-group favorites-map">' + 
                    '<button id="route_btn"' +
                        'type="button" class="btn btn-favorites"' +
                        'onclick="calculateAndDisplayRoute(directionsService, directionsDisplay, currentMarkerLatlng)">' +
                        '<span class="glyphicon glyphicon-globe"></span>' +
                        '<span id="btn-text"> Plot direction </span>' +
                        '</button>' + 
                        '</div>';
  return routeDiv;
}

function setTweetButton(restaurant){
  var tweetDiv;
    tweetDiv = '<div class="btn-group favorites-map">' + 
                    '<a href="https://twitter.com/intent/tweet?button_hashtag=MochiOliveHappyHour&text=My%20Happy%20Hour%20experience%20at ' + restaurant.name +'" class="btn btn-favorites">' + '<span class="glyphicon glyphicon-comment"></span>' +
                     '<span id="btn-text"> Tweet my experience </span>' + '</a>' +
              '</div>';
  return tweetDiv;
}


function closePreviousInfoWindow(){
  if( prev_infowindow ) {
    prev_infowindow.close();
  }
}

var currentMarkerLatlng;

// Mark all happy hour restaurants on map
function markPoint(){
    var restaurants = getData();
    markers = [];
    infowindows = [];
    for (key in restaurants){
        var restaurant = restaurants[key];
        var lat = restaurant.location_lat;
        var lng = restaurant.location_long;
        var latlng = new google.maps.LatLng(lat, lng);
        var options = {position: latlng, title: restaurant.name};
        var marker = new google.maps.Marker(options);
        var infowindow =  new google.maps.InfoWindow();
        // marker.setMap(map);
        marker.addListener('click', function() {
          currentMarkerLatlng = this.getPosition();
        });
        bindInfoWindow(marker, map, infowindow, restaurant, latlng);
        infowindows.push(infowindow);
        markers.push(marker);
  };
    cluster = new MarkerClusterer(map, markers);
}

// Get happy hour restaurant data
function getData(){
    var items = {};
    $.ajax({
        url: '/v1/restaurants/',
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

function calculateAndDisplayRoute(directionsService, directionsDisplay, end) {
  if (myLatLng == null) {
    window.alert('Your position has not been set yet, please wait');
    return;
  } else {
      //console.log(start.lat);
  }
  //var tempLatLng = new LatLng (lat: myLatLng.lat, lng: myLatLng.lng);
  directionsService.route({
    origin: myLatLng,
    destination: end,
    travelMode: google.maps.TravelMode.WALKING
    }, function(response, status) {
    if (status === google.maps.DirectionsStatus.OK) {
      directionsDisplay.setOptions({ preserveViewport: true });
      directionsDisplay.setOptions({ suppressMarkers: true });
      directionsDisplay.setDirections(response);
    } else {
      window.alert('Directions request failed due to ' + status);
    }
  });
}
