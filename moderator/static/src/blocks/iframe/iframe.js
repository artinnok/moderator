var url = require("url");

$(document).ready(function () {
    var query = url.parse(window.location.href, true).query;
    var owner_id = query.group_id;
    var permissions = query.api_settings;
    var access_token = query.access_token;
    var installed = query.is_app_user;
    console.log(query);
    var mask = 0;

    if (installed == false){
        VK.callMethod("showGroupSettingsBox", mask);
    }
    else{
        if (permissions != mask){
            VK.callMethod("showGroupSettingsBox", mask);
        }
    }
    $(document).on("onGroupSettingsChanged",  function () {
        console.log('HERE 1')
    });
    $('body').on("onGroupSettingsChanged",  function () {
        console.log('HERE 2')
    });
    $('*').on("onGroupSettingsChanged",  function () {
        console.log('HERE 3')
    });
});