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
