from flask import Flask, Response, request
from datetime import datetime
import json
from players import NbaPlayerResource
from flask_cors import CORS

# Create the Flask application object.
application = Flask(__name__,
                    static_url_path='/',
                    static_folder='static/class-ui/',
                    template_folder='web/templates')

CORS(application)


@application.get("/stats/player")
def get_player():
    result = NbaPlayerResource.get_players()
    if result:
        rsp = Response(json.dumps(result), status=200,
                       content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp
    # t = str(datetime.now())
    # msg = {
    #     "name": "F22-Starter-Microservice",
    #     "health": "Good",
    #     "at time": t
    # }

    # # DFF TODO Explain status codes, content type, ... ...
    # result = Response(json.dumps(msg), status=200, content_type="application/json")

    # return result


@application.route("/stats/player/<id>", methods=["GET"])
def get_student_by_id(id):

    result = NbaPlayerResource.get_by_key(id)

    if result:
        rsp = Response(json.dumps(result), status=200,
                       content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


if __name__ == "__main__":
    application.run(host="0.0.0.0", port=5000)
