function verificarVideo() {
    const checkInterval = setInterval(() => {
        fetch('verify-video')
            .then(response => response.json())
            .then(data => {
                if (data.video_generado) {
                    clearInterval(checkInterval);
                    // Redirigir a la página de video finalizado
                    window.location.href = 'video-finished';
                }
            })
            .catch(error => {
                console.error('Error al verificar el estado del video:', error);
            });
    }, 1000); // Verifica cada segundo
}

// Iniciar la verificación cuando se cargue la página
//window.onload = verificarVideo;