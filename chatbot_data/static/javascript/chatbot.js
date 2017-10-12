$('document').ready(function () {

    $('#submit').on('click', function () {
        var $question = $('#question');
        var questionText = $question.val();
        var $responsePlaceholder = $("#machineResponse");
        if(questionText !== '' || questionText !== 'undefined') {
            var content = {
                'question': questionText
            };
            var url = 'https://cryptic-hamlet-56422.herokuapp.com/ask-question/';
            var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
            function csrfSafeMethod(method) {
                return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
            }
            $.ajax({
                url: url,
                type: 'POST',
                dataType: 'json',
                data: content,
                beforeSend: function(xhr, settings) {
                    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                        xhr.setRequestHeader("X-CSRFToken", csrftoken);
                    }
                },
                success: function (data) {
                    $responsePlaceholder.html(data.response);
                }
            });
        }
    });
});