from app.app import app
from app import version

if __name__ == "__main__":
    print("Version : " + version)
    app.run(debug=app.config["DEBUG"])