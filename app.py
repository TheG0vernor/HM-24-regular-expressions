import os
from flask import Flask, request, Response, abort

from constants import DATA_DIR
from services import filter_in_cmd1, map_in_cmd1, sort_in_cmd1, limit_in_cmd1, regex_in_cmd1

app = Flask(__name__)


@app.post("/perform_query/")
def perform_query() -> Response:
    try:
        cmd1 = request.args['cmd1']
        value1 = request.args['value1']
        cmd2 = request.args['cmd2']
        value2 = request.args['value2']
        file_name = request.args['file_name']
        log_file = os.path.join(DATA_DIR, file_name)
        if not os.path.isfile(log_file):
            abort(400, 'несоответствие имени файла')
        elif cmd1 == 'filter':
            return Response(filter_in_cmd1(cmd2, value1, value2))
        elif cmd1 == 'map':
            return Response(map_in_cmd1(cmd2, value1, value2))
        elif cmd1 == 'sort':
            return Response(sort_in_cmd1(cmd2, value1, value2))
        elif cmd1 == 'limit':
            return Response(limit_in_cmd1(cmd2, value1, value2))
        elif cmd1 == 'regex':
            return Response(regex_in_cmd1(cmd2, value1, value2))
        else:
            abort(400, 'введены недопустимые данные')
    except Exception as e:
        abort(400, e)
    return app.response_class('', content_type="text/plain")


if __name__ == '__main__':
    app.run()
