import PySimpleGUI as sg
import os
import gn

def main():
    bg_color = '#FFFFFF'
    sg.theme_background_color(bg_color)
    
    # 封装功能项：固定宽度以保证整齐对齐
    def make_item(icon, title, desc, key):
        return sg.Column([
            [sg.Button("", image_filename=icon, image_subsample=5, border_width=0, 
                       button_color=(bg_color, bg_color), key=key),
             sg.Column([
                 [sg.Text(title, font=("微软雅黑", 12, "bold"), text_color="#333333", background_color=bg_color)],
                 [sg.Text(desc, font=("微软雅黑", 9), text_color="#777777", background_color=bg_color)]
             ], pad=(0, 0), background_color=bg_color)]
        ], pad=(10, 5), background_color=bg_color, size=(250, 80)) # 固定宽高，防止歪斜

    layout = [
        [sg.Text("PDF 智能工具箱", font=("微软雅黑", 16, "bold"), pad=(20, 20), 
                 text_color="#333333", background_color=bg_color)],
        
        # 第一行
        [make_item("icons/word.png", "转 Word", "将 PDF 转换为 Word", "-DO-P2W-"),
         make_item("icons/img.png", "转 图片", "将 PDF 导出为图片", "-DO-P2I-")],
        
        # 第二行
        [make_item("icons/pdf.png", "图片转 PDF", "多张图片合成 PDF", "-DO-I2P-"),
         make_item("icons/merge.png", "合并 PDF", "多个 PDF 合并", "-DO-MERGE-")],
        
        # 第三行（为了对齐，可以用 Column 占位，或者单独放一行）
        [make_item("icons/split.png", "拆分 PDF", "PDF 页面拆分", "-DO-SPLIT-"),
         sg.Column([], size=(250, 80), background_color=bg_color)]
    ]

    # 重点：icon 参数必须是 .ico 文件
    window = sg.Window("PDF 工具箱", layout, finalize=True, 
                       background_color=bg_color, 
                       icon="icons/logo.ico", 
                       element_justification='center')
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED: break
        
        
        try:
            # 统一处理逻辑：点击图标后，先让用户选文件，再执行
            if event == "-DO-P2W-":
                files = sg.popup_get_file("选择 PDF 文件:", multiple_files=True)
                if files:
                    out_dir = sg.popup_get_folder("选择保存 Word 的文件夹:")
                    if out_dir:
                        for f in files.split(";"):
                            name = os.path.splitext(os.path.basename(f))[0]
                            gn.convert_pdf_to_word(f, os.path.join(out_dir, name + ".docx"))
                        sg.popup("完成！")

            elif event == "-DO-P2I-":
                f = sg.popup_get_file("选择 PDF 文件:")
                if f:
                    out_dir = sg.popup_get_folder("选择保存图片的文件夹:")
                    if out_dir:
                        gn.pdf_to_images(f, os.path.join(out_dir, os.path.splitext(os.path.basename(f))[0]))
                        sg.popup("完成！")

            elif event == "-DO-I2P-":
                files = sg.popup_get_file("选择图片文件:", multiple_files=True)
                if files:
                    save_path = sg.popup_get_file("保存为:", save_as=True, default_extension=".pdf")
                    if save_path:
                        gn.images_to_pdf(files.split(";"), save_path)
                        sg.popup("完成！")

            elif event == "-DO-MERGE-":
                files = sg.popup_get_file("选择要合并的 PDF (Ctrl多选):", multiple_files=True)
                if files:
                    save_path = sg.popup_get_file("保存合并后的文件:", save_as=True, default_extension=".pdf")
                    if save_path:
                        gn.merge_pdfs(files.split(";"), save_path)
                        sg.popup("完成！")

            elif event == "-DO-SPLIT-":
                f = sg.popup_get_file("选择要拆分的 PDF:")
                if f:
                    out_dir = sg.popup_get_folder("选择保存拆分文件的文件夹:")
                    if out_dir:
                        gn.split_pdf(f, out_dir)
                        sg.popup("完成！")

        except Exception as e:
            sg.popup_error(f"发生错误: {e}")

    window.close()

if __name__ == "__main__":
    main()