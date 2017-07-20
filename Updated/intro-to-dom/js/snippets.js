var teacherArray = ["Wes", "Garrett", "Baylee"];

// For Loop:
for(var i = 0; i < teacherArray.length; i++) {
    console.log(teacherArray[i]);
}

var currentTeacher = teacherArray[0];

// If-Else Statement:

if (currentTeacher === "Wes") {
    console.log("Wait a moment...");
}
else if (currentTeacher === "Garrett") {
    console.log("That's not right either!");
}
else {
    console.log("Yes! Baylee is teaching today!");
}


// DOM

document.getElementsByTagName('p');

var elems = document.getElementsByTagName('p');

elems

elems[0];

elems[0].textContent;



// Event Listeners
var evtlst = function(){
  var elem = document.getElementById('firstPara');

  elem.addEventListener('click', function(){
    if(elem.style.color === 'red'){
      elem.style.color = 'green';
    }else{
      elem.style.color = 'red';
    }
  });

};

// activate by directly invoking function
evtlst();


// activate after page load
window.onload = function(){
  evtlst();
};

// or activate with IIF
var evtlst = (function(){
  var elem = document.getElementById('firstPara');

  elem.addEventListener('click', function(){
    if(elem.style.color === 'red'){
      elem.style.color = 'green';
    }else{
      elem.style.color = 'red';
    }
  });
}());


// Callback example

var simpleCb = function(item1, item2, callback){
  console.log('I am eating a sandwich with '+item1+' and '+item2+'.');
  callback();
};

var message = function(){
  alert('Finished eating my sandwich!');
};

var timer = function(){
  window.setTimeout(message, 1000);
};


simpleCb('ham', 'cheese', timer);