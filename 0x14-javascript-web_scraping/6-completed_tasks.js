#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
	if (error) {
		console.error(error);
	} else {
		const todos = JSON.parse(body);
		const completedTasksByUserId = {};

		todos.forEach((todo) => {
			if (todo.completed) {
				if (!completedTasksByUserId[todo.userId]) {
					completedTasksByUserId[todo.userId] = 1;
				} else {
					completedTasksByUserId[todo.userId]++;
				}
			}
		});

		console.log('Users with completed tasks:');
		for (const userId in completedTasksByUserId) {
			console.log('User ID: ${userId} - Completed Tasks: ${completedTasksByUserId[userId]}');
		}
	}
});
