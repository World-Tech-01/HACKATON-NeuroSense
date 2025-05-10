# HACKATON-NeuroSense
Detector de Estados Emociones En Tiempo Real - Como solución nuestro proyecto propone el desarrollo de una aplicacion web que permita identificar en tiempo real el estado emocional de una persona (felicidad, tristeza, enojo y miedo)
Este proyecto es una aplicación web desarrollada con Flask para la gestión y visualización de datos de electroencefalografía (EEG) en el ámbito de la neurociencia. Ofrece interfaces especializadas para pacientes y profesionales médicos, con herramientas interactivas para el análisis de bandas cerebrales.

🌟 Características Principales
🚀 Módulos Principales
Autenticación de Usuarios

Sistema de inicio de sesión con roles (Paciente/Especialista)

Panel de administración para especialistas

Visualización de Datos

Carrusel interactivo de bandas EEG (Alpha, Beta, Theta, Delta)

Gráficos dinámicos de actividad cerebral

Historial de sesiones y progreso

Gestión de Pacientes

Perfiles completos de pacientes

Registro de observaciones médicas

Sistema de alertas y notificaciones

💻 Tecnologías Utilizadas
Área	Tecnologías
Backend	Python 3, Flask, SQLAlchemy (para futuras implementaciones de base de datos)
Frontend	HTML5, CSS3, JavaScript, Chart.js (para visualización de datos)
Herramientas	Git, Pip, Virtualenv, Flask Development Server
🛠️ Instalación y Configuración
Sigue estos pasos para configurar el proyecto en tu entorno local:

Clonar el repositorio

bash
git clone https://github.com/tu-usuario/neurociencia-frontend.git
cd neurociencia-frontend
Configurar entorno virtual (recomendado)

bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/MacOS
source venv/bin/activate
Instalar dependencias

bash
pip install -r requirements.txt  # Si tienes un archivo requirements.txt
# O instalar Flask manualmente
pip install flask
Ejecutar la aplicación

bash
python app.py
Acceder a la aplicación
Abre tu navegador en: http://localhost:5000

🗃️ Estructura del Proyecto
neurociencia-frontend/
├── app.py                  # Punto de entrada principal de la aplicación
├── config.py               # Configuraciones (claves secretas, etc.)
├── requirements.txt        # Dependencias del proyecto
│
├── static/                 # Archivos estáticos
│   ├── css/                # Hojas de estilo
│   ├── js/                 # Scripts JavaScript
│   └── images/             # Imágenes y assets visuales
│
└── templates/              # Plantillas HTML
    ├── base.html           # Plantilla base
    ├── login.html          # Página de inicio de sesión
    ├── paciente/           # Vistas del paciente
    │   ├── dashboard.html  # Panel principal
    │   └── historial.html  # Historial médico
    ├── especialista/       # Vistas del especialista
    │   ├── panel.html      # Panel de control
    │   └── pacientes.html  # Gestión de pacientes
    └── componentes/        # Componentes reutilizables
        └── graficos.html   # Componentes de gráficos EEG
👥 Equipo de Desarrollo
Nombre	Rol	Contacto
Aaron Néstor Choque Condori	Backend Developer	vantas1412@gmail.com
Joel Hernan Tancara Suñagua	Frontend Developer	tancarajoe@gmail.com
Fidel Angel Rojas Condori	Data Analyst	rojascondorifidelangel@gmail.com
Carlos Eduardo Reyes Barja	UI/UX Designer	kaereyes0@gmail.com
Esther Sara Copa Quispe	Documentation	e.sara.cq.25@gmail.com
🤝 Cómo Contribuir
¡Agradecemos las contribuciones! Para colaborar:

Haz un fork del proyecto

Crea una rama con tu feature (git checkout -b feature/AmazingFeature)

Haz commit de tus cambios (git commit -m 'Add some AmazingFeature')

Haz push a la rama (git push origin feature/AmazingFeature)

Abre un Pull Request

📄 Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.

📧 Contacto
Para preguntas o sugerencias, contacta al equipo de desarrollo o abre un issue en el repositorio.
