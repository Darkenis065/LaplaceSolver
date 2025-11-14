import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from campo_estatico_mdf.solver import LaplaceSolver2D # (RNF1.1)

st.set_page_config(layout="wide")
st.title("Taller Avanzado: Solucion del Campo Electroestatico 2D (MDF)")

# --- 1. ENTRADAS DE USUARIO (RF2.1) ---
st.sidebar.header("Parametros de Simulacion")

N = st.sidebar.slider("Tamaño de la malla (N x N)", 10, 100, 20)
tolerancia = st.sidebar.number_input("Tolerancia (ε)", 1e-3, 1e-8, 1e-5, format="%.8f")

st.sidebar.subheader("Voltajes de Contorno (V)")
v_arriba = st.sidebar.number_input("V Arriba", value=0.0)
v_abajo = st.sidebar.number_input("V Abajo", value=0.0)
v_izquierda = st.sidebar.number_input("V Izquierda", value=10.0)
v_derecha = st.sidebar.number_input("V Derecha", value=0.0)

# --- 2. PROCESAMIENTO (Backend) ---
if st.sidebar.button("Resolver Simulacion"):
    
    # Crear y resolver la simulacion
    with st.spinner(f"Resolviendo malla {N}x{N}..."):
        solver = LaplaceSolver2D(N, v_izquierda, v_derecha, v_arriba, v_abajo)
        iteraciones = solver.resolver_jacobi(tolerancia)
    
    # Obtener resultados
    V = solver.V
    Ex, Ey = solver.calcular_campo_e()
    
    st.success(f"¡Convergencia alcanzada en {iteraciones} iteraciones!")

    # --- 3. SALIDAS (RF2.2, RF2.3, RF2.4) ---
    
    # Metrica de Convergencia (RF2.4)
    st.metric("Iteraciones Requeridas", iteraciones)

    col1, col2 = st.columns(2)

    # Grafico 1: Mapa de Colores (Heatmap) (RF2.2)
    with col1:
        st.subheader("Potencial Electrico V(x, y)")
        fig_v, ax_v = plt.subplots()
        im = ax_v.imshow(V, cmap='viridis', origin='lower')
        plt.colorbar(im, ax=ax_v, label='Potencial (V)')
        ax_v.set_xlabel('x')
        ax_v.set_ylabel('y')
        st.pyplot(fig_v)

    # Grafico 2: Grafico de Vectores (Quiver) (RF2.3)
    with col2:
        st.subheader("Campo Electrico E(x, y)")
        
        # Reducir la densidad del quiver para mejor visualizacion
        skip = max(1, N // 15)
        x = np.arange(0, N, skip)
        y = np.arange(0, N, skip)
        X, Y = np.meshgrid(x, y)
        
        Ex_q = Ex[::skip, ::skip]
        Ey_q = Ey[::skip, ::skip]

        fig_e, ax_e = plt.subplots()
        # Dibujar tambien el potencial como fondo
        ax_e.imshow(V, cmap='viridis', origin='lower', alpha=0.5)
        # Dibujar los vectores (Quiver)
        ax_e.quiver(X, Y, Ex_q, Ey_q, color='red', scale_units='xy', scale=None)
        ax_e.set_xlabel('x')
        ax_e.set_ylabel('y')
        st.pyplot(fig_e)

else:
    st.info("Ajuste los parametros en la barra lateral y presione 'Resolver Simulacion'.")


