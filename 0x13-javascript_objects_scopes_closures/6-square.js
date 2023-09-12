#!/usr/bin/node
const SquareType = require('./5-square');

class Square extends SquareType {
	charPrint(c) {
		if (c === undefined) {
			c = 'X';
		}
		for (let i = 0; i < this.height; i++) {
			console.log(c.repeat(this.width));
		}
	}
}

module.exports = Square;
