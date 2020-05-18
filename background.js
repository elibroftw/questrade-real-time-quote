// TODO: add delay option (seconds)
// TODO: add options_ui

function clickBtns() {
    btns = document.getElementsByClassName('snap-timer');
    [].forEach.call(btns, btn => {
        btn.click();
    });
    if (document.hasFocus()) {
        window.setTimeout(clickBtns, 1000);
    } else {
        document.onfocus = clickBtns;
    }   
}


clickBtns();
