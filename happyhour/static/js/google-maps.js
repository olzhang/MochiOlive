// Initialize google maps
var map;
function initGoogleMap() {
    var options={
        center: {lat: 49.25, lng: -123.1},
        zoom: 11
    };
    map = new google.maps.Map(document.getElementById('map'), options);
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
        // marker.setMap(map);
        markers.push(marker);
    }
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