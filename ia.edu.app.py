contenido_html = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>La Inteligencia Artificial en la Educación</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
            background-color: #f4f4f4;
            line-height: 1.6;
        }
        h1, h2 {
            color: #2c3e50;
        }
        p {
            color: #333;
        }
        .container {
            background: white;
            padding: 20px;
            border-radius: 10px;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>La inteligencia artificial en la educación</h1>

    <p><em>“La inteligencia artificial no sustituye tu mente, la potencia: aprender a usarla es aprender a multiplicar tu propio conocimiento.”</em></p>

    <h2>¿Qué es la IA en educación?</h2>
    <p>
        La Inteligencia Artificial en educación (AIEd) se refiere a sistemas computacionales
        capaces de realizar tareas que normalmente requieren inteligencia humana. Permiten
        crear experiencias personalizadas para cada estudiante.
    </p>

    <h2>1. Aprendizaje adaptativo</h2>
    <p>
        La IA permite ajustar el contenido, ritmo y estrategias de enseñanza según el nivel
        del alumno. Utiliza técnicas como el aprendizaje automático.
    </p>

    <p><strong>Herramientas principales:</strong></p>
    <ul>
        <li>Sistemas de Tutoría Inteligente: guían al estudiante paso a paso.</li>
        <li>Analítica Multimodal: analiza datos para mejorar el aprendizaje.</li>
    </ul>

    <h2>2. Nuevas habilidades digitales</h2>
    <p>
        La alfabetización en IA incluye comprender conceptos básicos, desarrollar pensamiento
        computacional y actuar con ética en el uso de datos.
    </p>

    <p>
        Además, la IA fomenta la inclusión, permitiendo que estudiantes con discapacidades
        accedan a mejores oportunidades educativas.
    </p>

    <h2>3. Desafíos de la IA</h2>
    <ul>
        <li>Ética e integridad académica</li>
        <li>Falta de capacitación docente</li>
        <li>Dependencia tecnológica</li>
    </ul>

    <h2>Conclusión</h2>
    <p>
        La inteligencia artificial no reemplaza a los docentes, sino que potencia el aprendizaje.
        Ofrece una gran oportunidad si se utiliza de manera ética y responsable.
    </p>

</div>

</body>
</html>
"""

# Guardar archivo HTML
with open("ia_educacion.html", "w", encoding="utf-8") as archivo:
    archivo.write(contenido_html)
