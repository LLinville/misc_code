var http = require("http").default;

var options = {
  method: 'GET',
  url: 'https://imdb-internet-movie-database-unofficial.p.rapidapi.com/film/10000',
  headers: {
    'x-rapidapi-host': 'imdb-internet-movie-database-unofficial.p.rapidapi.com',
    'x-rapidapi-key': '22e110fec9msh31ddf964854d045p183004jsnc60cd67c9606'
  }
};

var fs = require('fs');
fs.readFile( __dirname + '/names', function (err, data) {
  if (err) {
    throw err;
  }
  console.log(data.toString());
});

http.request(options).then(function (response) {
	console.log(response.data);
}).catch(function (error) {
	console.error(error);
});

