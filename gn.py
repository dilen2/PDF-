import fitz
import os
from pdf2docx import Converter

def convert_pdf_to_word(pdf_path, output_docx_path):
    cv = Converter(pdf_path)
    cv.convert(output_docx_path, start=0, end=None)
    cv.close()

def pdf_to_images(pdf_path, output_folder, zoom=2.0):
    if not os.path.exists(output_folder): os.makedirs(output_folder)
    doc = fitz.open(pdf_path)
    base = os.path.splitext(os.path.basename(pdf_path))[0]
    for i in range(len(doc)):
        mat = fitz.Matrix(zoom, zoom)
        pix = doc.load_page(i).get_pixmap(matrix=mat)
        pix.save(os.path.join(output_folder, f"{base}_{i+1}.png"))
    doc.close()

def images_to_pdf(image_list, output_pdf_path):
    doc = fitz.open()
    for img_path in image_list:
        img_doc = fitz.open(img_path)
        doc.insert_pdf(fitz.open("pdf", img_doc.convert_to_pdf()))
        img_doc.close()
    doc.save(output_pdf_path)
    doc.close()

def merge_pdfs(pdf_list, output_path):
    doc = fitz.open()
    for pdf in pdf_list:
        if os.path.exists(pdf): doc.insert_pdf(fitz.open(pdf))
    doc.save(output_path)
    doc.close()

def split_pdf(pdf_path, output_folder):
    if not os.path.exists(output_folder): os.makedirs(output_folder)
    doc = fitz.open(pdf_path)
    base = os.path.splitext(os.path.basename(pdf_path))[0]
    for i in range(len(doc)):
        new_doc = fitz.open()
        new_doc.insert_pdf(doc, from_page=i, to_page=i)
        new_doc.save(os.path.join(output_folder, f"{base}_{i+1}.pdf"))
        new_doc.close()
    doc.close()