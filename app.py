from flask import Flask, render_template_string

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Redirigir a GitHub</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f4f8;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        button {
            background-color: #4CAF50;
            border: none;
            color: white;
            padding: 15px 30px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 18px;
            border-radius: 8px;
            cursor: pointer;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: background-color 0.3s ease;
        }
        button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <button onclick="window.location.href='https://github.com/Brayanj20/Plantas'">
        Ir a GitHub Plantas
    </button>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_PAGE)

if __name__ == '__main__':
    app.run(debug=True)
