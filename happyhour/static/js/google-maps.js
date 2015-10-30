/// <reference path="../ts/google.maps.d.ts.1.0.10/content/typings/google.maps.d.ts" />
var Mapping;
(function (Mapping) {
    var GoogleMap = (function () {
        function GoogleMap(mapDiv) {
            this.name = "GoogleMap";
            this.options = { center: { lat: 49.25, lng: -123.1 }, zoom: 10 };
            this.map = new google.maps.Map(mapDiv, this.options);
        }
        GoogleMap.prototype.marker = function () {
            var position = new google.maps.LatLng(49.25, -123.1);
            var title = "First marker!";
            var marker = new google.maps.Marker({ 'position': position, 'title': title });
            marker.setMap(this.map);
        };
        return GoogleMap;
    })();
    Mapping.GoogleMap = GoogleMap;
})(Mapping || (Mapping = {}));
