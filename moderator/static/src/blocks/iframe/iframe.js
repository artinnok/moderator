var url = require("url");

$(document).ready(function () {
    var query = url.parse(window.location.href, true).query;
    var owner_id = query.group_id;
    var permissions = query.api_settings;
    var access_token = query.access_token;
    var installed = query.is_app_user;
    var mask = 262144;
    console.log(query);

    if (installed == false){
        VK.callMethod("showGroupSettingsBox", mask);
    }
    else{
        if (permissions >= mask){
            VK.callMethod("showGroupSettingsBox", mask);
        }
    }
    VK.addCallback("onGroupSettingsChanged", function(data){
       console.log(data);
    });
});