from flask import Blueprint, request
from classes.request.requestHandler import RequestHandler
import methons.authentication.callbackAuthentication as callbackauth

root_bt = Blueprint("root", __name__)


@root_bt.route("/fishbot", methods=["GET", "POST"])
def root():
    handler = RequestHandler()
    print(handler.get_op())
    #回调验证请求
    if handler.get_op() == 13:
        return callbackauth.build_callback_body(handler)
    if handler.get_op() == 0:
        handler.print_all()
    return "Request processed."
