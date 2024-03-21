import streamlit as st

layout: str = "centered"
page_title: str = "Porfolio | Cristian Montoya Garces"
page_icon = "🗃️"


# ---Config pagina---
st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)

social_media: dict = {
    "LinkedIn": "https://www.linkedin.com/in/cristianmontoyagarces/",
    "GitHub": "https://github.com/Mongar28",
}


# ---Columnas con los links de las las redes sociales---

c_foto, c_nombre = st.columns(spec=[0.4, 0.7])

with c_foto:
    st.image("assets/foto_redonda.png")


with c_nombre:
    st.title("Cristian Montoya Garces")

    c_linkedin, c_github, c_espacio = st.columns([0.3, 0.3, 0.5])
    with c_linkedin:
        st.link_button(label="LinkedIn", url=social_media["LinkedIn"])
    with c_github:
        st.link_button(label="GitHub", url=social_media["GitHub"])


resumen = """
<div style="text-align: justify">
👋 Soy Cristian Montoya Garcés, estudiante de sociología con una pasión por la programación. Combino estos mundos para acceder al conocimiento desde una perspectiva innovadora e interdisciplinar. 🌐💡

Mi camino en la programación, especialmente con Python, me ha brindado herramientas potentes para acceder y analizar la abundante información en la sociedad actual. Esto ha permitido que desarrolle un enfoque en la investigación en ciencias sociales más amplio e innovador. 📊🔍

Con habilidades en web scraping, procesamiento y limpieza de datos, expresiones regulares y herramientas básicas de NLP, he obtenido resultados destacados en el ámbito académico. Acceder a fuentes de información en las ciencias sociales la mayoría de las veces requiere de muchos recursos, y es ahí donde la programación, con sus facilidades para automatizar, extraer, procesar y transformar los datos, enriquece la experiencia investigativa otorgándole dinamismo y eficiencia. Pero de igual manera, estoy muy interesado en llevar mi expertise a la industria tecnológica. 🚀🔧

Me emociona seguir aprendiendo y contribuir con mi conocimiento para beneficiar a otros. Siempre abierto a nuevas oportunidades y desafíos. ¡Conectemos y exploremos juntos! 🤝
</div>
"""

skills: str = """
- **Lenguajes de programación:** Python, Bash, SQL.
- **Paradigmas de programación:** Porgramación orientada a objetos, funicional, imperativa/procedural.
- **Herramientas:** Docker, Streamlit, web scraping
- **Soft skills:** Responsable, confiable, transparente, eficiente, fuertes habilidades de comunicación y resolución de problemas, orientado al detalle.
- **Lenguages:** Español (Nativo - C2), Inglés (B1).
"""

educacion: str = """
### **Universidad de Antioquia**

**Sociología**
- **Grupos**
    - Coordinador: Semillero de Investigación de Ciencias Sociales Computacionales
    - Linea de investigación: Territorios Inteligentes adscrito al grupo de investigación Redes Y Actores
Sociales (RAS) de la Facultad de Ciencias Sociales y Humanas dela Universidad de Antioquia.
- **Actividades**
    - Como Coordinador del Semillero de Ciencias Sociales Computacionales, tengo la responsabilidad de
    liderar el desarrollo de algoritmos para mejorar la recolección y análisis de datos en investigaciones en
    ciencias sociales. Además, realizo la gestión administrativa necesaria para el funcionamiento dinámico
    del semillero de investigación. Asimismo, lidero los procesos de trabajo del semillero en colaboración
    con otros semilleristas.
"""

experiencia: str = '''
### **Universidad de Antioquia** - Oct 2023 - Actualidad
Jornada parcial - híbrido
***Joven investigador***

<div style="text-align: justify">
    Como joven investigador en la línea de investigación de Territorios Inteligentes, he sido fundamental en la
    aplicación de enfoques teóricos y metodológicos innovadores para desarrollar técnicas computacionales
    destinadas a mejorar los procesos de investigación en ciencias sociales. Mis responsabilidades incluyen la
    investigación teórica y metodológica para el desarrollo de técnicas computacionales, la extracción de
    información de bases de datos bibliográficas mediante web scraping, la utilización de modelos de lenguaje
    de inteligencia artificial para el procesamiento de datos y la identificación de patrones, la estructuración y
    reestructuración de grandes volúmenes de datos cualitativos, el desarrollo de scripts y herramientas
    informáticas para optimizar el proceso de investigación, y la colaboración en la creación y ejecución de
    proyectos de investigación.
</div>

### **Universidad de Antioquia** - May 2023 - Sep 2023
Jornada parcial - híbrido
***Pasante de investigación**

<div style="text-align: justify">
Como pasante de investigación, participé en un proyecto cuyo objetivo es desarrollar una ruta estratégica
de investigación en la Facultad de Ciencias Sociales y Humanas como parte del Plan de Acción 2022-2025.
Mis responsabilidades dentro del proyecto incluyeron la recopilación, sistematización y análisis de datos, así
como la construcción de scripts para la extracción de datos de Internet mediante web scraping y la
elaboración de scripts para la estructuración y limpieza de datos cualitativos.
</div>
'''

tabs: list = ["Sobre mi", "Skills", "Educación", "Experiencia", "Licencias y certificaciones"]
t_resumen, t_skills, t_edu, t_expe, t_certi = st.tabs(tabs)

with t_resumen:
    with st.container():
        st.markdown(resumen, unsafe_allow_html=True)

with t_skills:
    st.markdown(skills)

with t_edu:
    st.markdown(educacion)
    
with t_expe:
    st.markdown(experiencia)
