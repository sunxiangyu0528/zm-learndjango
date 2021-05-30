# import qrcode as qrcode
# from PIL import Image
# qr = qrcode.QRCode(
#     version=1,
#     error_correction=qrcode.constants.ERROR_CORRECT_L,
#     box_size=10,
#     border=2,
# )
# # 添加数据
# qr.add_data("sunxy,i love you")
# # 填充数据
# qr.make(fit=True)
# # 生成图片
# img = qr.make_image(fill_color="pink", back_color="white")
#
# # 添加logo
# icon = Image.open("img.png")
# # 获取图片的宽高
# img_w, img_h = img.size
# img.paste(icon, (600, 600), icon)
# img.show()
import os
import sys
print(os.path.join(sys.path[0],'apps'))