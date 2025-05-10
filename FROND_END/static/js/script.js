document.addEventListener('DOMContentLoaded', function() {
    // Referencias a elementos
    const loginForm = document.getElementById('login-form');
    const loginScreen = document.getElementById('login-screen');
    const configScreen = document.getElementById('config-screen');
    const monitoringScreen = document.getElementById('monitoring-screen');
    const toast = document.getElementById('toast');
    const sessionDuration = document.getElementById('session-duration');
    const durationValue = document.getElementById('duration-value');
    
    // Evento de inicio de sesión
    loginForm.addEventListener('submit', function(event) {
      event.preventDefault();
      
      // Mostrar notificación
      toast.classList.remove('hidden');
      
      // Ocultar notificación después de 3 segundos
      setTimeout(() => {
        toast.classList.add('hidden');
      }, 3000);
      
      // Cambiar a pantalla de configuración
      loginScreen.classList.add('hidden');
      configScreen.classList.remove('hidden');
    });
    
    // Actualizar valor del slider de duración
    sessionDuration.addEventListener('input', function() {
      durationValue.textContent = this.value + ' minutos';
    });
    
    // Manejo de opciones seleccionables
    const deviceOptions = document.querySelectorAll('.device-option');
    deviceOptions.forEach(option => {
      option.addEventListener('click', function() {
        deviceOptions.forEach(opt => opt.classList.remove('selected'));
        this.classList.add('selected');
      });
    });
    
    const monitorOptions = document.querySelectorAll('.monitor-option');
    monitorOptions.forEach(option => {
      option.addEventListener('click', function() {
        monitorOptions.forEach(opt => opt.classList.remove('selected'));
        this.classList.add('selected');
      });
    });
    
    // Botón para iniciar monitoreo
    const startButton = document.querySelector('.config-card .btn-primary');
    startButton.addEventListener('click', function() {
      configScreen.classList.add('hidden');
      monitoringScreen.classList.remove('hidden');
      
      // Mostrar notificación
      toast.querySelector('.toast-title').textContent = 'Sesión iniciada';
      toast.querySelector('.toast-message').textContent = 'Monitoreo en tiempo real activado.';
      toast.classList.remove('hidden');
      
      setTimeout(() => {
        toast.classList.add('hidden');
      }, 3000);
    });
    
    // Botón para volver desde configuración al login
    const backButton = document.querySelector('.config-card .btn-secondary');
    backButton.addEventListener('click', function() {
      configScreen.classList.add('hidden');
      loginScreen.classList.remove('hidden');
    });
    
    // Botones de sesiones recientes
    const sessionButtons = document.querySelectorAll('.btn-session');
    sessionButtons.forEach(button => {
      button.addEventListener('click', function() {
        loginScreen.classList.add('hidden');
        monitoringScreen.classList.remove('hidden');
        
        // Mostrar notificación
        toast.querySelector('.toast-title').textContent = 'Sesión cargada';
        toast.querySelector('.toast-message').textContent = 'Cargando datos de sesión anterior.';
        toast.classList.remove('hidden');
        
        setTimeout(() => {
          toast.classList.add('hidden');
        }, 3000);
      });
    });
    
    // Botón para finalizar sesión
    const endSessionButton = document.querySelector('.btn-danger');
    endSessionButton.addEventListener('click', function() {
      monitoringScreen.classList.add('hidden');
      loginScreen.classList.remove('hidden');
      
      // Mostrar notificación
      toast.querySelector('.toast-title').textContent = 'Sesión finalizada';
      toast.querySelector('.toast-message').textContent = 'Los datos han sido guardados correctamente.';
      toast.classList.remove('hidden');
      
      setTimeout(() => {
        toast.classList.add('hidden');
      }, 3000);
    });
  });