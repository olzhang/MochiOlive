/// <reference path="../ts/google.maps.d.ts.1.0.10/content/typings/google.maps.d.ts" />
module Mapping {
    export class GoogleMap {

        public name: string;
        private map: any;
        private options: any;

        constructor (mapDiv:Element) {
            this.name = "GoogleMap";
            this.options = { center: {lat: 49.25, lng: -123.1}, zoom: 10 };
            this.map = new google.maps.Map(mapDiv, this.options);
         }
    }
}