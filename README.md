# PDF to JPG Converter

このツールは、PDFファイルをJPG画像に変換するPythonスクリプトです。各PDFページは個別のJPGファイルとして保存されます。

## 特徴

- ドラッグアンドドロップで簡単にPDFファイルを指定できます。
- PDFの各ページを個別のJPGファイルとして保存します。
- 出力されるJPG画像には元のPDFファイル名が含まれます。

## 前提条件

このスクリプトを実行する前に、以下のソフトウェアがシステムにインストールされている必要があります：

- Python 3.6以上
- Poppler for Windows

## インストール方法

### 1. Pythonのインストール

Pythonは[公式サイト](https://www.python.org/downloads/)からダウンロードしてインストールできます。

### 2. Popplerのインストール

- Popplerは[こちら](https://github.com/oschwartz10612/poppler-windows/releases)からダウンロードできます。
- ダウンロードしたファイルを解凍し、`C:\Program Files\`などの適切な場所に配置してください。
- 環境変数PATHにPopplerのbinディレクトリ（例: `C:\Program Files\poppler-xx\bin`）を追加してください。

### 3. 必要なPythonパッケージのインストール

コマンドプロンプトまたはターミナルを開き、以下のコマンドを実行してください。

```bash
pip install pdf2image pillow
```


## 使用方法

1. スクリプトをダウンロード後、任意のディレクトリに保存します。
2. コマンドプロンプトを開き、スクリプトが保存されているディレクトリに移動します。
3. スクリプトを実行するには以下のコマンドを入力します。

```python
python pdf_to_jpg.py
```


4. 表示されるメッセージに従って、変換したいPDFファイルをウィンドウにドラッグアンドドロップします。
5. 処理が完了すると、PDFファイルと同じディレクトリに新しいフォルダが作成され、その中に変換されたJPGファイルが保存されます。

## ライセンス

このプロジェクトは[GNU General Public License version 3 (GPLv3)](https://www.gnu.org/licenses/gpl-3.0.html)のもとで公開されています。

## 貢献

プルリクエストはいつでも歓迎します。大きな変更を提案する場合は、まずissueを開いて議論してください。

