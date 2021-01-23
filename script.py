from flask import Flask , render_template , request
from folium.plugins import Draw
import json
import folium

app = Flask(__name__)
def getCoords(coords):  
    for i in range(len(coords)):
        if(coords[i] == '['):
            start = i 
        if(coords[i] == ']'):
            end = i+1
            break 
    return coords[start : end]

@app.route('/', methods=['POST','GET'])
def index():
    coords = ''
    if request.method == "POST":
        coords = request.form.get('coords')
        coords = getCoords(coords)
        print(coords)
    return render_template("index.html", coords = coords )


if __name__ == '__main__':
    app.run(debug=True)