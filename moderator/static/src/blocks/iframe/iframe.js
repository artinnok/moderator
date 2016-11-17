var url = require("url");

VK.init(function () {
    var query = url.parse(window.location.href, true).query;
    var owner_id = query.group_id;
    var permissions = query.api_settings;
    var access_token = query.access_token;
    var installed = query.is_app_user;
    var mask = 4096;
    console.log(query);

    if (installed == false){
        VK.callMethod("showGroupSettingsBox", mask);
    }
    else{
        if (permissions != mask){
            VK.callMethod("showGroupSettingsBox", mask);
        }
    }
    VK.addCallback("onGroupSettingsChanged", function(data){
       console.log(data);
    });
    VK.api("wall.deleteComment", {
        "owner_id": -132545756,
        "comment_id": 7
    }, function (data) {
        console.log(data);
    })
}, function () {

}, '5.60');
