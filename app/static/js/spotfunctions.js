var clientId = "5300cd177d35485eb638b51cac5d7ee7"
var SPOTIFY_REDIRECT_URI = "http://127.0.0.1:5000/"
var accessToken = ""

$("#spotifybutton").click(function authorizeUser() { 
	var scopes = "playlist-read-private";

	var url = `https://accounts.spotify.com/authorize?&client_id=${clientId}&response_type=code&scope=${encodeURIComponent(scopes)}&redirect_uri=${encodeURIComponent(SPOTIFY_REDIRECT_URI)}`;
	document.location = url;

});

var hash = location.search.split("=")
console.log(location)

accessToken = hash[1]
console.log("Access: " + accessToken)
var url = 'https://api.spotify.com/v1/me'

function getSpotify(url, data) {
    $.ajax(url, {
        dataType: 'json',
        data: data,
        headers: {
            'Authorization': 'Bearer ' + accessToken
        },
        success: function(data) {
            console.log(data)
        },
        error: function(response) {
            console.log(response)
        }
    });
}

function fetchCurrentUserProfile() {
    var url = 'https://api.spotify.com/v1/me';
    getSpotify(url, null);

}

fetchCurrentUserProfile()
