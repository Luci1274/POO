// ===== ELEMENTOS DEL DOM =====
const inputId = document.getElementById('input-id');
const btnBuscar = document.getElementById('btn-buscar');
const carruselContainer = document.getElementById('carrusel-container');
const carrusel = document.getElementById('carrusel');
const detalleContainer = document.getElementById('detalle-container');
const detalleJuego = document.getElementById('detalle-juego');
const btnVolver = document.getElementById('btn-volver');
const maxIdSpan = document.getElementById('max-id');

// Variables de estado
let juegosActuales = [];
let indiceActual = 0;
let intervaloRotacion = null;

// ===== OBTENER ID MÁXIMO =====
async function obtenerIdMaximo() {
    try {
        const response = await fetch('/api/juegos/max-id/');
        const datos = await response.json();
        maxIdSpan.textContent = datos.max_id;
        inputId.max = datos.max_id;
    } catch (error) {
        console.error('Error al obtener ID máximo:', error);
    }
}

// ===== OBTENER JUEGOS ALEATORIOS =====
async function cargarJuegosAleatorios() {
    try {
        carrusel.innerHTML = '<p class="cargando">Cargando juegos...</p>';
        const response = await fetch('/api/juegos/');
        
        if (!response.ok) {
            throw new Error('Error al cargar juegos');
        }
        
        juegosActuales = await response.json();
        indiceActual = 0;
        mostrarJuegosCarrusel();
        console.log('✓ Juegos aleatorios cargados');
    } catch (error) {
        console.error('✗ Error:', error);
        carrusel.innerHTML = `<p class="error">Error al cargar juegos</p>`;
    }
}

// ===== MOSTRAR JUEGOS EN CARRUSEL =====
function mostrarJuegosCarrusel() {
    if (juegosActuales.length === 0) return;
    
    carrusel.innerHTML = '';
    
    juegosActuales.forEach((juego, index) => {
        const card = document.createElement('div');
        card.className = 'juego-card';
        
        card.innerHTML = `
            <img src="${juego.thumbnail}" alt="${juego.title}" class="juego-img">
            <h3>${juego.title}</h3>
            <p class="genero">${juego.genre}</p>
            <p class="plataforma">${juego.platform}</p>
            <button class="btn-detalles" data-id="${juego.id}">Ver detalles</button>
        `;
        
        card.querySelector('.btn-detalles').addEventListener('click', () => {
            obtenerDetallesJuego(juego.id);
        });
        
        carrusel.appendChild(card);
    });
}

// ===== OBTENER DETALLES DEL JUEGO =====
async function obtenerDetallesJuego(gameId) {
    try {
        detalleJuego.innerHTML = '<p class="cargando">Cargando detalles...</p>';
        const response = await fetch(`/api/juegos/${gameId}`);
        
        if (!response.ok) {
            throw new Error('Juego no encontrado');
        }
        
        const juego = await response.json();
        mostrarDetallesJuego(juego);
        
        // Cambiar vista
        carruselContainer.style.display = 'none';
        detalleContainer.style.display = 'block';
        
        console.log('✓ Detalles del juego obtenidos');
    } catch (error) {
        console.error('✗ Error:', error);
        detalleJuego.innerHTML = `<p class="error">Error: ${error.message}</p>`;
    }
}

// ===== MOSTRAR DETALLES DEL JUEGO =====
function mostrarDetallesJuego(juego) {
    const plataformas = juego.platform || 'No especificada';
    const generos = juego.genre || 'No especificado';
    
    detalleJuego.innerHTML = `
        <div class="detalle-contenido">
            <img src="${juego.thumbnail}" alt="${juego.title}" class="detalle-img">
            <div class="detalle-info">
                <h2>${juego.title}</h2>
                
                <div class="detalle-item">
                    <span class="label">📱 Plataformas:</span>
                    <span class="valor">${plataformas}</span>
                </div>
                
                <div class="detalle-item">
                    <span class="label">🎮 Género:</span>
                    <span class="valor">${generos}</span>
                </div>
                
                <div class="detalle-item">
                    <span class="label">📝 Descripción:</span>
                    <p class="descripcion">${juego.short_description || 'Sin descripción disponible'}</p>
                </div>
                
                ${juego.release_date ? `
                <div class="detalle-item">
                    <span class="label">📅 Fecha de lanzamiento:</span>
                    <span class="valor">${juego.release_date}</span>
                </div>
                ` : ''}
            </div>
        </div>
    `;
}

// ===== VOLVER AL CARRUSEL =====
function volverAlCarrusel() {
    detalleContainer.style.display = 'none';
    carruselContainer.style.display = 'block';
    inputId.value = '';
}

// ===== ROTAR JUEGOS CADA 30 SEGUNDOS =====
function iniciarRotacion() {
    intervaloRotacion = setInterval(() => {
        if (juegosActuales.length > 0) {
            console.log('🔄 Rotando juegos...');
            mostrarJuegosCarrusel();
        }
    }, 30000); // 30 segundos
}

// ===== EVENT LISTENERS =====
// Botón buscar
btnBuscar.addEventListener('click', () => {
    const id = parseInt(inputId.value);
    
    if (isNaN(id) || id < 1) {
        alert('Por favor ingresa un ID válido');
        return;
    }
    
    obtenerDetallesJuego(id);
});

// Enter en el input
inputId.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        btnBuscar.click();
    }
});

// Botón volver
btnVolver.addEventListener('click', volverAlCarrusel);

// ===== INICIALIZAR =====
obtenerIdMaximo();
cargarJuegosAleatorios();
iniciarRotacion();

console.log('✓ Página de juegos cargada');
