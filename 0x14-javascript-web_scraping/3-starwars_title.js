#!/usr/bin/node
const request = require("request");
const BASE_URL = "https://swapi-api.hbtn.io/api";

if (process.argv.length > 2) {
  request.get(`${BASE_URL}/films/${process.argv[2]}/`, (err, res, body) => {
    if (err) {
      console.log(err);
    } else {
      console.log(JSON.parse(body).title);
    }
  });
}
