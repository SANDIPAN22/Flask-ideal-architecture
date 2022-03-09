from flask import Blueprint

core_bp=Blueprint('core_bp',__name__,url_prefix='/core')

@core_bp.route("/")
def core_index():
    return "Hello world From sandipan"