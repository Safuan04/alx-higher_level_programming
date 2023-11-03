
$(function () {
    const $listmovies = $('#list_movies');

    $.ajax({
        type: 'GET',
        url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
        success: function (data) {
            $.each(data.results, function (i, movies) {
                $listmovies.append('<li>'+movies.title+'</li>');
            });
        }
    })
});
