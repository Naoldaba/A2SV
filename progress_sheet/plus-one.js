/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
    let strdig=digits.join('');
    strdig=BigInt(strdig)+1n;
    strdig=strdig.toString()
    console.log(typeof strdig)
    let final=strdig.split('')
    final=final.map(num=>Number(num))
    return final

    
};