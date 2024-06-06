import os
from pdf2image import convert_from_path


def convert_pdf_to_jpg(pdf_path):
    # ファイルパスの前後の余分なクオートを削除（ドラッグアンドドロップ時に追加されることがある）
    pdf_path = pdf_path.strip('"')

    # PDFファイル名を取得（拡張子なし）
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]

    # PDFを画像リストとして読み込む
    images = convert_from_path(pdf_path, dpi=200)

    # 出力フォルダを決定
    output_folder = os.path.splitext(pdf_path)[0] + '_images'
    os.makedirs(output_folder, exist_ok=True)

    # 画像を一つずつ保存する
    for i, image in enumerate(images):
        image_path = os.path.join(output_folder, f'{base_name}_page_{i + 1}.jpg')
        image.save(image_path, 'JPEG')
        print(f'Saved: {image_path}')


if __name__ == "__main__":
    print("PDFファイルをこのウィンドウにドラッグアンドドロップしてください。")
    pdf_path = input("ここにファイルパスをドロップ: ")
    convert_pdf_to_jpg(pdf_path)
