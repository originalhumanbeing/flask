from flask import Flask, request, jsonify

from tasks import add_task
app = Flask(__name__)


@app.route('/')
def index():
    return 'My First Flask Web Site!'


@app.route('/greeting/<username>')
def hello_there(username):
    return "hello %s" % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return "your post_id is %s" % post_id


@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    task = add_task.add_task.delay(a, b)
    return f"<a href=\"http://localhost:5000/status/{str(task.id)}\">{str(task.id)}</a>"


@app.route('/status/<task_id>')
def taskstatus(task_id):
    task = add_task.add_task.AsyncResult(task_id)
    if task.state == 'PENDING':
        # job did not start yet
        response = {
            'state': task.state,
            'current': 0,
            'total': 1,
            'status': 'Pending...'
        }
    elif task.state != 'FAILURE':
        response = {
            'state': task.state,
            'current': task.info
        }
    else:
        # something went wrong in the background job
        response = {
            'state': task.state,
            'current': 1,
            'total': 1,
            'status': str(task.info),  # this is the exception raised
        }
    return jsonify(response)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
