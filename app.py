from flask import Flask
import sys
import optparse
import time

app = Flask(__name__)

start = int(round(time.time()))


@app.route("/")
def hello_world():

    return "Hello Sauce Labs ! "

if __name__ == '__main__':
    parser = optparse.OptionParser(usage="python app.py -p ")
    parser.add_option('-p', '--port', action='store', dest='port', help='The port to listen on.')
    (args, _) = parser.parse_args()
    if args.port == None:
        print "Missing required argument: -p/--port"
        sys.exit(1)
    app.run(host='0.0.0.0', port=int(args.port), debug=False)


@app.route('/health', methods=['GET'])
def return_ok():
    return 'Ok!', 200

    