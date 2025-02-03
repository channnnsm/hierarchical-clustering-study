from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt

X = [[i] for i in [2, 8, 0, 4, 1, 9, 9, 0]]

# ウォード法でリンクエージ行列を計算
Z_ward = linkage(X, 'ward')
fig = plt.figure(figsize=(15, 5))
dn_ward = dendrogram(Z_ward)
plt.title('dn-ward', fontsize=14, pad=20)  # タイトルを追加

# 単一リンク法でリンクエージ行列を計算
Z_single = linkage(X, 'single')
fig = plt.figure(figsize=(15, 5))
dn_single = dendrogram(Z_single)
plt.title('dn-single', fontsize=14, pad=20)  # タイトルを追加

plt.show()
