/**
 *@param {number}num
 *@return {string}
*/
var intToRoman = function(num){
	var toRoman = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"];
	var numSet = [1000,900,500,400,100,90,50,40,10,9,5,4,1];
	var each = [];
	var result = "";
	for (var i = 0 ; i < numSet.length ; i++ ){
		each[i] = parseInt(num/numSet[i]);
		for (var j = 0 ; j < each[i], j++){
			result += toRoman[i];
		}
		num = num - each[i]*numSet[i];
	}
	return result;
}
