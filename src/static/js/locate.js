function getLocation() {
    if(navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(position) {
        	/* lookupCity(position.coords.latitude, position.coords.longitude);*/
        	document.getElementById("location").value = "Washington, DC";
        });
    }
}
