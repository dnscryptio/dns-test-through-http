from dns.resolver import Resolver
from dns.exception import Timeout
from flask import Flask, abort


def resolve(ip='127.0.0.1', port=53, hostname='google.com', timeout=5):
    resolver = Resolver()
    resolver.nameservers = [ip]
    resolver.port = port
    resolver.lifetime = timeout # seconds

    try:
        if len(list(resolver.query('google.com', 'A'))) < 1:
            abort(500)
    except Timeout as e:
        abort(500)

    return 'OK'


app = Flask(__name__)

@app.route("/test")
def test():
    return resolve()

if __name__ == "__main__":
    app.run()
