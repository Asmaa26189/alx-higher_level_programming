#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const myDict = {};

request(url, function (err, data, body) {
  if (err) {
    console.log(err);
  } else {
    const res = JSON.parse(body);

    for (let i = 0; i < res.length; i++) {
      if (res[i].completed === true) {
        if (myDict[res[i].userId] === undefined) {
          myDict[res[i].userId] = 1;
        } else {
          myDict[res[i].userId] += 1;
        }
      }
    }
  }
  console.log(myDict);
});
