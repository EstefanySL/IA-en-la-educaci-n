import streamlit as st

# Configuración de la página
st.set_page_config(page_title="IA en la Educación", layout="wide")

# Estilos personalizados (paleta azul)
st.markdown("""
    <style>
    body {
        background-color: #f4f8fb;
    }
    .title {
        font-size: 48px;
        font-weight: bold;
        color: #0b3c5d;
        text-align: center;
    }
    .subtitle {
        font-size: 20px;
        color: #1d4e89;
        text-align: center;
        margin-bottom: 30px;
    }
    .section-title {
        font-size: 28px;
        color: #0b3c5d;
        margin-top: 20px;
    }
    .content {
        font-size: 18px;
        color: #333333;
        text-align: justify;
    }
    </style>
""", unsafe_allow_html=True)

# Título principal
st.markdown('<div class="title">La inteligencia artificial en la educación</div>', unsafe_allow_html=True)

# Frase debajo del título
st.markdown('<div class="subtitle">“La inteligencia artificial no sustituye tu mente, la potencia: aprender a usarla es aprender a multiplicar tu propio conocimiento.”</div>', unsafe_allow_html=True)

# Menú lateral
st.sidebar.title("Menú")
seccion = st.sidebar.radio("Selecciona una sección:", [
    "La Revolución Inteligente en el Aula",
    "¿Qué es exactamente la AIEd?",
    "El aprendizaje que se adapta a ti",
    "Nuevas habilidades para un mundo digital",
    "Los desafíos que debemos enfrentar",
    "Conclusión",
    "Referencias"
])

# Secciones
if seccion == "La Revolución Inteligente en el Aula":
    st.markdown('<div class="section-title">La Revolución Inteligente en el Aula: ¿Cómo la IA está Transformando tu Forma de Aprender?</div>', unsafe_allow_html=True)
    st.markdown('<div class="content">La educación digital del siglo XXI ha encontrado un aliado que, hasta hace poco, parecía parte de una película de ciencia ficción: la Inteligencia Artificial (IA). Lo que comenzó como una disciplina técnica se ha convertido en un pilar fundamental para transformar cómo aprendemos y enseñamos. Especialmente desde el año 2022, la llegada de herramientas de "IA generativa" —capaces de crear texto y conversar con nosotros— ha cambiado por completo la relación entre profesores y alumnos.</div>', unsafe_allow_html=True)

elif seccion == "¿Qué es exactamente la AIEd?":
    st.markdown('<div class="section-title">¿Qué es exactamente la AIEd?</div>', unsafe_allow_html=True)
    st.markdown('<div class="content">Cuando hablamos de IA en educación (AIEd), nos referimos a sistemas computacionales diseñados para realizar tareas que normalmente requieren de la inteligencia humana. Estos sistemas no solo procesan datos, sino que permiten crear experiencias personalizadas en tiempo real para cada estudiante.</div>', unsafe_allow_html=True)

elif seccion == "El aprendizaje que se adapta a ti":
    st.markdown('<div class="section-title">El aprendizaje que se adapta a ti</div>', unsafe_allow_html=True)
    st.markdown('<div class="content">Imagina que tu libro de texto pudiera cambiar su dificultad dependiendo de qué tan rápido vas. Esto es lo que llamamos aprendizaje adaptativo. A diferencia del modelo tradicional donde todos reciben lo mismo, la IA utiliza algoritmos avanzados (como el machine learning o aprendizaje automático) para ajustar el contenido, el ritmo y las estrategias de enseñanza al perfil de cada alumno.</div>', unsafe_allow_html=True)

    st.markdown('<div class="content">Para lograr esta personalización, destacan dos herramientas:</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="content">
    * Sistemas de Tutoría Inteligente (ITS): Son tutores virtuales que usan el lenguaje natural para guiar al estudiante paso a paso, lo que mejora la motivación y los resultados académicos.<br><br>
    * Analítica Multimodal: Estos sistemas analizan datos de diversas fuentes para predecir comportamientos y ajustar las clases de manera muy precisa.
    </div>
    """, unsafe_allow_html=True)

elif seccion == "Nuevas habilidades para un mundo digital":
    st.markdown('<div class="section-title">Nuevas habilidades para un mundo digital</div>', unsafe_allow_html=True)
    st.markdown('<div class="content">Hoy en día, no basta con saber usar una computadora; necesitamos desarrollar la alfabetización en IA (AI literacy). Esta nueva competencia va desde entender conceptos técnicos básicos hasta desarrollar el pensamiento computacional y la ética en el manejo de datos. Es una habilidad que debe cultivarse desde la primaria hasta la universidad.</div>', unsafe_allow_html=True)

    st.markdown('<div class="content">Además, la IA tiene un papel noble: fomentar la equidad y la inclusión. Gracias a herramientas asistivas, alumnos con discapacidades pueden acceder a información y participar en entornos educativos que antes tenían barreras insuperables. Sin embargo, existe un riesgo: si esta tecnología no se distribuye de forma justa, las brechas entre quienes tienen acceso a internet y quienes no podrían hacerse más grandes.</div>', unsafe_allow_html=True)

elif seccion == "Los desafíos que debemos enfrentar":
    st.markdown('<div class="section-title">Los desafíos que debemos enfrentar</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="content">
    * Integridad y Ética: La IA generativa pone a prueba la honestidad académica y puede traer sesgos (prejuicios) en la forma en que se evalúa a los alumnos.<br><br>
    * Formación Docente: Muchos profesores sienten resistencia porque no han recibido la formación técnica necesaria para usar estas herramientas de forma eficiente.<br><br>
    * Dependencia Tecnológica: Existe el temor de que, si confiamos demasiado en sistemas automáticos, dejemos de desarrollar nuestras propias habilidades críticas y autónomas.
    </div>
    """, unsafe_allow_html=True)

