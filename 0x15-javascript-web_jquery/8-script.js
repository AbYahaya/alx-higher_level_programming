$(document).ready(function() {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
    var movies = data.results;
    var list = $('#list_movies');
    movies.forEach(function(movie) {
      list.append('<li>' + movie.title + '</li>');
    });
  });
});
