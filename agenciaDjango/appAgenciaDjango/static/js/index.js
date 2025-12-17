document.addEventListener('DOMContentLoaded', function() {
    
    
    // NEWSLETTER - Simple
    const popup = document.getElementById('newsletterPopup');
    if (popup) {
        // Mostrar una vez al día
        const lastShow = localStorage.getItem('newsLastShow');
        const today = new Date().toDateString();
        
        if (lastShow !== today) {
            setTimeout(() => {
                popup.style.display = 'flex';
                localStorage.setItem('newsLastShow', today);
            }, 2000);
        }
        
        // Cerrar
        document.querySelector('.close-newsletter').onclick = () => {
            popup.style.display = 'none';
        };
    }
});