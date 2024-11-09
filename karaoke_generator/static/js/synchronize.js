const audio_element = document.getElementById('audio');
const source_element = document.querySelector('source');
const audio_source = source_element.getAttribute('src');

let palabras = document.querySelectorAll('.word');
let tiempos = [];
let indice = 0;


function enviar_json(json) {
    const csrftoken = getCookie('csrftoken');

    datos = {
        "musica": audio_source,
        "image":image_path,
        "lyrics": json,
    }
    fetch('generating-karaoke', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken  
        },
        body: JSON.stringify(datos) // Convierte el objeto JSON a string
    }).then(response => {
        // Verifica si la respuesta está bien formateada como JSON
        if (!response.ok) {
            throw new Error(`Error en la respuesta: ${response.status}`);
        }
        return response.json();  // Convertir la respuesta a JSON
    })
        .then(data => {
            console.log('Datos enviados correctamente:', data);

            // Redirigir o manejar la respuesta
            if (data.status === "success") {
                window.location.href = 'finished';
            } else {
                console.error('Error en la respuesta:', data.message);
            }
        })
        .catch(error => {
            console.error('Error al enviar los datos:', error);
        });
}


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}




function start() {
    let boton_sincro = document.getElementById('synchronize')
    boton_sincro.disabled = true
    audio_element.currentTime = 0;
    audio_element.play();
    console.log(palabras)
    document.addEventListener('keydown', function (event) {
        if (event.key == 'Enter') {
            if (indice < palabras.length) {
                let tiempoActual = audio.currentTime;

                tiempos.push({
                    "palabra": palabras[indice].textContent,
                    "tiempo": tiempoActual
                });

                palabras[indice].style.color = 'red'; // Marca la paabra sincronizada
                indice++;
            } else {
                const interface = document.getElementById('synchro')
                const loader = document.getElementById('loader')

                interface.style.display = 'none';
                loader.style.display = 'flex'
                
                array = JSON.stringify(tiempos)
                enviar_json(array)

                //console.log(array)
            }
        }
    });
}

