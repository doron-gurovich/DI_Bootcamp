import flask

from app import app


@app.errorhandler(404)
def error_404(error):
	return flask.render_template('errors/404_error.html'), 404


@app.errorhandler(400)
def error_400(error):
	return flask.render_template('errors/400_bad_color.html'), 400


@app.errorhandler(500)
def error_500(error):
	return flask.render_template('errors/500_internal_server_error.html'), 500
