def save_markdown_report(report_text: str, output_path: str):
    """把生成的报告文本保存成md文件"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(report_text)
    return output_path

