# Recetas App

Aplicación web para la gestión de recetas de cocina, desarrollada con **Flask** y **Flask-AppBuilder** como proyecto de la materia _Taller de Aplicaciones en Internet_.

Permite administrar categorías, ingredientes y recetas, relacionándolos entre sí, y generar un reporte de ingredientes filtrado por categoría.

## Tecnologías usadas

- **Python 3.12**
- **Flask** — framework web
- **Flask-AppBuilder** — generación automática de CRUDs, autenticación y panel de administración
- **SQLAlchemy** — ORM para el manejo de la base de datos
- **MySQL** — base de datos relacional
- **Bootstrap 5** — estilos del reporte

## Estructura de la base de datos

El proyecto maneja 4 tablas principales:

- **categoria**: categorías de recetas (ej. Postre, Entrada)
- **ingrediente**: ingredientes disponibles, con su unidad de medida
- **receta**: recetas, cada una asociada a una categoría
- **receta_ingrediente**: tabla intermedia que resuelve la relación muchos a muchos entre receta e ingrediente, guardando además la cantidad usada

```
categoria (1) ──── (∞) receta (1) ──── (∞) receta_ingrediente (∞) ──── (1) ingrediente
```

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/zergioal/recetas-app.git
cd recetas-app
```

### 2. Crear y activar el entorno virtual

```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Linux / Mac
```

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar la base de datos

Crear una base de datos vacía llamada `app-receta` en MySQL (por ejemplo desde phpMyAdmin con XAMPP).

Revisar que `config.py` tenga la cadena de conexión correcta:

```python
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost:3306/app-receta'
```

### 5. Crear el usuario administrador

```bash
flask fab create-admin
```

### 6. Ejecutar la aplicación

```bash
python run.py
```

La aplicación queda disponible en `http://127.0.0.1:8080`.

## Funcionalidades

- **CRUD de Categorías**: alta, edición y eliminación de categorías.
- **CRUD de Ingredientes**: alta, edición y eliminación de ingredientes con su unidad de medida.
- **CRUD de Recetas**: alta, edición y eliminación de recetas, con gestión de sus ingredientes y cantidades desde la misma pantalla de detalle.
- **Reporte de ingredientes por categoría**: pantalla en _Reportes → Reportes de recetas por categoria_ donde se puede:
  - Seleccionar una categoría y ver únicamente los ingredientes de las recetas que pertenecen a ella.
  - Dejar la selección en blanco para ver los ingredientes de **todas** las recetas.

La consulta recorre la relación `receta_ingrediente → receta` y aplica un filtro condicional por `categoria_id` solo cuando el usuario eligió una categoría:

```python
query = db.session.query(RecetaIngrediente).join(Receta)

if categoria_seleccionada:
    query = query.filter(Receta.categoria_id == categoria_seleccionada)
```

## Autor

Sergio Alcocer — Técnico en Sistemas Informáticos
