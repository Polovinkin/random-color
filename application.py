from flask import Flask, render_template
import os
import random
from PIL import Image

app = Flask(__name__, template_folder='static/templates')
app.config['UPLOAD_FOLDER'] = os.path.join('static', 'pics')

@app.route('/')
def show_index():
    colors_list = random.sample(range(1,255), 3)
    colors = tuple(colors_list)
    img = Image.new('RGB', (500, 500), colors)
    filename = str(colors).replace(')','').replace('(','').replace(',','-').replace(' ','') + ".png"
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    img.save(os.path.join(full_filename))
    
    return render_template("index.html", user_image = full_filename)

if __name__ == "__main__":
    app.run(debug=True)