import tkinter as tk
from tkinter import scrolledtext, ttk
import pyperclip
import re


def convert_markdown_table_to_tsv(table):
    # 解析Markdown表格
    rows = table.strip().split("\n")
    headers = [cell.strip() for cell in rows[0].split("|")]
    headers = headers[1:-1]
    data = []

    # 跳过第二行（通常是列分隔线）
    for row in rows[2:]:
        cells = [cell.strip() for cell in row.split("|")]
        cells = cells[1:-1]
        data.append(cells)

    # 转换为制表符分隔的文本
    tsv_table = "\t".join(headers) + "\n"
    for row in data:
        tsv_table += "\t".join(row) + "\n"

    return tsv_table


def replace_markdown_tables_with_tsv(markdown_text):
    # 使用正则表达式匹配Markdown表格
    pattern = r"((^\|(.+?)\|$\n)+)"
    matches = re.findall(pattern, markdown_text, re.M)
    # 替换每个匹配到的表格
    for match in matches:
        tsv_table = convert_markdown_table_to_tsv(match[0])
        markdown_text = markdown_text.replace(match[0], "```\n" + tsv_table + "```\n")

    return markdown_text


def do_convert():
    # 获取Markdown文本框中的内容
    markdown_text = text_md_area.get("0.0", "end-1c")

    # 统一换行符
    markdown_text = markdown_text.replace("\r\n", "\n")
    markdown_text = markdown_text.replace("\r", "\n")

    # 替换Markdown表格为制表符分隔的文本
    converted_text = replace_markdown_tables_with_tsv(markdown_text)

    # 显示转换结果
    text_excel_area.delete("1.0", tk.END)
    text_excel_area.insert(tk.END, converted_text)

    # 如果用户选择了自动复制，则复制结果到剪贴板
    if auto_copy_var.get():
        pyperclip.copy(converted_text)


# 创建主窗口
root = tk.Tk()
root.title("Markdown表格转Excel表格")

# 添加markdown表格文本输入框
label_md_area = ttk.Label(root, text="Markdown文本：")
label_md_area.pack(pady=5)
text_md_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10)
text_md_area.pack(padx=10, pady=5)

# 添加“自动复制转换结果”选择框
auto_copy_var = tk.IntVar(value=1)
auto_copy_check = ttk.Checkbutton(root, text="自动复制转换结果", variable=auto_copy_var)
auto_copy_check.pack(pady=10)

# 添加转换按钮
start_button = ttk.Button(root, text="转换", command=do_convert, padding=5)
start_button.pack(pady=20)

# 添加excel表格文本显示框
label_excel_area = ttk.Label(root, text="转换后的文本：")
label_excel_area.pack(pady=5)
text_excel_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10)
text_excel_area.pack(padx=10, pady=5)

# 运行主循环
root.mainloop()
