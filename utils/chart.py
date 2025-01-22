import pandas as pd
import plotly.graph_objects as go
from data.constants import data

def create_chart(data, df, st):
    with st.container():
        st.header("📊 Datos de Producción")
    
    col1, col2 = st.columns([3, 2], gap="large")  
    
    with col1:
        fig = go.Figure()
        
        bar_width = 0.4
        bar_gap = 0.1
        
        fig.add_trace(go.Bar(
            x=df["Película"],
            y=df["Presupuesto (USD)"],
            name="Presupuesto",
            marker_color='#1f77b4',
            width=bar_width,
            offset=-bar_width/2
        ))
        
        fig.add_trace(go.Bar(
            x=df["Película"],
            y=df["Recaudación (USD)"],
            name="Recaudación",
            marker_color='#ff7f0e',
            width=bar_width,
            offset=bar_width/2
        ))
        
        fig.add_trace(go.Scatter(
            x=df["Película"],
            y=df["Puntaje Rotten Tomatoes"],
            name="Puntaje",
            line=dict(color='#2ca02c', width=3),
            yaxis='y2'
        ))
        
        # Layout mejorado
        fig.update_layout(
            title="Relación presupuesto, recaudación y puntaje",
            hovermode="x unified",
            barmode='group',
            bargap=bar_gap,
            height=600,
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1
            ),
            yaxis=dict(
                title="Monto en USD",
                titlefont=dict(color='#1f77b4'),
                tickfont=dict(color='#1f77b4'),
                gridcolor='#000000'
            ),
            yaxis2=dict(
                title="Puntaje (%)",
                titlefont=dict(color='#2ca02c'),
                tickfont=dict(color='#2ca02c'),
                overlaying='y',
                side='right',
                gridcolor='#f0f2f6'
            ),
            plot_bgcolor='#1a1a1a'
        )
        
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("📈 Estadísticas Clave")
        
        st.markdown("""
        <style>
            .metric-card {
                border: 1px solid #e6e6e6;
                border-radius: 10px;
                padding: 20px;
                margin: 10px 0;
                background: #1a1a1a;
                box-shadow: 0 2px 4px rgba(0,0,0,0.05);
            }
            .metric-title {
                font-size: 1.1em;
                color: #660;
                margin-bottom: 8px;
            }
        </style>
        """, unsafe_allow_html=True)
        
        mejor_peli = df.loc[df['Puntaje Rotten Tomatoes'].idxmax()]
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">🏆 Mejor Evaluada</div>
            <div style="font-size: 1.4em; font-weight: bold; color: #2ca02c;">
                {mejor_peli['Película']}
            </div>
            <div style="color: #666; margin-top: 8px;">
                Puntaje: {mejor_peli['Puntaje Rotten Tomatoes']}%
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        max_recaudacion = df['Recaudación (USD)'].max()
        peli_recaudacion = df.loc[df['Recaudación (USD)'].idxmax()]['Película']
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">💰 Mayor Recaudación</div>
            <div style="font-size: 1.4em; font-weight: bold; color: #ff7f0e;">
                ${max_recaudacion:,.0f}
            </div>
            <div style="color: #666; margin-top: 8px;">
                {peli_recaudacion}
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        promedio_presupuesto = df['Presupuesto (USD)'].mean()
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">📅 Presupuesto Promedio</div>
            <div style="font-size: 1.4em; font-weight: bold; color: #1f77b4;">
                ${promedio_presupuesto:,.2f}
            </div>
            <div style="color: #666; margin-top: 8px;">
                Base: {len(df)} películas
            </div>
        </div>
        """, unsafe_allow_html=True)
    