#!/usr/bin/node
let count = 0;
exports.logMe = function (item) {
    console.log('%d: %s', count, arguments[0] )
    count++;
}