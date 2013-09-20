var dict = [];
var num = 300;
var count = 0;
var dictPairs = [];

function populate() {
	for(var d=-num; d<num; d++) {
		dict[d] = [];
		for(var e=-num; e<num; e++) {
			dict[d][e] = false;
		}
	}
}

function validDigits(x, y) {
	var xTotal = 0;
	var yTotal = 0;
	
	x = Math.abs(x);
	y = Math.abs(y);
	
	while(x >= 1) {
		xTotal += x%10;
		x = Math.floor(x/10);
	}
		
	while(y >= 1) {
		yTotal += y%10;
		y = Math.floor(y/10);
	}
	
	if(xTotal + yTotal <= 19)
		return true;
	
	return false;
}

function check(x, y) {
	if(!dict[x][y] && validDigits(x, y)) {
		dict[x][y] = true;
		count++;
		dictPairs.push(x);
		dictPairs.push(y);
	}
}

function walk(x, y) {
	dict[x][y] = true;
	count++;
	dictPairs.push(x);
	dictPairs.push(y);
	
	var i = 0;
	while(i < dictPairs.length) {
		x = dictPairs[i];
		y = dictPairs[i+1];
		check(x+1, y);
		check(x-1, y);
		check(x, y+1);
		check(x, y-1);
		i+=2;
	}
}

populate();
walk(0, 0);
console.log(count);
