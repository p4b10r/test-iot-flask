from flask import Flask, render_template
from flask_mqtt import Mqtt
from flask_socketio import SocketIO


app=Flask(__name__) #creación objeto flask, recibiendo como parametro __name__

#configuraciones de broker MQTT
app.config['MQTT_BROKER_URL'] = '192.168.1.48'
app.config['MQTT_BROKER_PORT'] = 1883
app.config['MQTT_USERNAME'] = ''
app.config['MQTT_PASSWORD'] = ''
app.config['MQTT_KEEPALIVE'] = 5

mqtt=Mqtt(app) #creación objeto mqtt, recibe como parámetro app
socketio=SocketIO(app) #creación objeto socketio recibiendo como parámetro app




#ruta de la aplicación

@app.route("/")
def Index():
    
    return render_template("index.html")


#rutas y decoradores socketio

@socketio.on("publish")
def handle_publish(json_str):
    data=json.loads(json_str)
    mqtt.publish(data["topic"],data["message"])


if "__name__"=="__main__":
    app.run(host="127.0.0.1", port=5000, use_reloader=False, debug=True)


