const onBtnClick = function() {
    // kun callbackin tekee perinteisesti function()-avainsanalla, this viittaa aina siihen
    // dom-elementtiin, johon eventti on kiinnitetty
    // vrt fat arrow syntax () => {}
    const button = this;
    let count = button.innerText;
    //"0" + 1
    // 01
    count = parseInt(count)
    count = count + 1;
    button.innerText = count;
}

document.addEventListener('DOMContentLoaded', () => {

    const btn = document.querySelector('#btn');
    btn.addEventListener('click', onBtnClick)

    


})
