$(document).ready(function () {
    var hash = window.location.hash;
    hash = hash.replace('#', '?');
    window.location.replace("http://localhost:8000/api/callback/" + hash);
});