import qrcode

generate_image = qrcode.make("https://www.youtube.com/")
generate_image.save('image1.png')