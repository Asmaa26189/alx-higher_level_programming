#!/usr/bin/node

const filePath = process.argv[2];
const data = process.argv[3];
const fs = require('fs');
fs.writeFile(filePath, data, err => {
  if (err) {
    console.log(err);
  }
});
