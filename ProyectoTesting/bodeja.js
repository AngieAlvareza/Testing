class Bodega {
    constructor() {
      // Aquí podrías inicializar propiedades o conectarte a una base de datos
    }
  
    buscarProductos(sucursal, categoria, vino) {
      // Esta función simula una búsqueda en la base de datos
      console.log('Realizando búsqueda de productos:');
      console.log('Sucursal:', sucursal);
      console.log('Categoría:', categoria);
      console.log('Vino:', vino);
      // Aquí podrías hacer una solicitud a tu backend para obtener los resultados de la búsqueda
    }
  
    buscarSucursales(sucursal, categoria, vino) {
      // Esta función simula una búsqueda en la base de datos
      console.log('Realizando búsqueda de sucursales:');
      console.log('Sucursal:', sucursal);
      console.log('Categoría:', categoria);
      console.log('Vino:', vino);
      // Aquí podrías hacer una solicitud a tu backend para obtener los resultados de la búsqueda
    }
  
    agregarFavorito(item) {
      // Esta función podría agregar un ítem a la lista de favoritos
      console.log('Agregando a favoritos:', item);
      // Aquí podrías almacenar el ítem en la lista de favoritos del usuario (por ejemplo, en el almacenamiento local del navegador)
    }
  }
  
  // Función para manejar el envío del formulario de búsqueda
  function handleSearch(event) {
    event.preventDefault(); // Evita que el formulario se envíe
  
    // Captura los valores de los campos de búsqueda
    const sucursal = document.getElementById('input-1').value;
    const categoria = document.getElementById('input-2').value;
    const vino = document.getElementById('input-3').value;
  
    // Crea una instancia de la clase Bodega
    const bodega = new Bodega();
  
    // Realiza la búsqueda de productos y sucursales
    bodega.buscarProductos(sucursal, categoria, vino);
    bodega.buscarSucursales(sucursal, categoria, vino);
  }
  
  // Captura el formulario de búsqueda
  const searchForm = document.querySelector('.hero-form');
  
  // Agrega un evento de escucha para el envío del formulario
  searchForm.addEventListener('submit', handleSearch);
  