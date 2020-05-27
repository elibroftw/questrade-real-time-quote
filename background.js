// TODO: add delay option (seconds)
// TODO: add options_ui

var MS_DELAY = 1000;

function clickBtns() {
    btns = document.getElementsByClassName('snap-timer');
    for (const btn of btns) {
        btn.click();
    }
    if (document.hasFocus()) {
        window.setTimeout(clickBtns, MS_DELAY);
    } else {
        window.onfocus = clickBtns;
    }
}


clickBtns();
