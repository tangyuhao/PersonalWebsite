$(document).ready(function() {
     $("#form-login").submit(login_handler);

});

login_error_handler = function(data,status){
    $("#error_div").css("display","block");    
};
login_success_handler = function(data,status){
    window.location.replace('/');
};

function login_handler(event){
    event.preventDefault();
    var login_url = "/api/login";
    var data_dict ={
            username: $('#login_username_input').val(),
            password: $('#login_password_input').val()
    }
    $.ajax({
            url: login_url,
            type: "POST",
            data: JSON.stringify(data_dict),
            dataType: "json",
            success: login_success_handler,
            error: login_error_handler,
            contentType: "application/json"
        });

}