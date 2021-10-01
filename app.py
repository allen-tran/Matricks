__author__ = "Allen Tran"
__version__ = "1.0"
__date__ = "06/06/2021"

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)