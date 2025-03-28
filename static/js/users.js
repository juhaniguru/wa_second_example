
// 1 varmista, että sisältö on kokonaan latautunut

document.addEventListener('DOMContentLoaded', function() {

    // 2. keksitään joku tapa, jolla saadaan evenlistener kiinni Poisto-formiin
    // jokaisen poistoformin css-class on button-form. Käytetään querySelectoria
    // css-classin querySelector on piste (.)

    const forms = document.querySelectorAll('.button-form')
    forms.forEach(function(form) {

        // 3 laitetaan jokaiseen formiin kiinni eventlistener submit eventiin
        // eventlistener-funktio saa parametrinaan sen eventin, johon se on kiinnitetty
        form.addEventListener('submit', async function(event) {
            const currentForm = this;
            // event on submit
            // estetään perinteinen formin lähetys, jotta koko sivu ei päivity kerralla
            event.preventDefault()
            
            const requestData = new FormData(currentForm)
            const response = await fetch('http://localhost:3001/delete-user', {
                method: 'POST',
                body: requestData
            })

            if(!response.ok) {
                console.log('tapahtui virhe')
                return
            } 

            const responseBody = await response.text();
            currentForm.parentNode.parentNode.remove()
            
            







        })

    })
});