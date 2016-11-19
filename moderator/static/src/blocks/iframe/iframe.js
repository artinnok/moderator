var url = require("url");

VK.init(function () {
    var query = url.parse(window.location.href, true).query;
    var owner_id = query.group_id;
    var permissions = query.api_settings;
    var installed = query.is_app_user;
    var mask = 8192;

    if (installed == false){
        VK.callMethod("showSettingsBox", mask);
    }
    else{
        if (permissions < mask){
            VK.callMethod("showSettingsBox", mask);
        }
    }


    VK.addCallback("onSettingsChanged", function(perm, token){
        window.localStorage.setItem('moder.access_token', token);
        window.localStorage.setItem('moder.owner_id', owner_id);
    });
}, function () {
    window.location.reload()
}, '5.60');