elif seccion == "Conclusión":
    st.markdown('<div class="section-title">Conclusión</div>', unsafe_allow_html=True)
    st.markdown('<div class="content">La Inteligencia Artificial no ha llegado para reemplazar a los maestros, sino para potenciar el aprendizaje humano. Al personalizar la enseñanza y derribar barreras de inclusión, ofrece una oportunidad histórica, siempre y cuando se maneje con ética y se garantice que nadie se quede atrás por falta de tecnología.</div>', unsafe_allow_html=True)

elif seccion == "Referencias":
    st.markdown('<div class="section-title">Referencias</div>', unsafe_allow_html=True)
    st.markdown('<div class="content">García, M., y Crespo, J. (s.f.). Uso de tecnologías digitales en educación. Revista Iberoamericana de Investigación en Educación.<br><br>El artículo analiza el uso de tecnologías digitales en el ámbito educativo, destacando su utilidad, frecuencia y efectividad según percepciones de usuarios. Se identifican beneficios como la mejora del aprendizaje y la accesibilidad, pero también limitaciones como la falta de dispositivos, capacitación y sobrecarga de actividades. Concluye que su impacto depende del acceso y la formación adecuada.<br><br>Martínez, I. (2025). Inteligencia artificial generativa en los procesos de enseñanza-aprendizaje: retos y oportunidades. Revista Psicología Educativa.<br><br>Analiza el impacto de la inteligencia artificial generativa en la educación mediante una revisión documental de artículos científicos y estudios internacionales. Destaca beneficios como la automatización de tareas, la personalización del aprendizaje y el aumento de la motivación estudiantil. Sin embargo, también señala riesgos como el uso poco reflexivo y la posible pérdida de habilidades críticas. Concluye que es necesario establecer normativas claras, capacitar a docentes y promover un uso ético y responsable.<br><br>Hariyanto, H., Kristianingsih, F. X. D., & Maharani, R. (2025). Artificial intelligence in adaptive education: a systematic review of techniques for personalized learning. Discover Education, 4, 458.<br><br>Este artículo presenta una revisión sistemática de 142 estudios sobre el uso de la inteligencia artificial en el aprendizaje personalizado. Explica cómo técnicas como el machine learning, deep learning y el aprendizaje por refuerzo permiten adaptar los contenidos educativos en tiempo real a las necesidades de cada estudiante. Se destacan beneficios como el aumento del compromiso, la mejora del rendimiento académico y la promoción de la equidad educativa. No obstante, se identifican desafíos importantes como la privacidad de los datos, la interpretabilidad de los modelos y su implementación en contextos con pocos recursos.<br><br>Fu, Y., Weng, Z., & Wang, J. (2025). Examining AI use in educational contexts: A scoping meta-review and bibliometric analysis. International Journal of Artificial Intelligence in Education, 35, 1388–1444.<br><br>Este estudio realiza una meta-revisión de 126 artículos sobre inteligencia artificial en educación, con el objetivo de ofrecer una visión general del campo. Identifica tres áreas principales de impacto: la enseñanza, el aprendizaje y la administración educativa. Además, muestra un crecimiento acelerado en la investigación sobre IA y destaca el uso predominante de técnicas como el machine learning. El artículo concluye que aún existen vacíos importantes en la investigación y sugiere la necesidad de estudios más integradores y aplicados.<br><br>Garzón, J., Patiño, E., & Marulanda, C. (2025). Systematic review of artificial intelligence in education: Trends, benefits, and challenges.<br><br>Este artículo presenta una revisión sistemática de 155 estudios sobre inteligencia artificial en educación, analizando tendencias, beneficios y desafíos.<br><br>Cotilla Conceição, J. M., & van der Stappen, E. (2025). The Impact of AI on Inclusivity in Higher Education: A Rapid Review. Education Sciences.<br><br>Analiza el uso de la IA en la educación superior con enfoque en la inclusión. Señala que herramientas como el aprendizaje adaptativo y los tutores inteligentes permiten personalizar la enseñanza, pero en la práctica se usan más para eficiencia que para equidad. También identifica problemas como desigualdad de acceso y sesgos en los datos. Concluye que, sin un enfoque ético e inclusivo, la IA puede aumentar las brechas educativas.<br><br>Bond, M. et al. (2024). A meta systematic review of artificial intelligence in higher education. International Journal of Educational Technology in Higher Education.<br><br>Revisión de múltiples estudios sobre IA en educación superior. Encuentra que las aplicaciones más comunes son la personalización del aprendizaje, los sistemas adaptativos y la predicción del rendimiento. También menciona herramientas como tutores inteligentes y evaluación automatizada. Destaca la necesidad de mejorar la calidad de la investigación y fortalecer aspectos éticos y de colaboración interdisciplinaria.<br><br>Yim, I. H. Y., & Su, J. (2025). Artificial intelligence literacy education in primary schools: a review.<br><br>Revisión sobre la enseñanza de alfabetización en IA en primaria. Define que incluye comprensión de la IA, pensamiento computacional y ética. Identifica metodologías como aprendizaje basado en proyectos y uso de herramientas digitales. Aunque se observan beneficios en el aprendizaje y motivación, existen retos como la falta de contenidos claros y la necesidad de capacitar a los docentes.<br><br>Acuña-Gamboa, L. A. (2025). Inteligencia artificial e investigación educativa en los contextos internacional y mexicano.<br><br>Analiza el uso de la IA en la investigación educativa. Señala que se emplea en revisión de literatura, diseño de estudios y análisis de datos, mejorando la eficiencia. Sin embargo, advierte riesgos como sesgos y problemas éticos. Concluye que la IA debe usarse como apoyo, junto con el pensamiento crítico y la formación ética de los investigadores.<br><br>(2024). La inteligencia artificial en la educación: De la personalización al aprendizaje complejo-colectivo. UCA Profesional.<br><br>El artículo analiza el impacto de la inteligencia artificial en la transformación de la educación, pasando de modelos tradicionales a enfoques personalizados y colectivos. Explica cómo la IA permite adaptar el aprendizaje a las necesidades individuales mediante el uso de datos y sistemas inteligentes. Sin embargo, también advierte sobre problemas como la aceptación acrítica de la tecnología, la confiabilidad de la información generada y los efectos sociales derivados de su uso. Además, resalta la importancia de considerar aspectos éticos y de fomentar un pensamiento crítico en los estudiantes frente a estas herramientas.<br><br>Aparicio-Gómez, O.-Y., Ostos-Ortiz, O.-L., & Abadía-García, C. (2025). Inteligencia artificial y aprendizaje personalizado en el siglo XXI.<br><br>Este artículo examina cómo la inteligencia artificial ha revolucionado los procesos educativos mediante el aprendizaje personalizado. A través de una revisión de literatura, se demuestra que los sistemas basados en IA mejoran el rendimiento académico, incrementan la motivación y promueven la autonomía del estudiante. No obstante, también se identifican desafíos importantes como la opacidad de los algoritmos, los riesgos para la privacidad de los datos y la posibilidad de sesgos en los sistemas automatizados. Los autores concluyen que es necesario implementar políticas educativas que regulen su uso ético y fomenten un equilibrio entre tecnología y pedagogía.<br><br>Barros Tutivén, Z. M., Alvarado Cabrera, Y. D., Guamán Rodríguez, C. A., Vargas Barrionuevo, S. J., Valenzuela Valenzuela, F. M., & Mosquera Méndez, D. F. (2025). Inteligencia artificial aplicada al aprendizaje personalizado en educación básica.<br><br>La investigación analiza el impacto de la inteligencia artificial en estudiantes de educación básica mediante un enfoque mixto. Los resultados evidencian mejoras significativas en el rendimiento académico, la motivación, la participación y la comprensión de contenidos, especialmente en áreas como matemáticas y ciencias. Además, se observa un fortalecimiento de la autonomía y de las habilidades digitales de los estudiantes. El estudio concluye que la IA favorece una educación más inclusiva y equitativa, aunque subraya la necesidad de establecer marcos éticos claros y garantizar la capacitación continua de los docentes.<br><br>Lumbi Salazar, F. O., Zurita Pilco, L. A., & Achiña Andrango, E. P. (2025). La inteligencia artificial como herramienta para personalizar el aprendizaje en la educación superior.<br><br>Este artículo describe cómo la inteligencia artificial se ha convertido en una herramienta clave en la educación superior para personalizar el aprendizaje. Explica que los sistemas inteligentes permiten adaptar contenidos, identificar estilos de aprendizaje y ofrecer retroalimentación inmediata, lo que mejora la experiencia educativa.<br><br>Macías León, H. A. (2025). Estrategias de enseñanza basadas en inteligencia artificial para lograr un aprendizaje personalizado, inclusivo y centrado en las necesidades individuales de cada estudiante.<br><br>El artículo presenta una revisión sistemática sobre estrategias de enseñanza apoyadas en inteligencia artificial. Se destaca que herramientas como tutores virtuales, sistemas adaptativos y analítica del aprendizaje permiten ajustar los contenidos y ritmos educativos a las características de cada estudiante. Esto favorece la inclusión, especialmente en estudiantes con necesidades educativas especiales.<br><br>Peñalver-Higuera, M. J., Guerra-Castellanos, Y. B., Rodríguez Alegre, L. R., & López Padilla, R. del P. (2024). Transformando la educación con inteligencia artificial: Hacia un aprendizaje personalizado en la era 4.0.<br><br>Este artículo realiza una revisión sistemática sobre el papel de la inteligencia artificial en la educación dentro del contexto de la Educación 4.0. Los autores destacan que la IA ha evolucionado desde herramientas básicas hasta sistemas avanzados capaces de personalizar el aprendizaje en tiempo real. Asimismo, se enfatiza que la IA mejora la eficiencia educativa al automatizar tareas administrativas y apoyar a docentes y estudiantes.<br><br>Hoana, N. Y. (2025). Artificial intelligence in education: Transforming the learning experience.<br><br>El artículo analiza el papel transformador de la inteligencia artificial en la educación moderna. Describe cómo tecnologías como los sistemas de tutoría inteligente, la evaluación automatizada y el análisis predictivo permiten personalizar el aprendizaje y mejorar el rendimiento académico.<br><br>Leal Ríos, F., Hernández Ramírez, M., Ruiz Méndez, M., & Cabero Almenara, J. (2025). Educación e inteligencia artificial: Generando ecosistemas de aprendizaje adaptativo.<br><br>Este libro aborda el impacto de la inteligencia artificial en la educación superior desde una perspectiva integral. Analiza la evolución de la IA, su papel en la creación de ecosistemas de aprendizaje adaptativo y su influencia en las competencias docentes. Además, destaca la importancia de diseñar modelos educativos flexibles, inclusivos y centrados en el estudiante.<br><br>Chen, X., & Pérez, M. (2023). Artificial intelligence in personalized education: Opportunities and challenges.<br><br>Este artículo analiza el uso de la inteligencia artificial en la educación personalizada, destacando su capacidad para adaptar contenidos, evaluar el progreso de los estudiantes y ofrecer retroalimentación en tiempo real.<br><br>Sadiku, M. N. O., Ashaolu, T. J., Ajayi-Majebi, A., & Musa, S. M. (2021). Artificial intelligence in education.<br><br>El artículo ofrece una visión general sobre la inteligencia artificial en la educación, explicando sus aplicaciones y beneficios. Señala que la IA permite automatizar tareas, mejorar la enseñanza y personalizar el aprendizaje. Además, destaca que esta tecnología facilita la interacción entre estudiantes y contenidos educativos, haciendo el aprendizaje más flexible y eficiente.<br><br>Martínez-Márquez, M. A. (2025). Inteligencia artificial y educación.<br><br>Este artículo analiza las realidades y retos del uso de la inteligencia artificial en la educación. Señala que la IA es una tecnología disruptiva con gran potencial para innovar los procesos educativos, pero su éxito depende de la alfabetización digital de docentes y estudiantes.</div>', unsafe_allow_html=True)
