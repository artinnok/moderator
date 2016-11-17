var url = require("url");

$(document).ready(function () {
    var query = url.parse(window.location.href, true).query;
    var owner_id = query.group_id;
    var permissions = query.api_settings;
    var access_token = query.access_token;
    var installed = query.is_app_user;
    var mask = 8192 + 65536;
    console.log(query);

    if (installed == false){
        VK.callMethod("showSettingsBox", mask);
    }
    else{
        if (permissions >= mask){
            VK.callMethod("showSettingsBox", mask);
        }
    }
    VK.addCallback("onSettingsChanged", function(data){
       console.log(data);
    });
});