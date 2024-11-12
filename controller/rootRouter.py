from flask import Blueprint, request
from classes.request.RequestHandler import RequestHandler
import methons.authentication.callbackAuthentication as callbackauth

root_bt = Blueprint("root", __name__)


@root_bt.route("/farmbot", methods=["GET", "POST"])
def root():
    handler = RequestHandler()
    #回调验证请求
    if handler.get_op() == 13:
        handler.print_all()
        return callbackauth.build_callback_body(handler)
    if handler.get_op() == 0:
        handler.print_all()
    return "Request processed."
