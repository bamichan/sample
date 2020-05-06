//jqueryには必須↓
$(function(){


  $('#change_btn').on('click',function() {
    $('#txt').text('ボタンを押して更新')
  });






























});

/*=========
var text_node = document.getElementById("txt");
console.log(text_node.textContent);//idがtxtのhtml要素をjsコンソールで取得
text_node.textContent = "ゾロリ参上！！"//idがtxtのhtmlの中身を上書き
=========*/

//comment
/*=========
FizzBuzzゲーム
for(var i= 1;i<=100;i++){
  if(i%15==0){
    console.log("Fizz Buzz");
  }else if (i%5==0){
    console.log("Buzz");
  }else if (i%3==0){
    console.log("Fizz");
  }else{
    console.log(i);
  }
}

平均点と最高点
var scores = [88, 62, 65, 21, 47, 92, 57, 89, 79, 89, 54, 82, 69, 72, 74, 54, 66, 92, 64, 96, 47, 89, 95, 93, 70, 30, 84, 93, 81, 98, 78, 96, 32, 56, 64, 42, 67];

var sum = 0;
for (var i=0;i<scores.length;i++){
  sum += scores[i];
}
var avelage = sum/scores.length;
console.log("平均点は"+avelage+"点です");

var topscore = 0;
for (var i=0;i<scores.length;i++){
  if (topscore<scores[i]){
    topscore=scores[i];
  }
}
console.log("最高点は"+topscore+"点です");
=========*/

/*==========
var btn_node = document.getElementById("change_btn");
btn_node.addEventListener("click",changeTxt);
function changeTxt() {
  let text_node = document.getElementById("txt");
  text_node.textContent = "押された！";
}
=========*/