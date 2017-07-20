function CoinDeterminer(num) {
	var res = 0;
	var Coin = [1,5,7,9,11];

	var quotinet = Math.floor(num/Coin[4]);
	var remainder = num%Coin[4];

	res = res + quotinet + changeCoin(remainder);
	//console.log(res);
	if (remainder != 3 && remainder != 4) {
		return res;
	} else if (remainder === 3 || remainder === 4) {
		var Recal = 0;
		Recal = Recal + Math.floor(num/Coin[3]) + changeCoin(num%Coin[3]);
		if (Recal > res) {
			return res;
		} else {
			return Recal;
		}

	}
	function changeCoin(rem) {
		switch (rem) {
			case 0:
				return 0;
				break;
			case 1:
				return 1;
				break;
			case 2:
				return 2;
				break;
			case 3:
				return 3;
				break;
			case 4:
				return 4;
				break;
			case 5:
				return 1;
				break;
			case 6:
				return 2;
				break;
			case 7:
				return 1;
				break;
			case 8:
				return 2;
				break;
			case 9:
				return 1;
				break;
			case 10:
				return 2;
				break;
		}
	}

}