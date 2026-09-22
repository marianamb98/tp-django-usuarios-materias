# Actividad Práctica - Proyecto Django

Este proyecto consiste en una aplicación web desarrollada con Django que incluye autenticación personalizada, gestión de perfiles de usuario y listado paginado de materias mediante Vistas Basadas en Clases (CBV).

---

## 🛠️ Estructura del Proyecto

```text
proyecto_programacion/
├── applications/
│   ├── templates/
│   │   ├── usuarios/
│   │   │   ├── login.html
│   │   │   ├── perfil.html
│   │   │   └── signup.html
│   │   └── materias/
│   │       └── materia_list.html
│   └── usuarios/
│       ├── forms.py
│       ├── models.py
│       ├── urls.py
│       └── views.py
├── ecommerce_project/
│   ├── settings.py
│   └── urls.py
├── static/
│   └── css/
│       └── base.css
├── manage.py
└── requirements.txt