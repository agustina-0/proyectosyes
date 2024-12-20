import streamlit as st
st.title("CalculadoraIMC")
peso=st.number_input("Ingrese su peso actual en kg: ",min_value=0.0)

altura=st.number_input("Ingrese su altura actual en mts: ",min_value=0.0)
if peso>0 and altura>0:
    imc=peso/(altura**2)
    st.metric("SUIMC es:",f"{imc:2f}")
    if imc<18.5:
        st.write("Bajo peso")
    elif 18.5<=imc<24.9:
        st.write("Peso normal")
    elif 25<=imc<29.9:
        st.write("Sobre peso")
    else:
        st.write("Obesidad")    
else:
    st.write("ingrese valores a evaluar")                