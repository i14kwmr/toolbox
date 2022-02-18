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
