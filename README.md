# hierarchical-clustering-study

以下のSciPyのドキュメントの日本語訳

https://docs.scipy.org/doc/scipy-1.15.0/reference/cluster.hierarchy.html

### 階層クラスタリング (scipy.cluster.hierarchy)
これらの関数は、階層クラスタリングをフラットクラスタリングに分割したり、カットによって形成されるフォレストのルートを見つけたりするために使用されます。それぞれの観測値に対応するフラットクラスタIDを提供します。

- **fcluster(Z, t[, criterion, depth, R, monocrit])**  
  指定されたリンク行列に基づいて、階層クラスタリングからフラットクラスタを形成します。

- **fclusterdata(X, t[, criterion, metric, ...])**  
  指定された距離尺度を使用して観測データをクラスタリングします。

- **leaders(Z, T)**  
  階層クラスタリングにおけるルートノードを返します。

---

### 凝集型クラスタリングのルーチン
- **linkage(y[, method, metric, optimal_ordering])**  
  階層的/凝集型クラスタリングを実行します。

- **single(y)**  
  condensed距離行列 `y` に対して、単一/最小/最近隣法リンクを実行します。

- **complete(y)**  
  condensed距離行列 `y` に対して、完全/最大/最遠点リンクを実行します。

- **average(y)**  
  condensed距離行列 `y` に対して、平均/UPGMAリンクを実行します。

- **weighted(y)**  
  condensed距離行列 `y` に対して、加重/WPGMAリンクを実行します。

- **centroid(y) / 重心法**  
  セントロイド/UPGMCリンクを実行します。  
  UPGMC=Unweighted Pair Group Method using Centroids  
  各クラスタのサイズに関係なく同じ重みを割り当てます  

- **median(y) / メディアン法**  
  メディアン/WPGMCリンクを実行します。  
  WPGMC=Weighted Pair Group Method using Centroids  
  クラスタのサイズに基づいて距離に重みを付けます  
  大きなクラスタが小さなクラスタに比べて距離計算においてより影響を与えるようになる  

- **ward(y)**  
  condensed距離行列 `y` に対してウォード法リンクを実行します。

---

### 階層に関する統計の計算ルーチン
- **cophenet(Z[, Y])**  
  リンク行列 `Z` で定義された階層クラスタリングにおける観測値間のコフェネティック距離を計算します。

- **from_mlab_linkage(Z)**  
  MATLAB(TM)で生成されたリンク行列を、このモジュールに互換性のあるリンク行列に変換します。

- **inconsistent(Z[, d])**  
  リンク行列の不一致統計を計算します。

- **maxinconsts(Z, R)**  
  非単一クラスタおよびその子の最大不一致係数を返します。

- **maxdists(Z)**  
  非単一クラスタ間の最大距離を返します。

- **maxRstat(Z, R, i)**  
  非単一クラスタおよびその子の最大統計量を返します。

- **to_mlab_linkage(Z)**  
  リンク行列をMATLAB(TM)互換のものに変換します。

---

### フラットクラスタの可視化ルーチン
- **dendrogram(Z[, p, truncate_mode, ...])**  
  階層クラスタリングをデンドログラムとしてプロットします。

---

### 階層を木構造として表現するためのデータ構造とルーチン
- **ClusterNode(id[, left, right, dist, count])**  
  クラスタを表すためのツリーノードクラス。

- **leaves_list(Z)**  
  葉ノードのIDリストを返します。

- **to_tree(Z[, rd])**  
  リンク行列を使いやすいツリーオブジェクトに変換します。

- **cut_tree(Z[, n_clusters, height])**  
  リンク行列 `Z` に基づきカットツリーを返します。

- **optimal_leaf_ordering(Z, y[, metric])**  
  リンク行列 `Z` と距離に基づき、カットツリーを再配置します。

---

### 妥当性チェックと等価性の判定
- **is_valid_im(R[, warning, throw, name])**  
  提供された不一致行列が有効であればTrueを返します。

- **is_valid_linkage(Z[, warning, throw, name])**  
  リンク行列の妥当性をチェックします。

- **is_isomorphic(T1, T2)**  
  2つの異なるクラスタ割り当てが等価であるかを判定します。

- **is_monotonic(Z)**  
  提供されたリンク行列が単調であればTrueを返します。

- **correspond(Z, Y)**  
  リンク行列と凝縮距離行列の対応をチェックします。

- **num_obs_linkage(Z)**  
  提供されたリンク行列の元の観測数を返します。

---

### プロットのユーティリティルーチン
- **set_link_color_palette(palette)**  
  デンドログラムで使用するmatplotlibカラーコードのリストを設定します。

---

### ユーティリティクラス
- **DisjointSet([elements])**  
  境界の接続クエリに使用される不連結集合データ構造。
