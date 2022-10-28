#!/bin/sh

template_name=$1
tar -xvf $template_name.tar
cd $template_name

# 文字コードの確認
nkf -g sample.tex

# 文字コードをUTF-8に変更
nkf -w --overwrite sample.tex
nkf -w --overwrite onkoron.sty
nkf -g sample.tex
