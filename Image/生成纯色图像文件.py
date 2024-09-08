from PIL import Image

# 定义图像的宽度、高度和颜色
width, height = 800, 600  # 图像大小
color = (255, 0, 0)  # 颜色
color_name = "红色"  # 颜色名称
image = Image.new("RGB", (width, height), color)  # 创建纯色图像

# 保存图像到文件
image.save(f"{color_name}.png")

print(f"纯色图像已生成并保存为{color_name}.png")
