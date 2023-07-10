import PyPDF2
from reportlab.pdfgen import canvas


def generate_summary_pdf(input_file, output_file, summary_text):
    # 打开输入的 PDF 文件
    with open(input_file, 'rb') as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        # 创建一个新的 PDF 文件
        with open(output_file, 'wb') as output:
            pdf_writer = PyPDF2.PdfFileWriter()

            # 从输入的 PDF 文件中提取第一页
            first_page = pdf_reader.getPage(0)

            # 将提取的第一页添加到新的 PDF 文件中
            pdf_writer.addPage(first_page)

            # 在新的 PDF 文件中添加总结文本
            c = canvas.Canvas(output)
            c.setFont("Helvetica", 12)
            c.drawString(50, 50, summary_text)
            c.save()

            # 将新的 PDF 文件合并到输出文件中
            pdf_writer.write(output)

    print(f"生成总结 PDF 文件成功！保存为：{output_file}")


# 示例用法
input_pdf_file = 'C:/Users/Polo/Desktop/工程伦理小作业 2020212118 彭松焕.pdf'  # 输入的 PDF 文件路径
output_pdf_file = 'output.pdf'  # 输出的总结 PDF 文件路径
summary = "这是一个示例总结。"  # 要添加到总结 PDF 文件中的文本

generate_summary_pdf(input_pdf_file, output_pdf_file, summary)
