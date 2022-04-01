 alert("Правила: копите деньги и прокачиваетесь, в минус можно уходить до -100, далее вы проиграете!")
var score = 0;
var updating = 1;
var minus = 0;
score = +localStorage.getItem('score');
if (!(!isNaN(parseFloat(score)) && isFinite(score))) score = 0
window.onunload = () => {
  localStorage.setItem('score', score)
};
teg();
function teg () {
  document.getElementsByTagName("h1")[0].firstChild.data = score + "$";
}
//+$
function clickBtn() {
  score = score + updating;
  teg();
  new Audio('img/jg-032316-sfx-elevator-button.mp3').play(); return false;
}
//Прокачка
function update() {
  score = score - 100;
  if (score > 0) {

      updating += 1;
      teg();
      level();
  }
  else{
    if1();
     score = score + 100;
     }
}
function update1() {
    score = score - 150;
  if (score> 0) {
      updating += 2;
      teg();
      level();
  }
  else{
  score = score + 150;
    if1();
  }
}
function update2() {
  score = score - 250;
  if (score > 0) {
      updating += 3;
      teg();
      level();
  }
  else{
    if1();
    score = score + 250;
  }
}
function update3() {
  score = score - 500;
  if(score> 0 ){
      updating += 10;
      teg();
      level();
  }
  else{
    if1();
    score = score - 500;
  }
}
function if1() {

}
//автоклике
function auto() {
  score = score - 10000;
  if (score > 0){
  teg();
  if1();
  setTimeout("plusauto()", 1000);
  }
  else{
    score = score + 10000;
  }
}
//вызов автокликера для его работы
function plusauto () {
  score += updating;
  teg();
  setTimeout("auto1()", 1000);
}
function auto1 () {
  score += updating;
  setTimeout("plusauto()", 1000);
  teg();
}
//временная пасхалка\\
function pashalka () {
  score += 10000;
  teg();
}
function level () {
  document.getElementsByTagName("h3")[0].firstChild.data = "Ваш уровень: " + updating;
}
function reboot () {
  alert("Ваш уровень прокачки " + updating + ". Ваш баланс " + score + " .");
}
function dialog () {
  minus = 1;
  minus = parseInt(prompt("На сколько уровней прокачать(x*50, и это минус ваши деньги)", 5));
  if (!(!isNaN(parseFloat(minus)) && isFinite(minus))) return;
  score = score - 100 * minus;
  if(score >0){
  dialog1();
  teg();
  nan();
  }else{
    if1();
    score = score + 100 * minus;
    }

}
function dialog1 () {
  score -= minus * 50;
  updating += minus;
  teg();
  document.getElementsByTagName("h3")[0].firstChild.data = "Ваш уровень: " + updating;
  if1()
  nan();
}
//таймер
window.onload = () => {
  StartStop();
}
//объявляем переменные
var base = 60;
var clocktimer, dateObj, dh, dm, ds, ms;
var readout = '';
var h = 1,
  m = 1,
  tm = 1,
  s = 0,
  ts = 0,
  ms = 0,
  init = 0;
//функция для очистки поля
function ClearСlock() {
  clearTimeout(clocktimer);
  h = 1;
  m = 1;
  tm = 1;
  s = 0;
  ts = 0;
  ms = 0;
  init = 0;
  readout = '00:00:00';
  document.MyForm.stopwatch.value = readout;
}
//функция для старта секундомера
function StartTIME() {
  var cdateObj = new Date();
  var t = (cdateObj.getTime() - dateObj.getTime()) - (s * 1000);
  if (t > 999) {
    s++;
  }
  if (s >= (m * base)) {
    ts = 0;
    m++;
  } else {
    ts = parseInt((ms / 100) + s);
    if (ts >= base) {
      ts = ts - ((m - 1) * base);
    }
  }
  if (m > (h * base)) {
    tm = 1;
    h++;
  } else {
    tm = parseInt((ms / 100) + m);
    if (tm >= base) {
      tm = tm - ((h - 1) * base);
    }
  }
  ms = Math.round(t / 10);
  if (ms > 99) {
    ms = 0;
  }
  if (ms == 0) {
    ms = '00';
  }
  if (ms > 0 && ms <= 9) {
    ms = '0' + ms;
  }
  if (ts > 0) {
    ds = ts;
    if (ts < 10) {
      ds = '0' + ts;
    }
  } else {
    ds = '00';
  }
  dm = tm - 1;
  if (dm > 0) {
    if (dm < 10) {
      dm = '0' + dm;
    }
  } else {
    dm = '00';
  }
  dh = h - 1;
  if (dh > 0) {
    if (dh < 10) {
      dh = '0' + dh;
    }
  } else {
    dh = '00';
  }
  readout = dh + ':' + dm + ':' + ds;
  document.MyForm.stopwatch.value = readout;
  clocktimer = setTimeout("StartTIME()", 1);
}
//Функция запуска и остановки
function StartStop() {
  if (init == 0) {
    ClearСlock();
    dateObj = new Date();
    StartTIME();
    init = 1;
  } else {
    clearTimeout(clocktimer);
    init = 0;
  }
}
function nan () {
  if (money == NaN) {
    money = 0;
  }
}
