from flask import Flask, render_template, request
import threading
from monitor import start_monitoring

app = Flask(__name__)
monitor_thread = None

@app.route("/", methods=["GET", "POST"])
def index():
    global monitor_thread
    if request.method == "POST":
        folder_path = request.form["folder_path"]
        drive_folder_id = request.form["drive_folder_id"]
        
        # Start monitoring in a new thread
        monitor_thread = threading.Thread(target=start_monitoring, args=(folder_path, drive_folder_id), daemon=True)
        monitor_thread.start()
        return f"Started monitoring folder: {folder_path}. Check console for updates."

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
