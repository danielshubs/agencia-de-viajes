// mis_reservas.js - Funcionalidades básicas
document.addEventListener('DOMContentLoaded', function() {
   
    
    // Filtro por destino
    const filterInput = document.createElement('input');
    filterInput.type = 'text';
    filterInput.placeholder = 'Buscar destino...';
    filterInput.style.cssText = `
        padding: 10px;
        margin-bottom: 20px;
        width: 300px;
        max-width: 100%;
    `;
    
    const greeting = document.querySelector('.user-greeting');
    greeting.parentNode.insertBefore(filterInput, greeting.nextElementSibling);

    filterInput.addEventListener('input', function() {
        const searchTerm = this.value.toLowerCase();
        cards.forEach(card => {
            const destino = card.querySelector('p:nth-child(2)').textContent.toLowerCase();
            card.style.display = destino.includes(searchTerm) ? 'flex' : 'none';
        });
    });

    // 3. Contador de días para próximos viajes
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