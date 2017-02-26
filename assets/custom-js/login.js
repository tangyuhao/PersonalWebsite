$(document).ready(function() {
     $("#form-login").submit(login_handler);

});

error_handler = function(data,status){
    $("#error_div").css("display","block");    
};
success_handler = function(data,status){
    window.location.replace('/');
};

function login_handler(event){
    event.preventDefault();
    var login_url = "/api/login"
    var data_dict ={
            username: $('#login_username_input').val(),
            password: $('#login_password_input').val()
    }
    $.ajax({
            url: login_url,
            type: "POST",
            data: JSON.stringify(data_dict),
            dataType: "json",
            success: success_handler,
            error: error_handler,
            contentType: "application/json"
        });

}