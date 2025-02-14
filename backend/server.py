from flask import Flask\napp = Flask(__name__)\n@app.route('/')\ndef home():\n    return 'SmartScaleAI Server Running'\n\nif __name__ == '__main__':\n    app.run(host='0.0.0.0', port=8000)
