#!/usr/bin/node
const request = require('request');
const endPoint = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request.get(endPoint, function (err, res, body) {
  if (err) {
    throw err;
  } else if (res.statusCode === 200) {
    const list = JSON.parse(body).characters;
    const l = [];
    list.forEach(ch => {
      l.push(new Promise((resolve, reject) => {
        request.get(ch, function (err, res, body) {
          if (err) {
            reject(err);
          } else if (res.statusCode === 200) {
            resolve(JSON.parse(body).name);
          }
        });
      }));
    });
    Promise.all(l).then(names => {
      names.forEach(name => console.log(name));
    });
  }
});
