awk -f logExtract.awk .\150Epochs\logs_cifar_vgg_150MR1bgr.out > .\150Epochs\BGR.csv
awk -f logExtract.awk .\150Epochs\logs_cifar_vgg_150MR1brg.out > .\150Epochs\BRG.csv
awk -f logExtract.awk .\150Epochs\logs_cifar_vgg_150MR1gbr.out > .\150Epochs\GBR.csv
awk -f logExtract.awk .\150Epochs\logs_cifar_vgg_150MR1grb.out > .\150Epochs\GRB.csv
awk -f logExtract.awk .\150Epochs\logs_cifar_vgg_150MR1rbg.out > .\150Epochs\RBG.csv
awk -f logExtract.awk .\150Epochs\logs_cifar_vgg_150MR1rgb.out > .\150Epochs\RGB.csv
