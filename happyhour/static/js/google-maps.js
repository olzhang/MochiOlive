// Initialize google maps
var map;
function initGoogleMap() {
    var options={
        center: {lat: 49.25, lng: -123.1},
        zoom: 10
    };
  map = new google.maps.Map(document.getElementById('map'), options);
}

function markPoint(){
    var latlng = new google.maps.LatLng(49.25, -123.1);
    var comment = "New point!";
    var options = {position: latlng, title: comment};
    var marker = new google.maps.Marker(options);
    marker.setMap(map);
}
