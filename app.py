from flask import Flask, render_template
#from flask_mqtt import Mqtt
#from flask_socketio import SocketIO


app=Flask(__name__) #creación objeto flask, recibiendo como parametro __name__

#configuraciones de broker MQTT


#ruta de la aplicación

@app.route("/")
def Index():
    
    return "vamolopibee"


#rutas y decoradores socketio

#if "__name__"=="__main__":
#    app.run(host="127.0.0.1", port=5000, use_reloader=False, debug=True)


