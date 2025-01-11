### scipy.cluster.hierarchy.dendrogram

**`dendrogram(Z, p=30, truncate_mode=None, color_threshold=None, get_leaves=True, orientation='top', labels=None, count_sort=False, distance_sort=False, show_leaf_counts=True, no_plot=False, no_labels=False, leaf_font_size=None, leaf_rotation=None, leaf_label_func=None, show_contracted=False, link_color_func=None, ax=None, above_threshold_color='C0')`**  

階層型クラスタリングをデンドログラムとしてプロットします。

デンドログラムは、非シングルトン（non-singleton）クラスタとその子クラスタ間の結合をU字型のリンクで示すことで、各クラスタの構成を可視化します。U字リンクの頂点はクラスタの結合を表し、U字の脚は結合されたクラスタを示します。脚の長さは子クラスタ間の距離を表し、元の観測値間のコフェネティック距離（cophenetic distance）でもあります。

---

### パラメータ:

- **`Z`（ndarray）**  
  階層型クラスタリングを表すリンク行列（linkage matrix）。デンドログラムの描画に使用します。Zの形式については`linkage`関数を参照してください。

- **`p`（int, オプション）**  
  `truncate_mode`の`p`パラメータ。

- **`truncate_mode`（str, オプション）**  
  観測データが多い場合、デンドログラムの可読性が低下します。`truncate_mode`はデンドログラムを簡略化するために使用します。以下のモードがあります：  
  - **None**: 簡略化しない（デフォルト）。  
  - **'lastp'**: リンク行列の最後のp個の非シングルトンなクラスタだけをノードとして表示し、それ以外のクラスタはリーフノードにまとめます。  
  - **'level'**: デンドログラムのpレベル以下のノードだけを表示します。

- **`color_threshold`（float, オプション）**  
  クラスタ間距離が`color_threshold`より小さいリンクを同じ色で表示します。デフォルトでは`0.7 * max(Z[:, 2])`に設定されます。

- **`get_leaves`（bool, オプション）**  
  結果辞書にリーフノードのリスト`R['leaves']`を含めます。

- **`orientation`（str, オプション）**  
  デンドログラムの描画方向。以下の値が使用できます：  
  - **'top'**: ルートが上にあり、リンクが下に向かう（デフォルト）。  
  - **'bottom'**: ルートが下にあり、リンクが上に向かう。  
  - **'left'**: ルートが左にあり、リンクが右に向かう。  
  - **'right'**: ルートが右にあり、リンクが左に向かう。

- **`labels`（ndarray, オプション）**  
  デフォルトでは、元の観測値のインデックスがリーフノードのラベルとして使用されます。他のラベルを指定する場合は、このパラメータにリストを渡します。

- **`count_sort`（strまたはbool, オプション）**  
  ノードの2つの子リンクの描画順序を指定します：  
  - **False**: 何もしない（デフォルト）。  
  - **'ascending'またはTrue**: 子クラスタ内の観測値数が少ない方を左に表示。  
  - **'descending'**: 子クラスタ内の観測値数が多い方を左に表示。

- **`distance_sort`（strまたはbool, オプション）**  
  ノードの2つの子リンクの描画順序を指定します：  
  - **False**: 何もしない（デフォルト）。  
  - **'ascending'またはTrue**: 子クラスタ間の距離が短い方を左に表示。  
  - **'descending'**: 子クラスタ間の距離が長い方を左に表示。

- **`show_leaf_counts`（bool, オプション）**  
  Trueの場合、リーフノードのラベルに括弧付きで観測値数を表示します。

- **`no_plot`（bool, オプション）**  
  Trueの場合、描画を行わずデータ構造だけを返します。

- **`no_labels`（bool, オプション）**  
  Trueの場合、リーフノードのラベルを表示しません。

- **`leaf_rotation`（float, オプション）**  
  リーフラベルを回転する角度を指定します（デフォルトは0度）。

- **`leaf_font_size`（int, オプション）**  
  リーフラベルのフォントサイズをポイントで指定します。

- **`leaf_label_func`（関数またはlambda式, オプション）**  
  リーフラベルをカスタマイズする関数を指定します。関数はクラスタインデックスを受け取り、ラベル文字列を返します。

```python
# First define the leaf label function.
def llf(id):
    if id < n:
        return str(id)
    else:
        return '[%d %d %1.2f]' % (id, count, R[n-id,3])

# The text for the leaf nodes is going to be big so force
# a rotation of 90 degrees.
dendrogram(Z, leaf_label_func=llf, leaf_rotation=90)

# leaf_label_func can also be used together with ``truncate_mode``,
# in which case you will get your leaves labeled after truncation:
dendrogram(Z, leaf_label_func=llf, leaf_rotation=90,
           truncate_mode='level', p=2)
```

- **`show_contracted`（bool, オプション）**  
  Trueの場合、縮約された非シングルトンノードの高さをリンク上にクロスで表示します。

- **`link_color_func`（関数, オプション）**  
  リンクの色を決定する関数を指定します。
```python
dendrogram(Z, link_color_func=lambda k: colors[k])
```

- **`ax`（matplotlib Axesインスタンス, オプション）**  
  Noneの場合、現在の軸に描画します。指定された場合、その軸にデンドログラムを描画します。

- **`above_threshold_color`（str, オプション）**  
  `color_threshold`より大きい距離のリンクの色を指定します（デフォルトは'C0'）。

---

### 戻り値:

- **`R`（辞書）**  
  デンドログラムを描画するためのデータ構造を含む辞書。以下のキーが含まれます：  
  - **'color_list'**: リンクごとの色のリスト。  
  - **'icoord'**, **'dcoord'**: 各リンクのx座標とy座標。  
  - **'ivl'**: リーフノードに対応するラベルのリスト。  
  - **'leaves'**: リーフノードの順序。

---

### 注意:
Z[:, 2]内の距離が単調でない場合、デンドログラムに交差が発生する可能性があります。

### 例:
```python
import numpy as np
from scipy.cluster import hierarchy
import matplotlib.pyplot as plt
```
```python
ytdist = np.array([662., 877., 255., 412., 996., 295., 468., 268.,
                   400., 754., 564., 138., 219., 869., 669.])
Z = hierarchy.linkage(ytdist, 'single')
plt.figure()
dn = hierarchy.dendrogram(Z)
```
```python
hierarchy.set_link_color_palette(['m', 'c', 'y', 'k'])
fig, axes = plt.subplots(1, 2, figsize=(8, 3))
dn1 = hierarchy.dendrogram(Z, ax=axes[0], above_threshold_color='y',
                           orientation='top')
dn2 = hierarchy.dendrogram(Z, ax=axes[1],
                           above_threshold_color='#bcbddc',
                           orientation='right')
hierarchy.set_link_color_palette(None)  # reset to default after use
plt.show()
```
![image](https://github.com/user-attachments/assets/b327f0b1-a43d-4dd2-9f95-9a89d415f8d2)
![image](https://github.com/user-attachments/assets/d41b5a8d-447d-48cb-b1f6-c4ae0cd0ec4d)
