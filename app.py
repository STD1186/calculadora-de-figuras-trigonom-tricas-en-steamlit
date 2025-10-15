import streamlit as st
import math

st.title("calculadora de figuras trigonometricas")

# Selección de figura
figura = st.selectbox("Selecciona una figura", ["Círculo", "Cuadrado", "Triángulo", "Rectángulo"])

# Círculo
if figura == "Círculo":
    radio = st.slider("Selecciona el radio", 0.0, 20.0, 5.0)
    area = math.pi * radio**2
    perimetro = 2 * math.pi * radio
    st.metric("Área", f"{area:.2f}")
    st.metric("Perímetro", f"{perimetro:.2f}")
    st.success("¡Cálculos del círculo completados!")

# Cuadrado
elif figura == "Cuadrado":
    lado = st.slider("Selecciona el lado", 0.0, 20.0, 5.0)
    area = lado**2
    perimetro = 4 * lado
    st.metric("Área", f"{area:.2f}")
    st.metric("Perímetro", f"{perimetro:.2f}")
    st.success("¡Cálculos del cuadrado completados!")

# Triángulo
elif figura == "Triángulo":
    base = st.slider("Selecciona la base", 0.0, 20.0, 5.0)
    altura = st.slider("Selecciona la altura", 0.0, 20.0, 5.0)
    lado_a = st.slider("Lado a", 0.0, 20.0, 5.0)
    lado_b = st.slider("Lado b", 0.0, 20.0, 5.0)
    lado_c = st.slider("Lado c", 0.0, 20.0, 5.0)
    area = 0.5 * base * altura
    perimetro = lado_a + lado_b + lado_c
    st.metric("Área", f"{area:.2f}")
    st.metric("Perímetro", f"{perimetro:.2f}")
    st.success("¡Cálculos del triángulo completados!")

# Rectángulo
elif figura == "Rectángulo":
    base = st.slider("Selecciona la base", 0.0, 20.0, 5.0)
    altura = st.slider("Selecciona la altura", 0.0, 20.0, 5.0)
    area = base * altura
    perimetro = 2 * (base + altura)
    st.metric("Área", f"{area:.2f}")
    st.metric("Perímetro", f"{perimetro:.2f}")
    st.success("¡Cálculos del rectángulo completados!")
