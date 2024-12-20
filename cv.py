import streamlit as st
def main():
    st.title("Curriculum vitae")
    st.sidebar.header("Navegacion")
    page=st.sidebar.radio("Ir a",["perfil","Experiencia","Educacion","Contactar"])
    if page=="perfil":
        st.image("static/img/salud.jpg",width=200)
        st.header("perfil")
        st.write("Nombre:Nahir")
        st.write("Descripcion:recibida de la escuela secundaria de un bachiller de turismo,activa,predispuesta,atencion al publico")
    elif page=="Experiencia":
        st.header("Experiencia laboral")
        st.write("Tomates SRL,Gerente,2020")
    elif page=="Educacion":
        st.header("Educacion")
        st.write("Unju,Lic. en Sistemas,2024-2030")
    elif page=="Habilidades":
        st.header("Habilidades")
        st.write("python")
        st.write("Html")
        st.write("css")
        st.write("sql")
    elif page=="Contactar":
        st.header("Contactar")
        st.write("nahir@yesinfo.com")
        st.write("telefono:3888363636")

if __name__ == "__main__":
    main()                    