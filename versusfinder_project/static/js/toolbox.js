class BanlistTools {

    static alter(user_id, gameprofile_id, char_id)
    {
        console.log(user_id)
        console.log(gameprofile_id)
        console.log(char_id)
        $.ajax({
            type: 'POST',
            url : "/dashboard/" + user_id + "/gameprofiles/" + gameprofile_id + "/characters/" + char_id + "/alter",
            headers: {
                'X-CSRFToken': Toolbox.getCookie('csrftoken')
                // csrftoken 
            },
            success : function (data) {
                console.log('ok');
            }
        });
    }
}

class Toolbox
{
    // This snippet is provided in Django official documentation
    static getCookie(name)
    {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    static sendForm(uri)
}