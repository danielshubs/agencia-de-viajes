
document.addEventListener('DOMContentLoaded', function() {
    const newsletterPopup = document.getElementById('newsletterPopup');
    const closeButton = document.querySelector('.close-newsletter');
    
    //  Aparecer después de un tiempo
    setTimeout(function() {
        newsletterPopup.style.display = 'block';
    }, 3000); //  después de 3 segundos
    
    
    // Cerrar el popup al hacer clic en la X
    closeButton.addEventListener('click', function() {
        newsletterPopup.style.display = 'none';
    });
    
    //Cerrar al hacer clic fuera del contenido
    window.addEventListener('click', function(e) {
        if (e.target === newsletterPopup) {
            newsletterPopup.style.display = 'none';
        }
    });
});