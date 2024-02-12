from flask import render_template

def erreur(app):
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('erreur/500.html', sous_titre="Erreur interne du serveur", error_message=str(e)), 500
