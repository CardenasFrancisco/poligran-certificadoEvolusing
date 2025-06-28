import qrcode

# URL fija de tu página
url = "https://poligranevolusing.netlify.app/"

# Crear el objeto QR
qr = qrcode.QRCode(
    version=1,  # Controla el tamaño: 1 (más pequeño) a 40 (más grande)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # Alta corrección de errores
    box_size=10,  # Tamaño de cada caja en pixeles
    border=4,  # Borde blanco (mínimo recomendado: 4)
)

# Agregar la URL
qr.add_data(url)
qr.make(fit=True)

# Generar imagen
img = qr.make_image(fill_color="black", back_color="white")

# Guardar
img.save("qr_poligranevolusing.png")

print("✅ Código QR generado correctamente. Archivo: qr_poligranevolusing.png")
