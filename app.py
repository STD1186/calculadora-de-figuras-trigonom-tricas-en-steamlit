import streamlit as st
import matplotlib.pyplot as plt
import math

st.title("calculadora de figuras trigonometricas 🎨")

# Selección de figura
figura = st.selectbox("Selecciona una figura", ["Círculo", "Triángulo", "Rectángulo", "Cuadrado"])

# Círculo
if figura == "Círculo":
    radio = st.slider("Selecciona el radio", 0.0, 20.0, 5.0)
# calculo del area
    area = math.pi * radio**2
#calculo del perimetro
    perimetro = 2 * math.pi * radio
# resultados
    st.metric("Área", f"{area:.2f}")
    st.metric("Perímetro", f"{perimetro:.2f}")
    st.success("¡Resultados!")

# Triángulo
elif figura == "Triángulo":
    base = st.slider("Selecciona la base", 0.0, 20.0, 5.0)
    altura = st.slider("Selecciona la altura", 0.0, 20.0, 5.0)
    lado_a = st.slider("Lado a", 0.0, 20.0, 5.0)
    lado_b = st.slider("Lado b", 0.0, 20.0, 5.0)
    lado_c = st.slider("Lado c", 0.0, 20.0, 5.0)
# calculo del area
    area = 0.5 * base * altura
# calculo del perimetro
    perimetro = lado_a + lado_b + lado_c
#resultados
    st.metric("Área", f"{area:.2f}")
    st.metric("Perímetro", f"{perimetro:.2f}")
    st.success("¡Resultados!")

# Rectángulo
elif figura == "Rectángulo":
    base = st.slider("Selecciona la base", 0.0, 20.0, 5.0)
    altura = st.slider("Selecciona la altura", 0.0, 20.0, 5.0)
# calculo del area
    area = base * altura
# calculo del perimetro
    perimetro = 2 * (base + altura)
# calculos
    st.metric("Área", f"{area:.2f}")
    st.metric("Perímetro", f"{perimetro:.2f}")
    st.success("¡Resultados!")

# Cuadrado
elif figura == "Cuadrado":
    lado = st.slider("Selecciona el lado", 0.0, 20.0, 5.0)
# calculo del area
    area = lado**2
# calculo del perimetro
    perimetro = 4 * lado
# resultados
    st.metric("Área", f"{area:.2f}")
    st.metric("Perímetro", f"{perimetro:.2f}")
    st.success("¡Resultados!")



# Selector de color
color = st.color_picker("Selecciona el color del borde", "#00f900", "#00BFFF", "#32CD32", "#FF6347", "#DA70D6")
Puedes copiarlos directamente en el st.color_picker() o usarlos como valores por defecto. ¿Quieres que te ayude a aplicar uno de estos colores a una figura específica?)

# Crear figura de matplotlib
fig, ax = plt.subplots()

if figura == "Círculo":
    radio = st.slider("Radio", 0.0, 10.0, 5.0)
    circle = plt.Circle((0, 0), radio, color=color, fill=False)
    ax.add_artist(circle)
    ax.set_xlim(-radio - 1, radio + 1)
    ax.set_ylim(-radio - 1, radio + 1)

elif figura == "Cuadrado":
    lado = st.slider("Lado", 0.0, 10.0, 5.0)
    square = plt.Rectangle((-lado/2, -lado/2), lado, lado, edgecolor=color, fill=False)
    ax.add_artist(square)
    ax.set_xlim(-lado, lado)
    ax.set_ylim(-lado, lado)

elif figura == "Rectángulo":
    base = st.slider("Base", 0.0, 10.0, 6.0)
    altura = st.slider("Altura", 0.0, 10.0, 4.0)
    rect = plt.Rectangle((-base/2, -altura/2), base, altura, edgecolor=color, fill=False)
    ax.add_artist(rect)
    ax.set_xlim(-base, base)
    ax.set_ylim(-altura, altura)

elif figura == "Triángulo":
    base = st.slider("Base", 0.0, 10.0, 6.0)
    altura = st.slider("Altura", 0.0, 10.0, 4.0)
    # Triángulo isósceles centrado
    x = [-base/2, base/2, 0]
    y = [0, 0, altura]
    triangle = plt.Polygon(list(zip(x, y)), edgecolor=color, fill=False)
    ax.add_artist(triangle)
    ax.set_xlim(-base, base)
    ax.set_ylim(0, altura + 2)

# Configuración final del gráfico
ax.set_aspect('equal')
ax.axis('off')
st.pyplot(fig)
