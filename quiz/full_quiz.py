import streamlit as st
from data.datasets import cargar_preguntas

def ejecutar_quiz():
    state_keys = ['quiz_answers', 'current_question', 'quiz_submitted']
    for key in state_keys:
        if key not in st.session_state:
            st.session_state[key] = {} if key == 'quiz_answers' else 0 if key == 'current_question' else False

    preguntas = cargar_preguntas()
    total_preguntas = len(preguntas)

    quiz_container = st.container()
    
    with quiz_container:
        if not st.session_state.quiz_submitted:
            i = st.session_state.current_question
            pregunta = preguntas[i]

            # Barra de progreso nativa
            st.progress((i + 1) / total_preguntas, text=f"Pregunta {i+1} de {total_preguntas}")

            # Tarjeta de pregunta
            with st.form(key=f'pregunta_{i}'):
                st.markdown(f"### {pregunta['pregunta']}")
                
                # Opciones de respuesta
                respuesta = st.radio(
                    "Selecciona tu respuesta:",
                    options=pregunta['opciones'],
                    index=None,
                    key=f"radio_{i}"
                )

                # Botones de navegación
                cols = st.columns([1, 3, 1])
                with cols[0]:
                    if i > 0 and st.form_submit_button("⬅️ Anterior"):
                        st.session_state.current_question -= 1
                        st.rerun()
                
                with cols[2]:
                    btn_text = "Siguiente ➡️" if i < total_preguntas - 1 else "Finalizar 🎉"
                    if st.form_submit_button(btn_text):
                        if respuesta:
                            st.session_state.quiz_answers[i] = respuesta
                            if i < total_preguntas - 1:
                                st.session_state.current_question += 1
                            else:
                                st.session_state.quiz_submitted = True
                            st.rerun()
                        else:
                            st.warning("Selecciona una respuesta antes de continuar")

        else:
            # Mostrar resultados
            st.subheader("📝 Resultados del Quiz")
            score = sum(1 for i in range(total_preguntas) 
                       if st.session_state.quiz_answers.get(i) == preguntas[i]['opciones'][preguntas[i]['correcta']])
            
            for i, pregunta in enumerate(preguntas):
                usuario = st.session_state.quiz_answers.get(i)
                correcta = pregunta['opciones'][preguntas[i]['correcta']]
                
                with st.container():
                    if usuario == correcta:
                        st.success(f"✅ **Pregunta {i+1}:** {pregunta['pregunta']}\n\n**Tu respuesta:** {usuario} (Correcta)")
                    else:
                        st.error(f"""❌ **Pregunta {i+1}:** {pregunta['pregunta']}
                                  \n**Tu respuesta:** {usuario or 'Ninguna'}
                                  \n**Respuesta correcta:** {correcta}""")

            st.balloons()
            st.markdown(f"""
            <div style='text-align: center; margin: 2rem 0;'>
                <h2 style='color: #FF4B4B;'>Puntuación: {score}/{total_preguntas}</h2>
                <h3>{'🏆 Dominas el Lynchverso' if score == total_preguntas 
                   else '🎬 Buen trabajo Lynchiano' if score > total_preguntas/2 
                   else '🌀 Sigue explorando el cine de Lynch'}</h3>
            </div>
            """, unsafe_allow_html=True)

            if st.form_submit_button("🔄 Reiniciar quiz", use_container_width=True):
                for key in state_keys:
                    st.session_state.pop(key, None)
                st.rerun()

    return quiz_container