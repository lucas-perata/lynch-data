import fpdf

def generar_pdf(pelicula, datos, word_count, sentences_with_words, df):
    # Crear el PDF
    pdf = fpdf.FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Título del reporte
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt=f"Reporte: {pelicula}", ln=1, align='C')
    pdf.ln(10)
    
    # Sección de datos generales
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="Datos Generales", ln=1)
    pdf.set_font("Arial", size=12)
    
    # Obtener datos de la película
    pelicula_data = df[df["Película"] == pelicula].iloc[0]
    pdf.cell(200, 10, txt=f"Presupuesto: ${pelicula_data['Presupuesto (USD)']:,}", ln=1)
    pdf.cell(200, 10, txt=f"Recaudación: ${pelicula_data['Recaudación (USD)']:,}", ln=1)
    pdf.cell(200, 10, txt=f"Puntaje Rotten Tomatoes: {pelicula_data['Puntaje Rotten Tomatoes']}%", ln=1)
    pdf.ln(10)
    
    # Sección de análisis de palabras clave
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="Análisis de Palabras Clave", ln=1)
    pdf.set_font("Arial", size=12)
    
    for word, count in word_count.most_common():
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(200, 10, txt=f"Palabra: {word.capitalize()} (Frecuencia: {count})", ln=1)
        pdf.set_font("Arial", size=12)
        
        # Mostrar hasta 3 oraciones de ejemplo
        filtered_sentences = list(filter(lambda x: word in x[1], sentences_with_words))[:3]
        for sentence, _ in filtered_sentences:
            pdf.multi_cell(0, 10, txt=f"- {sentence}")
        pdf.ln(5)
    
    # Guardar el PDF
    pdf.output(f"reporte_{pelicula}.pdf")
    return pdf