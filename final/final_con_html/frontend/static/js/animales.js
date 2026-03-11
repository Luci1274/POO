// ===== ELEMENTOS DEL DOM =====
// Referencias a las imágenes en el HTML
const dogImage = document.getElementById('dog-image');
const catImage = document.getElementById('cat-image');

// ===== FUNCIÓN PARA OBTENER IMÁGENES =====
// Hace fetch a la API de Flask y actualiza las imágenes
async function obtenerImagenes() {
    try {
        // Hacer la solicitud a la API
        const response = await fetch('/api/imagenes/');
        
        // Verificar si la respuesta es exitosa
        if (!response.ok) {
            throw new Error(`Error: ${response.status}`);
        }
        
        // Convertir respuesta a JSON
        const datos = await response.json();
        
        // Actualizar las imágenes con las URLs obtenidas
        dogImage.src = datos.dog_image;
        catImage.src = datos.cat_image;
        
        console.log('✓ Imágenes actualizadas correctamente');
    } catch (error) {
        console.error('✗ Error al obtener imágenes:', error);
    }
}

// ===== LLAMADAS A LA FUNCIÓN =====
// Obtener imágenes al cargar la página
obtenerImagenes();

// Obtener nuevas imágenes cada 15 segundos (15000 milisegundos)
setInterval(obtenerImagenes, 15000);
