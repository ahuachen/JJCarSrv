#!/bin/python
import signal, time, os
from flask import Flask
from flask import request


app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"


@app.route('/carServer/action1', methods=['GET'])
def carAction1():
    #0:stop,1:left,2:right,4:up,8:back
    return "action1"

@app.route('/carServer/action', methods=['POST'])
def carAction():
    #0:stop,1:left,2:right,4:up,8:back
    action_id = request.form.get('action')
    stamp = request.form.get('stamp')
    
    if not action_id.strip():
	#error
	print('bad command none', action_id)
        abort(404)

    if action_id == '0':
	#stop
	print(stamp, 'stop')
	os.popen('python /home/pi/projects/gpio/dianjidown.py')
    elif action_id == '1':
	#left
	print(stamp, 'left')
	os.popen('python /home/pi/projects/gpio/dianjileft.py')
    elif action_id == '2':
	#right
	print(stamp, 'right')
	os.popen('python /home/pi/projects/gpio/dianjiright.py')
    elif action_id == '4':
	#up
	print(stamp, 'up')
	os.popen('python /home/pi/projects/gpio/dianjiup.py')
    elif action_id == '8':
	#back
	print(stamp, 'back')
	os.popen('python /home/pi/projects/gpio/dianjiback.py')
    else:
	#error
	print('bad command', action_id)
        abort(404)

    return "OK" + action_id


def cb(s, f):
  print 'recv signal', s
  # Reset GPIO settings
  os.popen('python /home/pi/projects/gpio/dianjidown.py')
  print 'quit'
  exit(0)

if __name__ == '__main__':
    signal.signal(signal.SIGTERM, cb)
    signal.signal(signal.SIGINT, cb)
    app.run(host='0.0.0.0', debug=True)
