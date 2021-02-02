
$(document).ready(function(){
    $("#id_username").attr('placeholder', 'Username');
    $("#id_username").attr('class', 'SignupInputs');
    
    $("#id_password").attr('placeholder', 'Password');
    $("#id_password").attr('class', 'SignupInputs');

    $("#id_password1").attr('placeholder', 'Password');
    $("#id_password1").attr('class', 'SignupInputs');

    $("#id_password2").attr('placeholder', 'Password');
    $("#id_password2").attr('class', 'SignupInputs');

    $("#id_email").attr('placeholder', 'error@mail.com');
    $("#id_email").attr('class', 'SignupInputs');

    $("#id_title").attr('placeholder', 'Title');
    //$("#id_title").attr('class', 'SignupInputs');
    $("#id_title").attr('style', 'margin-bottom: 2px;height: 100%; width: 100%; border: none; padding: 10px; box-sizing: border-box;');
    

    $("#id_description").attr('placeholder', 'Write a Response...');
    $("#id_description").attr('style', 'position: absolute; display: block; top:0; left:0; margin: 0; height: 100%; width: 100%; border: none; padding: 10px; box-sizing: border-box;');
    
});
