let inputin = document.querySelector('#inp');
let btn = document.querySelector('#go');

btn.onclick = function () {
    if (inputin.value == 'thebestwebsiteofalltime') {
        window.location.href = 'http://127.0.0.1:8000/game/';
    } else {
        window.location.href = 'http://127.0.0.1:8000/fail';
    }
};


