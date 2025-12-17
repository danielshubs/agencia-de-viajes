// Newsletter CORREGIDO
document.addEventListener('DOMContentLoaded', function() {
    const popup = document.getElementById('newsletterPopup');
    
    if (popup) {
        // Verificar si ya se mostró hoy
        const lastShown = localStorage.getItem('newsletterShown');
        const today = new Date().toDateString();
        
        // Solo mostrar si NO se mostró hoy
        if (lastShown !== today) {
            setTimeout(() => {
                popup.style.display = 'flex';
                // Guardar que se mostró HOY
                localStorage.setItem('newsletterShown', today);
            }, 2000);
        }
        
        // Cerrar popup
        document.querySelector('.close-newsletter').onclick = function() {
            popup.style.display = 'none';
        };
        
        // Cerrar al hacer clic fuera
        popup.onclick = function(event) {
            if (event.target === popup) {
                popup.style.display = 'none';
            }
        };
    }
});