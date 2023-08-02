$(document).ready(function() {
	$.get("https://swapi-api.alx-tools.com/api/films/?format=json", function(data) {
		const movieTitles = data.results.map(movie => movie.title);

		const listMovies = $("#list_movies");
		$.each(movieTitles, function(index, title) {
			$("<li>").text(title).appendTo(listMovies);
		});
	});
});
