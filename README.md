# toolbox

作業の効率化を行うプログラムをまとめる．

* load\_pickle.py
  
  * pickleファイルをロードするプログラム
  
  * 使い方（コマンドライン）
    
    ```
    python load_pickle.py ./sample.pickle
    # ./sample.pickleの内容が表示される．
    ```
  
  * 使い方（プログラム）
    
    ```python
    from load_pickle import load_pickle
    
    file_name = "./sample.pickle"
    data = load_pickle(file_name)
    print(data)  # ./sample.pickleの内容が表示される．
    ```

* convert\_wav\_to\_mp3.wav
  
  * wavファイルをmp3ファイルに変換する
  
  * プログラム使い方（コマンドライン）
    
    ```
    python load_pickle.py ./sample.wav
    # ./sample.mp3が書き出される＋wavとmp3の波形表示される．
    ```
  
  * 使い方（プログラム）
    
    ```python
    from convert_wav_to_mp3 import convert_wav_to_mp3
    
    file_name = "./sample.wav"
    convert_wav_to_mp3(file_name)  # ./sample.mp3が書き出される．
    ```

* convert\_template.sh

  * [日本音響学会の大会原稿をOverleafで書く方法](https://scrapbox.io/k-yasu/%E6%97%A5%E6%9C%AC%E9%9F%B3%E9%9F%BF%E5%AD%A6%E4%BC%9A%E3%81%AE%E5%A4%A7%E4%BC%9A%E5%8E%9F%E7%A8%BF%E3%82%92Overleaf%E3%81%A7%E6%9B%B8%E3%81%8F%E6%96%B9%E6%B3%95)の「2. UTF-8に文字コードを変更」を実行するシェルスクリプト．

  * 使い方（コマンドライン）

    1. テンプレートファイル([filename].tar)を同じ階層のフォルダにダウンロード．
    3. `convert_template.sh`を実行
    ```
    ./convert_template.sh [filename]
    ```
    3. [filename]フォルダ内のファイルの文字コードがUTF-8に変わっている．