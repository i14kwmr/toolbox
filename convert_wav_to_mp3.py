import argparse
import os

import ffmpeg
import librosa
import matplotlib.pyplot as plt


def convert_mp3_to_wav(fname):

    fname = os.path.splitext(os.path.basename(fname))[0]

    stream = ffmpeg.input(f"{fname}.wav")  # 入力
    stream = ffmpeg.output(stream, f"{fname}.mp3")  # 出力
    ffmpeg.run(stream)  # 実行


def confirm_convert(fname):

    fs = 16000  # 確認用
    fname = os.path.splitext(os.path.basename(fname))[0]

    sig_wav, _ = librosa.load(f"{fname}.wav", mono=False, sr=fs)
    sig_mp3, _ = librosa.load(
        f"{fname}.mp3", mono=False, sr=fs
    )  # https://github.com/librosa/librosa/issues/1015

    plt.subplot(2, 1, 1)
    plt.plot(sig_wav[0], label="wav")
    plt.plot(sig_mp3[0], label="mp3")
    plt.plot(sig_wav[0] - sig_mp3[0], label="err")

    plt.subplot(2, 1, 2)
    plt.plot(sig_wav[1], label="wav")
    plt.plot(sig_mp3[1], label="mp3")
    plt.plot(sig_wav[1] - sig_mp3[1], label="err")

    plt.legend()
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("fname")
    args = parser.parse_args()

    # 変換
    convert_mp3_to_wav(args.fname)

    # 確認
    confirm_convert(args.fname)
