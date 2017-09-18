from flask_admin import BaseView, expose
from flask import Blueprint

adminRoute = Blueprint(
    'admin',
    __name__,
    url_prefix='/admin',
    template_folder='templates',
    static_folder='static'
)

class SlaView(BaseView):
    """View function of Flask-Admin for Custom page."""

    @expose('/')
    def index(self):
        return self.render('sla.html')

    @expose('/sla')
    def second_page(self):
        return self.render('sla.html')