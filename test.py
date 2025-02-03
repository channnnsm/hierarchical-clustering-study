import numpy as np  
import pandas as pd  
from scipy.spatial.distance import pdist, squareform  
from scipy.cluster.hierarchy import linkage, dendrogram  
import matplotlib.pyplot as plt  
import japanize_matplotlib

# サンプルデータを作成  
# ここでは、4つのデータポイントを持つ2次元データを使用  
data = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])

# サンプルのuser_idを作成  
user_id = ['ユーザ1', 'ユーザ2', 'ユーザ3', 'ユーザ4']

# ペアワイズ距離を計算  
# pdistを使用して、データポイント間のユークリッド距離を計算  
distance_matrix = pdist(data, metric='euclidean')

# 距離行列を正方行列に変換  
# squareformを使用して、1次元の距離ベクトルを2次元の正方行列に変換  
distance_matrix_square = squareform(distance_matrix)

# 距離行列をDataFrameとして表示  
# 距離行列をpandasのDataFrameに変換し、行と列のラベルをuser_idに設定  
distance_df = pd.DataFrame(distance_matrix_square,   
                           index=user_id,   
                           columns=user_id)

# 距離行列を表示  
print("距離行列 (正方行列形式):")  
print(distance_df)

# 階層的クラスタリングを実行  
# linkageを使用して、距離行列から階層クラスタリングを実行  
# ここでは、Ward法を使用
linkage_matrix = linkage(distance_matrix, method='ward')

# デンドログラムを描画  
# 階層クラスタリングの結果をデンドログラムとして視覚化  
plt.figure()  
dendrogram(linkage_matrix, labels=user_id)  
plt.title("デンドログラム")  
plt.xlabel("データポイント")  
plt.ylabel("距離")  
plt.show()  
