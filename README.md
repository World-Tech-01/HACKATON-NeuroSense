# 🧠 HACKATON – NeuroSense

*Detector de Estados Emocionales en Tiempo Real*

Como solución, nuestro proyecto propone el desarrollo de una *aplicación web* que permite *identificar en tiempo real* el estado emocional de una persona (felicidad, tristeza, enojo y miedo).

Este sistema está diseñado para el análisis y visualización de datos de *electroencefalografía (EEG), ofreciendo interfaces especializadas para **pacientes* y *profesionales médicos*, con herramientas interactivas para el estudio de bandas cerebrales.


## 🌟 Características Principales

### 🚀 Módulos Principales

#### 🔐 Autenticación de Usuarios

* Sistema de inicio de sesión con roles: *Paciente / Especialista*
* Panel de administración exclusivo para especialistas

#### 📊 Visualización de Datos

* Carrusel interactivo de bandas EEG (*Alpha, Beta, Theta, Delta*)
* Gráficos dinámicos de actividad cerebral
* Historial de sesiones y progreso

#### 👤 Gestión de Pacientes

* Perfiles completos de pacientes
* Registro de observaciones médicas
* Sistema de alertas y notificaciones


## 💻 Tecnologías Utilizadas

| Área             | Tecnologías                                              |
| ---------------- | -------------------------------------------------------- |
| *Backend*      | Python 3, Flask, SQLAlchemy (para futuras integraciones) |
| *Frontend*     | HTML5, CSS3, JavaScript, Chart.js                        |
| *Herramientas* | Git, Pip, Virtualenv, Flask Development Server           |


## 🛠 Instalación y Configuración

### 1. Clonar el repositorio

bash
git clone https://github.com/tu-usuario/neurociencia-frontend.git
cd neurociencia-frontend


### 2. Configurar entorno virtual (recomendado)

bash
python -m venv venv

# Para Windows
venv\Scripts\activate

# Para Linux / macOS
source venv/bin/activate


### 3. Instalar dependencias

bash
pip install -r requirements.txt
# O instalar Flask manualmente si no tienes el archivo
pip install flask


### 4. Ejecutar la aplicación

bash
python app.py


### 5. Acceder a la aplicación

Abre tu navegador en: [http://localhost:5000](http://localhost:5000)


## 🗃 Estructura del Proyecto

´´´
neurociencia-frontend/
├── app.py                  # Punto de entrada principal de la aplicación
├── config.py               # Configuración general (claves, etc.)
├── requirements.txt        # Lista de dependencias
├── static/                 # Archivos estáticos
│   ├── css/                # Estilos CSS
│   ├── js/                 # Scripts JS
│   └── images/             # Imágenes y recursos visuales
├── templates/              # Plantillas HTML
│   ├── base.html           # Plantilla base
│   ├── login.html          # Página de inicio de sesión
│   ├── paciente/           # Vistas del paciente
│   │   ├── dashboard.html
│   │   └── historial.html
│   ├── especialista/       # Vistas del especialista
│   │   ├── panel.html
│   │   └── pacientes.html
│   └── componentes/
│       └── graficos.html   # Componentes reutilizables (gráficos EEG)
´´´

## 👥 Equipo de Desarrollo

| Nombre                      | Rol                | Contacto                                                                    |
| --------------------------- | ------------------ | --------------------------------------------------------------------------- |
| Aaron Néstor Choque Condori | Data Analyst       | [vantas1412@gmail.com](mailto:vantas1412@gmail.com)                         |
| Joel Hernan Tancara Suñagua | Frontend Developer | [tancarajoe@gmail.com](mailto:tancarajoe@gmail.com)                         |
| Carlos Eduardo Reyes Barja  | Backend Developer  | [kaereyes0@gmail.com](mailto:kaereyes0@gmail.com)                           |
| Fidel Angel Rojas Condori   | UI/UX Designer     | [rojascondorifidelangel@gmail.com](mailto:rojascondorifidelangel@gmail.com) |
| Esther Sara Copa Quispe     | UI/UX Designer     | [e.sara.cq.25@gmail.com](mailto:e.sara.cq.25@gmail.com)                     |



## 🤝 Cómo Contribuir

1. Haz un *fork* del proyecto
2. Crea una rama para tu feature:

   bash
   git checkout -b feature/NuevaFuncionalidad
   
3. Realiza tus cambios y haz commit:

   bash
   git commit -m "Agrega nueva funcionalidad"
   
4. Sube tu rama al repositorio:

   bash
   git push origin feature/NuevaFuncionalidad
   
5. Abre un *Pull Request*



## 📄 Licencia

Este proyecto está bajo la *licencia MIT*. Consulta el archivo LICENSE para más detalles.


## 📧 Contacto

¿Preguntas o sugerencias?
Contacta al equipo o abre un issue en el repositorio.
