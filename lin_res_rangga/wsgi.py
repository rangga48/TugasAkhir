from dotenv import load_dotenv
load_dotenv('.env')
from main import app
import os
if __name__ == "__main__":
    appLogger = app.logger
    import logging
    # logging.basicConfig(filename="logs/access.log", level=logging.INF
    try:
        os.mkdir("logs")
    except OSError as error:
        if error.errno != 17:
            print(error)
    except:
        print("Error pada server")
    logging.basicConfig(filename="logs/error.log", level=logging.ERROR)

    app.run(host="0.0.0.0", debug=False, port=os.environ.get("PORT", "5000"))