from app import app
from config import (SERVER, PORT)

if __name__ == '__main__':
    app.run(host=SERVER, port=PORT, debug=True)
