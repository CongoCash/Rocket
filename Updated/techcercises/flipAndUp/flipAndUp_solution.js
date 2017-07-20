/*Solution code for flipAndUp*/

// flipAndUp is a nonsense function that will take the input string, reverse the order of the characters AND convert all of the non-vowel characters to uppercase. It then returns the new string. 


var flipAndUp = function (str) {
  var res = '';
  var vowels = 'aeiouAEIOU';
  var i;
  var excluded = '!@#$%^&*()_-+=<>? /';
  for (i = str.length - 1; i >= 0; i--) {
    if (excluded.indexOf(str[i]) === -1){
      if (vowels.indexOf(str[i]) === -1){
        var temp = str[i].toUpperCase();
        res += temp;
      }else{
        res += str[i];
      }
    }

  }
  return res;
};

console.log(flipAndUp('ehr&*$%ugferhgndfhnvglauyntva'));