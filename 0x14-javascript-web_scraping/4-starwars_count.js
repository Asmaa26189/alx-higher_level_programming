#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (err, data, body) {
  if (err) {
    console.log(err);
  } else {
    let count = 0;
    const list = JSON.parse(body).results;
    for (let i = 0; i < list.length; i++) {
      const chs = list[i].characters;
      for (let j = 0; j < chs.length; j++) {
        if (chs[j] === 'https://swapi-api.hbtn.io/api/people/18/' || chs[j] === 'http://swapi-api.hbtn.io/api/people/18/') {
            count += 1;
        }
      }
    }
    console.log(counter);
  }
});
