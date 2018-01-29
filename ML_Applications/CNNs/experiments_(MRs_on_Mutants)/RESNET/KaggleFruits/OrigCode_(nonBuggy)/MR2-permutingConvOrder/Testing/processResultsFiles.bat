awk -f extractResults.awk .\150Epochs\results_kaggle_fruits-data_mr3_originalData.out > .\150Epochs\originalData.csv
awk -f extractResults.awk .\150Epochs\results_kaggle_fruits-data_mr3_rotate90.out > .\150Epochs\rotate90.csv
awk -f extractResults.awk .\150Epochs\results_kaggle_fruits-data_mr3_rotate90transpose.out > .\150Epochs\rotate90transpose.csv
awk -f extractResults.awk .\150Epochs\results_kaggle_fruits-data_mr3_rotate180.out > .\150Epochs\rotate180.csv
awk -f extractResults.awk .\150Epochs\results_kaggle_fruits-data_mr3_rotate180transpose.out > .\150Epochs\rotate180transpose.csv
awk -f extractResults.awk .\150Epochs\results_kaggle_fruits-data_mr3_rotate270.out > .\150Epochs\rotate270.csv
awk -f extractResults.awk .\150Epochs\results_kaggle_fruits-data_mr3_rotate270transpose.out > .\150Epochs\rotate270transpose.csv
awk -f extractResults.awk .\150Epochs\results_kaggle_fruits-data_mr3_transpose.out > .\150Epochs\transpose.csv
