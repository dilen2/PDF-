# PDF 智能工具箱

一个基于 Python 的本地 PDF 处理工具，集成 PDF 转 Word、转图片、图片合成 PDF、合并、拆分五类常用操作，全程离线运行，无需上传文件。

## 功能

- PDF 转 Word（.docx）
- PDF 转图片
- 多张图片合成 PDF
- 多个 PDF 合并
- PDF 拆分

## 技术栈

| 功能 | 库 |
| :--- | :--- |
| 图形界面 | PySimpleGUI |
| PDF 转 Word | pdf2docx |
| PDF 转图片 | pdf2image |
| 图片合成 PDF | Pillow |
| PDF 合并 / 拆分 | PyPDF2 |
| 路径处理 | os |
| 移动端界面骨架 | KivyMD |

## 安装

### 1. 安装 Python 依赖

```bash
pip install PySimpleGUI pdf2docx pdf2image Pillow PyPDF2
