from flask import Flask, render_template, send_from_directory, Response
import os

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/static/<path:filename>")
def serve_static(filename):
    def generate():
        file_path = os.path.join("static", filename)
        file_size = os.path.getsize(file_path)
        with open(file_path, "rb") as audio_file:
            while True:
                chunk = audio_file.read(1024)
                if not chunk:
                    break
                yield chunk

    response = Response(generate(), mimetype="audio/mpeg")
    response.headers["Content-Length"] = os.path.getsize(
        os.path.join("static", filename)
    )
    return response


if __name__ == "__main__":
    app.run(debug=True)
