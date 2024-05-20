import tempfile
import os
from flask import Flask, request, redirect, send_file
from skimage import io
import base64
import glob
import numpy as np

app = Flask(__name__)

main_html = """
<html>
<head></head>
<script>
  var mousePressed = false;
  var lastX, lastY;
  var ctx;

   function getRndInteger(min, max) {
    return Math.floor(Math.random() * (max - min) ) + min;
   }

  function InitThis() {
      ctx = document.getElementById('myCanvas').getContext("2d");


      numero = getRndInteger(0, 10);
      emociones = ["feliz", "triste", "enojado", "asustado"];
      random = Math.floor(Math.random() * emociones.length);
      aleatorio = emociones[random];

      document.getElementById('mensaje').innerHTML  = 'Dibuja una expresión de ' + aleatorio;
      document.getElementById('numero').value = aleatorio;

      // ... (resto del código igual)
  }

  // ... (resto del código igual)

</script>
<body onload="InitThis();">
    <!-- ... (resto del código HTML igual) -->
</body>
</html>
"""

# ... (resto del código igual)

if __name__ == "__main__":
    emociones = ['feliz', 'triste', 'enojado', 'asustado']
    for e in emociones:
        if not os.path.exists(str(e)):
            os.mkdir(str(e))
    app.run()
