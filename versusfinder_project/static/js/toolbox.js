class BanlistTools {

    static alter(user_id, char_id)
    {
      $.ajax({
          type: 'POST',
          url : "/accounts/" + user_id + "/characters/" + char_id + "/alter",
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
}