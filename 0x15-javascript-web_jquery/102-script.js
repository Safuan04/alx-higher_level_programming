
$(function () {
    const $lang = $('#language_code');
    $('#btn_translate').on('click', function() {
        if ($lang.length > 0) {
            const langInput = $lang.val()
            $.ajax({
                type: 'GET',
                url: 'https://hellosalut.stefanbohacek.dev/?lang='+langInput,
                success: function (data) {
                    $('#hello').html(data.hello).text();
                }
            });
        } 
    })
})
