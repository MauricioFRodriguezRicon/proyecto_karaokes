let audio = document.getElementById('audio');
let palabras = document.querySelectorAll('.word');
let tiempos = [];
let indice = 0;

function start() {
    audio.play();
    document.addEventListener('keydown', function(event) {
        if (event.key === 'Enter') {
            let tiempoActual = audio.currentTime;
            tiempos.push({
                palabra: palabras[indice].textContent,
                tiempo: tiempoActual
            });
            palabras[indice].style.color = 'red'; // Marca la palabra sincronizada
            indice++;
            console.log(tiempos)
            console.log(indice)
        }
    });

}