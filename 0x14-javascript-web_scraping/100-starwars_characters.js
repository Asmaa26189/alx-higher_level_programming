#!/usr/bin/node
const request = require('request');
const endPoint = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request.get(endPoint, function (err, res, body) {
  if (err) {
    throw err;
  } else if (res.statusCode === 200) {
    const list = JSON.parse(body).characters;
    list.forEach(ch => {
      request.get(ch, function (err, res, body) {
        if (err) {
          throw err;
        } else if (res.statusCode === 200) {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
