### **リンクエージ (linkage)**

`linkage(y, method='single', metric='euclidean', optimal_ordering=False)[source]`

階層的（凝集型）クラスタリングを実行します。

入力として渡す `y` は、1次元の凝縮距離行列（condensed distance matrix）または2次元の観測データ行列のいずれかである必要があります。

---

#### **1. 入力の詳細**
- **1次元の凝縮距離行列の場合**  
  `y` は \( \\binom{n}{2} \) のサイズのベクトルである必要があります。ここで \( n \) は元の観測値の数を指します。この形式は MATLAB の `linkage` 関数と非常に似ています。

- **出力**  
  \( (n-1) \\times 4 \) の行列 \( Z \) が返されます。  
  - \( i \)-回目のイテレーションでは、クラスター \( Z[i, 0] \) と \( Z[i, 1] \) が統合されて新しいクラスターが形成されます。
  - \( Z[i, 2] \) は統合されたクラスター間の距離を示し、\( Z[i, 3] \) は新しいクラスターに含まれる元の観測値の数を表します。

---

#### **2. リンクエージ法（Linkage Methods）**
次のリンクエージ法を使用して、2つのクラスター間の距離を計算します：

1. **`single`（単一リンク法）**  
   - 最も近い点同士の距離（Nearest Point Algorithm）。

2. **`complete`（完全リンク法）**  
   - 最も遠い点同士の距離（Farthest Point Algorithm または Voor Hees Algorithm）。

3. **`average`（平均リンク法）**  
   - クラスター内の全ての点間の平均距離（UPGMA）。

4. **`weighted`（重み付き平均法）**  
   - WPGMA としても知られる方法。

5. **`centroid`（重心法）**  
   - 各クラスターの重心間の距離（UPGMC）。

6. **`median`（中央値法）**  
   - 2つのクラスターの重心の平均を使用（WPGMC）。

7. **`ward`（ウォード法）**  
   - 分散の最小化アルゴリズム（インクリメンタルアルゴリズム）。

---

#### **3. 注意点**
- 最小距離のクラスターを選ぶ際、距離が同じ場合に MATLAB と異なる結果を選ぶ可能性があります。
- 方法 `centroid`, `median`, `ward` はユークリッド距離を仮定しています。それ以外の距離を使用した場合、結果が正しくない可能性があります。

---

#### **4. パラメータ**
- **`y`**  
  - 凝縮距離行列（`pdist` 関数が返す形式）または \( n \\times m \) の観測ベクトル行列。
  - 無限大（`inf`）や `NaN` を含んではいけません。

- **`method`**（デフォルト：`single`）  
  - 使用するリンクエージ法。

- **`metric`**（デフォルト：`euclidean`）  
  - 観測ベクトルを使う場合の距離の計算方法。

- **`optimal_ordering`**（デフォルト：`False`）  
  - クラスターの視覚化を直感的にするために、連続するリーフ間の距離を最小化するようリンクエージ行列を並べ替えるかどうか。

---

#### **5. 戻り値**
- **`Z`**（リンクエージ行列）  
  - 階層クラスタリングをエンコードした \( (n-1) \\times 4 \) の NumPy 配列。

---

#### **6. 参考**
- **`scipy.spatial.distance.pdist`**：ペア間距離計算
- **ペアワイズ距離のメトリック**

---

#### **7. メモ**
- `single` メソッドでは最小スパニングツリーに基づく最適化されたアルゴリズムが使用され、計算量は \( O(n^2) \) です。
- `complete`, `average`, `weighted`, `ward` メソッドでは最近傍チェインアルゴリズムが使用され、計算量は \( O(n^2) \) です。
- 他のメソッドでは、ナイーブなアルゴリズムを使用し、計算量は \( O(n^3) \) です。

---

#### **8. 実例**
```python
from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt

X = [[i] for i in [2, 8, 0, 4, 1, 9, 9, 0]]

# ウォード法でリンクエージ行列を計算
Z = linkage(X, 'ward')
fig = plt.figure(figsize=(25, 10))
dn = dendrogram(Z)

# 単一リンク法でリンクエージ行列を計算
Z = linkage(X, 'single')
fig = plt.figure(figsize=(25, 10))
dn = dendrogram(Z)

plt.show()
```
![image](https://github.com/user-attachments/assets/e8be3504-ec9d-4b89-8335-f5cbd88de955)
![image](https://github.com/user-attachments/assets/6c49477d-6450-48db-b673-56792f307b68)
