from flask import request
from app.extensions import db
from flask_appbuilder import BaseView, expose
from app.models.categoria import Categoria
from app.models.receta import Receta
from app.models.receta_ingrediente import RecetaIngrediente


class ReporteSimpleView(BaseView):

    @expose("/", methods=["GET", "POST"])
    def list(self):
        # 1. Traemos todas las categorias para llenar el <select> del formulario
        categorias = db.session.query(Categoria).all()

        # 2. Capturamos lo que el usuario seleccionó en el formulario (puede venir vacío)
        categoria_seleccionada = request.form.get('cat_id')

        # 3. Consulta base: RecetaIngrediente unido con Receta
        #    (es el camino para llegar de categoria -> receta -> receta_ingrediente -> ingrediente)
        query = db.session.query(RecetaIngrediente).join(Receta)

        # 4. Si el usuario eligió una categoria, filtramos por ella.
        #    Si no eligió nada (cadena vacia o None), no se aplica filtro y se traen todos.
        if categoria_seleccionada:
            query = query.filter(Receta.categoria_id == categoria_seleccionada)

        ingredientes_filtrados = query.all()

        return self.render_template(
            "reportes.html",
            categorias=categorias,
            id_categoria=categoria_seleccionada,
            ingredientes=ingredientes_filtrados
        )