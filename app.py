from flask import Flask, render_template, request, send_from_directory, redirect, url_for
import os

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    files = []
    for filename in os.listdir(app.config['UPLOAD_FOLDER']):
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        if os.path.isfile(path):
            size = round(os.path.getsize(path) / 1024 / 1024, 2)
            ext = os.path.splitext(filename)[1].lower()
            icon = "bi-file-earmark"
            if ext == ".frx":
                icon = "bi-puzzle"
            elif ext == ".snap":
                icon = "bi-hdd"
            elif ext in [".iso", ".img"]:
                icon = "bi-disc"
            elif ext == ".deb":
                icon = "bi-box-seam"
            elif ext == ".zip":
                icon = "bi-file-zip"
            elif ext == ".txt":
                icon = "bi-file-text"
            elif ext == ".sh":
                icon = "bi-terminal"
            files.append({'name': filename, 'size': size, 'icon': icon})
    return render_template('index.html', files=files)

@app.route('/download/<path:filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

@app.route('/upload', methods=['GET'])
def upload_page():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files or request.files['file'].filename == '':
        return "No file selected", 400
    file = request.files['file']
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    return redirect(url_for('index'))

@app.route('/uploads/<path:filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    import os
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
