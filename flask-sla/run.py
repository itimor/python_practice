# coding:utf-8
from demo.init_app import app
from flask_script import Manager, Server
from sys import argv


server = Server(host='0.0.0.0',port=5000,debug=True)

manager = Manager(app)

manager.add_command("runserver", server)

if __name__ == '__main__':
    if len(argv) > 1:
        manager.run()
    else:
        app.run(host='0.0.0.0',port=5000,debug=True)