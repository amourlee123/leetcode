/**
 *@desc: fibonacci
 *@param: count {Number}
 *@return: result {Number} 第count个fibonacci值，计数从0开始
  fibonacci数列为：[1, 1, 2, 3, 5, 8, 13, 21, 34 …]
  则getNthFibonacci(0)返回值为1
  则getNthFibonacci(4)返回值为5
 */

function getNthFibonacci(count){

	var count = parseInt(count);
	if ( isNaN(count) || count < 0){
		return 0;
	}	

	function f(count){
		if( count <= 1){
			return 1;
		}
	
		return arguments.callee(count - 1) + arguments.callee(count - 2);
	}

	return f(count);

}
