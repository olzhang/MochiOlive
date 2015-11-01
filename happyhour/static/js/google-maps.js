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

//attach the infowindow to marker
function bindInfoWindow(marker, map, infowindow, description) {
    google.maps.event.addListener(marker, 'click', function() {
        closePreviousInfoWindow();
        if(prev_infowindow == infowindow) {
           prev_infowindow.close();
           prev_infowindow = null;
           return;
        }
        prev_infowindow = infowindow;
        infowindow.setContent(description);
        infowindow.open(map, marker);
    });

    google.maps.event.addListener(map, 'click', function() {
        infowindow.close();
    });
}

function closePreviousInfoWindow(){
     if( prev_infowindow ) {
           prev_infowindow.close();
        }
}

// Mark all happy hour restaurants on map
function markPoint(){
    var restaurants = getData();
    console.log(restaurants[0].id); 
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

        bindInfoWindow(marker, map, infowindow, restaurant.name);
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
  console.log(items);
  return items;
}