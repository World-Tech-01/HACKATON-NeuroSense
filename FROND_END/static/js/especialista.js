document.addEventListener('DOMContentLoaded', function() {
    // Referencias a elementos de navegación
    const navItems = document.querySelectorAll('.nav-item');
    const sections = document.querySelectorAll('.dashboard-section');
    const toast = document.getElementById('toast');
    const logoutBtn = document.getElementById('logout-btn');
    const addPatientBtn = document.getElementById('add-patient-btn');
    const patientSearchInput = document.getElementById('patient-search');
    const evaluationPatientSelect = document.getElementById('evaluation-patient-select');
    const assignSessionBtn = document.getElementById('assign-session-btn');
    
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
    
    // Función para agregar nuevo paciente
    if (addPatientBtn) {
      addPatientBtn.addEventListener('click', function() {
        showToast('Añadir Paciente', 'Formulario de registro abierto.');
        
        // Aquí se abriría un modal o se redirigía al formulario de registro
        // Para esta demo solo mostramos un toast
      });
    }
    
    // Búsqueda de pacientes
    if (patientSearchInput) {
      patientSearchInput.addEventListener('input', function() {
        const searchTerm = this.value.toLowerCase();
        const patientRows = document.querySelectorAll('.patient-row');
        
        patientRows.forEach(row => {
          const patientName = row.querySelector('.patient-name').textContent.toLowerCase();
          
          if (patientName.includes(searchTerm)) {
            row.style.display = '';
          } else {
            row.style.display = 'none';
          }
        });
      });
    }
    
    // Manejo de botones de historial de paciente
    const historyBtns = document.querySelectorAll('.patient-history-btn');
    historyBtns.forEach(btn => {
      btn.addEventListener('click', function() {
        const patientName = this.closest('.patient-row').querySelector('.patient-name').textContent;
        showToast('Historial de Paciente', `Cargando historial de ${patientName}`);
        
        // Cambiar a la sección de historial y cargar datos del paciente
        navItems.forEach(nav => {
          if (nav.getAttribute('data-target') === 'historial') {
            nav.click();
          }
        });
      });
    });
    
    // Cambio de paciente en evaluación
    if (evaluationPatientSelect) {
      evaluationPatientSelect.addEventListener('change', function() {
        const patientName = this.options[this.selectedIndex].text;
        showToast('Evaluación', `Cargando datos de ${patientName}`);
        
        // Aquí se cargarían los datos del paciente seleccionado
        // Para esta demo solo actualizamos algunos elementos visuales
        document.querySelectorAll('.eeg-chart, .emotion-percentage').forEach(el => {
          // Simular actualización de datos
          el.classList.add('loading');
          setTimeout(() => {
            el.classList.remove('loading');
          }, 1000);
        });
      });
    }
    
    // Asignar nueva sesión a paciente
    if (assignSessionBtn) {
      assignSessionBtn.addEventListener('click', function() {
        showToast('Nueva Sesión', 'Sesión asignada correctamente');
      });
    }
    
    // Manejo de cierre de sesión
    if (logoutBtn) {
      logoutBtn.addEventListener('click', function() {
        showToast('Cerrando sesión', 'Redireccionando al inicio...');
        
        // Redirigir al login después de 1.5 segundos
        setTimeout(() => {
          window.location.href = 'emotion-insight.html';
        }, 1500);
      });
    }
    
    // Manejo de botones de período
    const periodBtns = document.querySelectorAll('.period-btn');
    periodBtns.forEach(btn => {
      btn.addEventListener('click', function() {
        const siblings = this.parentElement.querySelectorAll('button');
        siblings.forEach(sibling => sibling.classList.remove('active'));
        this.classList.add('active');
        
        showToast('Período cambiado', `Visualizando datos por ${this.textContent.trim()}.`);
      });
    });
    
    // Manejo de botones de descarga de reportes
    const downloadBtns = document.querySelectorAll('.download-btn');
    downloadBtns.forEach(btn => {
      btn.addEventListener('click', function(e) {
        e.preventDefault();
        showToast('Descarga iniciada', 'El reporte se está generando y descargando.');
      });
    });
    
    // Función para obtener título de sección para notificaciones
    function getNavTitle(sectionId) {
      const titles = {
        'inicio': 'Inicio',
        'analisis': 'Análisis de Pacientes',
        'evaluacion': 'Evaluación',
        'historial': 'Historial de Pacientes',
        'trastornos': 'Trastornos Mentales'
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
  });