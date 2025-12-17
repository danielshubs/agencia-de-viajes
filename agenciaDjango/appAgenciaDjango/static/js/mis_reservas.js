document.addEventListener('DOMContentLoaded', function() {
    const cards = document.querySelectorAll('.reserva-card');
    
    const filterInput = document.getElementById('filter-destino');
    
    if (cards.length === 0) return;
    
    filterInput.addEventListener('input', function() {
        const searchTerm = this.value.toLowerCase().trim();
        
        cards.forEach(card => {  
            const destino = card.getAttribute('data-destino') || 
                           card.querySelector('.destino-text').textContent.toLowerCase();
            
            if (destino.includes(searchTerm) || searchTerm === '') {
                card.style.display = 'grid';
            } else {
                card.style.display = 'none';
            }
        });
    });
    
    cards.forEach(card => {  
        const fechaTexto = card.querySelector('p:nth-child(3)').textContent;
        const fechaMatch = fechaTexto.match(/\d{2}\/\d{2}\/\d{4}/);
        
        if (fechaMatch) {
            const [dia, mes, año] = fechaMatch[0].split('/');
            const fechaViaje = new Date(año, mes - 1, dia);
            const hoy = new Date();
            const diasRestantes = Math.ceil((fechaViaje - hoy) / (1000 * 60 * 60 * 24));
            
            if (diasRestantes > 0 && diasRestantes <= 30) {
                const badge = document.createElement('span');
                badge.textContent = `Faltan ${diasRestantes} días`;
                badge.style.cssText = `
                    background: #ff6b35;
                    color: white;
                    padding: 3px 8px;
                    border-radius: 12px;
                    font-size: 12px;
                    margin-left: 10px;
                `;
                card.querySelector('h3').appendChild(badge);
            }
        }
    });
});