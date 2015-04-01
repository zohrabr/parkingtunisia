function load_markers(c){
    $.get('/car/liste/', function(data){
        create_markers(c, data);
    });
}

function addMarker(map, latlng, nb_places_libres, nom,nbtot,tel){
    var theaf = '/static/img/p.png';
    var marker = new google.maps.Marker({
        map: map,
        position: latlng,
        icon: theaf
    });
    google.maps.event.addListener(marker, 'click', function(){
            var form = '<div id="marker_option" >'+
                "Parking "+'<font color="green">'+ nom +'</font>' +"</br> Nbre de place disponible : "+ '<font color="red">'
                +nb_places_libres+'</font>'+ '</br> Nbre total de place: ' + '<font color="red">'+nbtot+'</font>'+'</br> Tel :' +'<font color="blue">'+tel + '</font>'
                '</div>';
            var infoWin = new google.maps.InfoWindow({content: form});
            infoWin.open(map, marker);
    });
    return marker;
}

function create_markers(c, data){
    var l = data.length;
    var markers = [];
    var theaf = '/static/img/p.png';
    for ( var i=0; i<l; i++) {
        var coordenates = data[i][1].split(",");
        var lat = parseFloat(coordenates[0]);
        var lon = parseFloat(coordenates[1]);
        console.log(lat+" "+lon);
        var nb_places_libres = parseInt(data[i][2]);
        console.log(nb_places_libres);
	var nom =data[i][0] ;
	console.log(nom);
	var nbtot = parseInt(data[i][3]);
        console.log(nbtot);
	var tel =data[i][4] ;
	console.log(tel);
        var the_marker = addMarker(c, new google.maps.LatLng(lat, lon), nb_places_libres,nom,nbtot,tel);
        markers.push(the_marker);
        google.maps.event.addListener(the_marker, 'click', function(){
            console.log("marker clicked at " + this.getPosition());
        });
    }
    console.log(markers.length);
    var mcoptions = {

    };
    var mc = new MarkerClusterer(c, markers);
}



    var center = new google.maps.LatLng(36.795, 10.15);
    var options = {
        center: center,
        zoom: 12,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    var carte = new google.maps.Map($('#map-canvas')[0], options);
    load_markers(carte);

