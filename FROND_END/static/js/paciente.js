document.addEventListener('DOMContentLoaded', function() {
  // Referencias a elementos de navegación
  const navItems = document.querySelectorAll('.nav-item');
  const sections = document.querySelectorAll('.dashboard-section');
  const toast = document.getElementById('toast');
  const logoutBtn = document.getElementById('logout-btn');
  
  // Manejo de navegación entre secciones
  navItems.forEach(item => {
    item.addEventListener('click', function() {
      const targetId = this.getAttribute('data-target');
      
      // Actualizar navegación activa
      navItems.forEach(nav => nav.classList.remove('active'));
      this.classList.add('active');
      
      // Mostrar sección correspondiente
      sections.forEach(section => {
        section.classList.remove('active');
        if (section.id === targetId) {
          section.classList.add('active');
          
          // Mostrar notificación
          showToast(`Sección ${getNavTitle(targetId)}`, 'Has cambiado a una nueva sección.');
        }
      });
    });
  });
  
  // Manejo de botones de período
  const periodBtns = document.querySelectorAll('.period-btn, .time-btn');
  periodBtns.forEach(btn => {
    btn.addEventListener('click', function() {
      // Encontrar todos los botones del mismo grupo (mismo padre)
      const siblings = this.parentElement.querySelectorAll('button');
      siblings.forEach(sibling => sibling.classList.remove('active'));
      this.classList.add('active');
      
      // Mostrar notificación
      showToast('Período cambiado', `Visualizando datos por ${this.textContent.trim()}.`);
    });
  });
  
  // Manejo de descargar reportes
  const downloadBtns = document.querySelectorAll('.download-btn, .download-report-btn, .btn-download');
  downloadBtns.forEach(btn => {
    btn.addEventListener('click', function(e) {
      e.preventDefault();
      showToast('Descarga iniciada', 'El reporte se está generando y descargando.');
    });
  });
  
  // Manejo de cierre de sesión
  logoutBtn.addEventListener('click', function() {
    showToast('Cerrando sesión', 'Redireccionando al inicio...');
    
    // Redirigir al login después de 1.5 segundos
    setTimeout(() => {
      window.location.href = 'login.html';
    }, 1500);
  });
  
  // Manejo de botones de detalle de sesión
  const detailBtns = document.querySelectorAll('.btn-details');
  detailBtns.forEach(btn => {
    btn.addEventListener('click', function() {
      showToast('Detalles de sesión', 'Cargando información detallada...');
    });
  });
  
  // Manejo de botones de recomendación
  const recBtns = document.querySelectorAll('.btn-start-now, .btn-remind, .btn-playlist, .btn-exercises, .btn-journal');
  recBtns.forEach(btn => {
    btn.addEventListener('click', function() {
      let message = 'Acción en progreso';
      
      if (this.classList.contains('btn-start-now')) {
        message = 'Iniciando actividad recomendada';
      } else if (this.classList.contains('btn-remind')) {
        message = 'Se te recordará más tarde';
      } else if (this.classList.contains('btn-playlist')) {
        message = 'Abriendo playlist recomendada';
      } else if (this.classList.contains('btn-exercises')) {
        message = 'Mostrando ejercicios sugeridos';
      } else if (this.classList.contains('btn-journal')) {
        message = 'Abriendo tu diario emocional';
      }
      
      showToast('Recomendación', message);
    });
  });
  
  // Manejo de la paginación
  const paginationBtns = document.querySelectorAll('.pagination-btn, .page-number');
  paginationBtns.forEach(btn => {
    btn.addEventListener('click', function() {
      if (!this.classList.contains('active')) {
        // Aquí se implementaría la lógica real de paginación
        // Para esta demo solo mostramos un toast
        showToast('Navegando', 'Cargando más resultados...');
      }
    });
  });
  
  // Función para obtener título de sección para notificaciones
  function getNavTitle(sectionId) {
    const titles = {
      'inicio': 'Inicio',
      'comparaciones': 'Comparaciones',
      'historial': 'Historial',
      'recomendaciones': 'Recomendaciones'
    };
    
    return titles[sectionId] || 'Nueva Sección';
  }
  
  // Función para mostrar notificaciones toast
  function showToast(title, message) {
    // Actualizar contenido del toast
    toast.querySelector('.toast-title').textContent = title;
    toast.querySelector('.toast-message').textContent = message;
    
    // Mostrar toast
    toast.classList.remove('hidden');
    
    // Ocultar toast después de 3 segundos
    setTimeout(() => {
      toast.classList.add('hidden');
    }, 3000);
  }
  
  // Simulación de datos en tiempo real para las gráficas
  function initChartAnimations() {
    // Aquí se podrían inicializar bibliotecas de gráficos reales
    // Para esta demo solo tenemos animaciones CSS básicas
    console.log('Inicializando animaciones de gráficos');
  }
  
  // Iniciar animaciones
  initChartAnimations();
  
  // Función para el manejo de búsqueda de sesiones
  const searchBtn = document.querySelector('.search-btn');
  if (searchBtn) {
    searchBtn.addEventListener('click', function() {
      const dateFilter = document.getElementById('date-filter').value;
      const typeFilter = document.getElementById('type-filter').value;
      
      showToast('Búsqueda aplicada', `Filtrando por: ${dateFilter}, ${typeFilter}`);
    });
  }
  
  // Conectar con el login existente
  // Si hay información de usuario del login anterior, la recuperamos
  const userInfo = sessionStorage.getItem('userInfo');
  if (userInfo) {
    try {
      const { username, role } = JSON.parse(userInfo);
      // Actualizar información del perfil si existe
      const profileName = document.querySelector('.profile-name');
      if (profileName) {
        profileName.textContent = username || 'Usuario';
      }
    } catch (e) {
      console.error('Error al recuperar información del usuario:', e);
    }
  }
});


/*simulacion graficos */
document.addEventListener('DOMContentLoaded', function() {
  // Configurar puntos en gráfico de líneas
  
  
  // Interactividad con la leyenda
  document.querySelectorAll('.emotion-label').forEach(label => {
    label.addEventListener('click', function() {
      const emotionClass = this.classList[1];
      const line = document.querySelector(`.emotion-line.${emotionClass}`);
      line.classList.toggle('hidden');
      this.classList.toggle('disabled');
    });
  });
  
  // Tooltips para puntos de datos
  document.querySelectorAll('.data-point').forEach(point => {
    point.addEventListener('mouseenter', function() {
      const tooltip = document.createElement('div');
      tooltip.className = 'tooltip';
      tooltip.textContent = this.getAttribute('data-value');
      this.appendChild(tooltip);
    });
    
    point.addEventListener('mouseleave', function() {
      const tooltip = this.querySelector('.tooltip');
      if (tooltip) tooltip.remove();
    });
  });
});

document.getElementById('logout-btn').addEventListener('click', function () {
  const url = this.getAttribute('data-url');
  window.location.href = url;
});