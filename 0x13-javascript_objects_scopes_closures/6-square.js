class Square extends require('./5-square') {
    constructor(size) {
        super(size);
    }
    charPrint(c) {
        let a = c
        if (typeof(c) === 'undefined') {
            a = 'X'
        }
        for (let i = 0; i < this.width; i++) {
            let line = "";
            for (let j = 0; j < this.width; j++) {
                line += a
            }
            console.log(line)
        }
    }
}
module.exports = Square