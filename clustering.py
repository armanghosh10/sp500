from sklearn.cluster import KMeans

target_rsi_values = [30,45,55,70]
initial_centroids = np.zeros((len(target_rsi_values),18))
initial_centroids[:,6] = target_rsi_values
initial_centroids

def get_clusters(stock_data):
    stock_data['cluster'] = KMeans(n_clusters=4,
                                   random_state=0,
                                   init=initial_centroids).fit(stock_data).labels_
    return stock_data

data = data.dropna().groupby('date',group_keys=False).apply(get_clusters)

def plot_clusters(stock_data):
    
    cluster_0 = stock_data[stock_data['cluster']==0]
    cluster_1 = stock_data[stock_data['cluster']==1]
    cluster_2 = stock_data[stock_data['cluster']==2]
    cluster_3 = stock_data[stock_data['cluster']==3]

    plt.scatter(cluster_0.iloc[:,0], cluster_0.iloc[:,3], color='red', label='cluster 0')
    plt.scatter(cluster_1.iloc[:,0], cluster_1.iloc[:,3], color='green', label='cluster 1')
    plt.scatter(cluster_2.iloc[:,0], cluster_2.iloc[:,3], color='blue', label='cluster 2')
    plt.scatter(cluster_3.iloc[:,0], cluster_3.iloc[:,3], color='black', label='cluster 3')
    
    plt.legend()
    plt.show()
    return 
