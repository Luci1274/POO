// ===== ELEMENTOS DEL DOM =====
// Referencias a los botones y contenedor de métricas
const botonesDolar = document.querySelectorAll('.dolar-btn');
const metricasDiv = document.getElementById('metricas');

// Variable para rastrear el tipo seleccionado
let tipoActual = 'oficial';

// ===== FUNCIÓN PARA OBTENER DATOS DEL DÓLAR =====
// Hace fetch a la API de Flask y muestra los datos
async function obtenerDatos(tipo) {
    try {
        // Mostrar mensaje de carga
        metricasDiv.innerHTML = '<p class="cargando">Cargando datos...</p>';
        
        // Hacer la solicitud a la API
        const response = await fetch(`/api/dolar/${tipo}`);
        
        // Verificar si la respuesta es exitosa
        if (!response.ok) {
            throw new Error(`Error: ${response.status}`);
        }
        
        // Convertir respuesta a JSON
        const datos = await response.json();
        
        // Mostrar los datos
        mostrarDatos(datos, tipo);
        
        console.log(`✓ Datos del dólar ${tipo} obtenidos`);
    } catch (error) {
        console.error(`✗ Error al obtener datos:`, error);
        metricasDiv.innerHTML = `<p class="error">Error al cargar datos: ${error.message}</p>`;
    }
}

// ===== FUNCIÓN PARA REFRESCAR LOS DATOS ACTUALES =====
// Actualiza los datos del tipo de dólar que está seleccionado
function refrescarDatos() {
    console.log(`🔄 Refrescando datos de ${tipoActual}...`);
    obtenerDatos(tipoActual);
}

// ===== FUNCIÓN PARA MOSTRAR DATOS =====
// Formatea y muestra los datos en el DOM
function mostrarDatos(datos, tipo) {
    // Capitalizar el tipo de dólar
    const tipoCapitalizado = tipo.charAt(0).toUpperCase() + tipo.slice(1);
    
    // Construir HTML con los datos
    let html = `<h2>Dólar ${tipoCapitalizado}</h2>`;
    
    // Si es un objeto, mostrar cada propiedad
    if (typeof datos === 'object') {
        html += '<div class="datos-grid">';
        for (const [clave, valor] of Object.entries(datos)) {
            // Formatear la clave (reemplazar guiones bajos por espacios y capitalizar)
            const claveFormateada = clave.replace(/_/g, ' ').toUpperCase();
            html += `
                <div class="dato-item">
                    <span class="dato-label">${claveFormateada}:</span>
                    <span class="dato-valor">${valor}</span>
                </div>
            `;
        }
        html += '</div>';
    } else {
        html += `<p>${datos}</p>`;
    }
    
    metricasDiv.innerHTML = html;
}

// ===== EVENT LISTENERS PARA LOS BOTONES =====
// Agregar click listeners a cada botón
botonesDolar.forEach(boton => {
    boton.addEventListener('click', () => {
        const tipo = boton.dataset.tipo;
        
        // Remover clase active de todos los botones
        botonesDolar.forEach(btn => btn.classList.remove('active'));
        
        // Agregar clase active al botón clickeado
        boton.classList.add('active');
        
        // Obtener y mostrar datos del tipo seleccionado
        tipoActual = tipo;
        obtenerDatos(tipo);
    });
});

// ===== CARGAR DATOS AL INICIAR =====
// Obtener datos del dólar oficial por defecto
obtenerDatos('oficial');

// ===== ACTUALIZACIÓN AUTOMÁTICA =====
// Refrescar datos cada 15 segundos (15000 milisegundos)
setInterval(refrescarDatos, 15000);