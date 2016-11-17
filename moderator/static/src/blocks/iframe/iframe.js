var url = require("url");

$(document).ready(function () {
    var query = url.parse(window.location.href, true).query;
    var owner_id = query.group_id;
    var permissions = query.api_settings;
    var access_token = query.access_token;
    var installed = query.is_app_user;
    var mask = 262144;

    if (installed == false){
        VK.callMethod("showGroupSettingsBox", mask);
    }
    else{
        if (permissions != mask){
            VK.callMethod("showGroupSettingsBox", mask);
        }
    }
    $.on("onGroupSettingsChanged", function (event) {
        alert(event.data);
    })
});