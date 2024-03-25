import streamlit as st
from texto.datos_texto import InfoCurriculum

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

    c_linkedin, c_github, c_curriculo_pdf = st.columns(
        [0.2, 0.2, 0.3,], gap="small")
    with c_linkedin:
        st.link_button(label="LinkedIn", url=social_media["LinkedIn"])
    with c_github:
        st.link_button(label="GitHub", url=social_media["GitHub"])
    with c_curriculo_pdf:
        with open("assets/Hoja_de_vida_2024.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        st.download_button(label="Download CV",
                           data=PDFbyte,
                           file_name="CV_CristianMG.pdf")


infoCurriculum = InfoCurriculum()

tabs: list = ["Sobre mi", "Skills", "Educación",
              "Experiencia", "Licencias y certificaciones"]
t_resumen, t_skills, t_edu, t_expe, t_certi = st.tabs(tabs)

with t_resumen:
    with st.container():
        st.markdown(infoCurriculum.resumen, unsafe_allow_html=True)

with t_skills:
    st.markdown(infoCurriculum.skills, unsafe_allow_html=True)

with t_edu:
    st.markdown(infoCurriculum.educacion, unsafe_allow_html=True)

with t_expe:
    st.markdown(infoCurriculum.experiencia, unsafe_allow_html=True)

with t_certi:
    st.markdown(infoCurriculum.licencias_cer, unsafe_allow_html=True)
