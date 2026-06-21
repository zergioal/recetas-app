from flask_appbuilder import CompactCRUDMixin, ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface
from app.models.receta import Receta
from app.models.receta_ingrediente import RecetaIngrediente
class RecetaIngredienteView(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(RecetaIngrediente)
    list_columns = ['ingrediente.nombre', "cantidad", "ingrediente.unidad_medida"]
    # 'receta' tiene que estar en add/edit_columns para que Flask-AppBuilder
    # pueda detectar la relacion con Receta y autocompletar el receta_id
    # cuando se agrega un ingrediente desde la pantalla "Mostrar" de una receta.
    add_columns = ['receta', 'ingrediente', "cantidad"]
    edit_columns = ['receta', 'ingrediente', "cantidad"]
    
class RecetaModelView (ModelView):
    datamodel= SQLAInterface(Receta)
    
    related_views = [RecetaIngredienteView]
    
    list_columns = ['nombre', "categoria.nombre", "descripcion"]
    add_columns = ['nombre', "categoria", "descripcion", "instrucciones"]
    edit_columns = ['nombre', "categoria", "descripcion", "instrucciones"]