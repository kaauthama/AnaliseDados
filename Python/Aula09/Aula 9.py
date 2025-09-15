# frase='Curso em video Pyton'
# print=(frase,[:15:2])

# # nome = input("Qual o seu nome? ")
# # print("Olá" , nome , " Prazer em te conhecer")

# import qrcode

# # Endereço de e-mail
# email = "kaauthama@gmail.com"

# # Criar o link 'mailto:'
# mailto_link = f"mailto:{email}"

# # Gerar o QR Code
# qr_img = qrcode.make(mailto_link)

# # Salvar a imagem
# qr_img.save("kaauthama_email_qrcode.png")

import qrcode

# URL do perfil do LinkedIn
linkedin_url = "https://www.linkedin.com/in/kaauthama-furtado-a63876231"

# Gerar o QR Code
qr_img = qrcode.make(linkedin_url)

# Salvar a imagem
qr_img.save("kaauthama_linkedin_qrcode.png")

# Exibir o QR Code (opcional)
qr_img.show()




