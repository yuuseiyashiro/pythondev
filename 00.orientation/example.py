zeinukikakaku=input("税抜き価格を入力してください")
zeikomikakaku=int(zeinukikakakaku)*1.1
if zeikomikakaku>=2000:
    print("送料は無料です")
else:
    print("送料は350円です")
    zeikomikakaku+=350
    print("価格は",zeikomikakaku,"円です。")
