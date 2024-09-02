import geocoder
import folium
from tzwhere import tzwhere
from wsgiref import simple_server
from flask import Flask, request, app,render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['DEBUG'] = True

# ## Route for Forms page
@app.route('/',methods=['GET', 'POST'])
def forms():
    return render_template('home.html')

# ## Route for location
@app.route('/location',methods=['GET', 'POST'])
def track_ip():
    if request.method == "POST":
        ip = request.form.get('ip')
        geocode_ip=geocoder.ip(ip)
        lati = geocode_ip.latlng
        
        if lati is None or lati == []:
            if int(ip[4:7])==168 or int(ip[:3]==10) or (int(ip[:4]==172 and int(ip[4:7])>=16 and int(ip[4:7])<=31)):
                return render_template('home.html',error="You have provided a private IP address, please enter a public IP address")
            else:
                return render_template('home.html',error="Please enter a valid public IP address")
        
        map1 = folium.Map(location=lati, zoom_start=12)
        tzwher = tzwhere.tzwhere()
        timezone = tzwher.tzNameAt(lati[0], lati[1])
        
        folium.Marker(lati, popup='Location of ip: '+ip+'\nTime-zone: '+timezone).add_to(map1)
        map1.save('templates/map.html')
        
        return render_template('map.html')
    
    else:
        return render_template('home.html')

if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)
