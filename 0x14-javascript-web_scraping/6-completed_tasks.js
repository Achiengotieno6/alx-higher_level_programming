#!/usr/bin/node

const request = require('request');

const Url = process.argv[2];

request(Url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const tasks = JSON.parse(body);
    const userTasks = {};

    for (const task of tasks) {
      if (task.completed) {
        userTasks[task.userId] = (userTasks[task.userId] ?? 0) + 1;
      }
    }

    console.log(userTasks);
  }
});
