#!/usr/bin/node
dict = require('./101-data').dict
console.log(dict)
var keys = Object.keys(dict)
console.log(keys)
new_dict = {}
temp = []
console.log(keys)
while (true) {
    for (let key of keys) {
        if ((dict[key]) === dict[keys[0]]) {
            temp.push(key)
            console.log(key)
            console.log(temp)
        }
    }
    new_dict[dict[keys[0]]] = temp
    keys = keys.filter(function(element, index) {
        return (!(temp.includes(element)))
    })
}
console.log(keys)
console.log(temp)
console.log(new_dict)
console.log(keys)