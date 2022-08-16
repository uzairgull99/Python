# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import math
import numpy as np
import re
import pandas as pd
import matplotlib.pyplot as plt


def main():
    dic = {}
    refined_array = []
    firstValue_array = []
    secondValue_array = []
    iris_class = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
    target = []
    array = []
    file = open("irris data.txt", "r")

    # index=0
    for i in range(150):
        line = file.readline().strip().split('\n')
        # (p_len,p_width,s_len,s_width)=file.strip(",")
        array.append(line)
        if i <= 50:
            target.append(0)
        elif i >= 51 and i <= 100:
            target.append(1)
        elif i >= 101:
            target.append(2)

    #    print(array)

    array_length = len(array)
    count = 0
    for i in range(array_length):
        str = ""
        for element in array[count]:
            str += element

        # search using regex
        x = re.findall('[0-9]+.[0-9]', str)
        new_x = np.array(x)
        y = new_x.astype(float)

        refined_array.append(y)

        firstValue_array.append(math.sqrt((refined_array[count][0]) * (refined_array[count][2])))
        secondValue_array.append(math.sqrt(refined_array[count][1] * (refined_array[count][3])))
        # new_array.append(refined_array[count][2])
        # new_array.append(refined_array[count][3])

        count += 1

    array_length = len(refined_array)
    print(array_length)
    print(target)
    print(refined_array[0][0])
    print(firstValue_array)

    print(len(firstValue_array))
    print(len(secondValue_array))
    print(len(target))
    df = pd.DataFrame({
        'x': firstValue_array,
        'y': secondValue_array,
        'cluster': target
    })

    print(df)

    centroids = {}

    for i in range(3):
        result_list = []
        result_list.append(df.loc[df['cluster'] == i]['x'].mean())
        result_list.append(df.loc[df['cluster'] == i]['y'].mean())
        centroids[i] = result_list

    print(result_list)
    print(centroids)

    # -------------Showing data points only ---------------

    # figure=plt.figure(figure=(5,5))
    plt.scatter(df['x'], df['y'], c=target, cmap='gist_rainbow')
    plt.xlabel('Sepal Length', fontsize=10)
    plt.ylabel('Sepal width', fontsize=10)
    plt.show()

    # -------------Showing centoroids only---------------

    color = {0: 'r', 1: 'g', 2: 'b'}
    for i in range(3):
        plt.scatter(centroids[i][0], centroids[i][1], color=color[i])
    plt.show()

    # -------------Showing both data points and centoroids ---------------

    plt.scatter(df['x'], df['y'], c=target, cmap='gist_rainbow', alpha=0.3)
    plt.xlabel('Sepal Length', fontsize=10)
    plt.ylabel('Sepal width', fontsize=10)
    color = {0: 'r', 1: 'g', 2: 'b'}
    for i in range(3):
        plt.scatter(centroids[i][0], centroids[i][1], color=color[i], edgecolors='k')

    plt.show()

    def assignment(df, centroids):
        for i in range(3):
            df['distance_from_{}'.format(i)] = (
                np.sqrt((df['x'] - centroids[i][0]) ** 2 + (df['y'] - centroids[i][1]) ** 2))

        centroid_distance_cols = ['distance_from_{}'.format(i) for i in centroids.keys()]
        df['closest'] = df.loc[:, centroid_distance_cols].idxmin(axis=1)
        df['closest'] = df['closest'].map(lambda x: int(x.lstrip('distance_from_')))
        df['color'] = df['closest'].map(lambda x: color[x])
        return df

    df = assignment(df, centroids)

    print(df)

    # -------------Showing both data points and centoroids ---------------

    plt.scatter(df['x'], df['y'], c=df['color'], cmap='gist_rainbow', alpha=0.3)
    plt.xlabel('Sepal Length', fontsize=10)
    plt.ylabel('Sepal width', fontsize=10)
    color = {0: 'r', 1: 'g', 2: 'b'}
    for i in range(3):
        plt.scatter(centroids[i][0], centroids[i][1], color=color[i], edgecolors='k')

    plt.show()
    """
    def update(k):
        for i in range(3):
            centroids[i][0]=np.mean(df[df['closest'] == 0]['x'])
            centroids[i][1] = np.mean(df[df['closest'] == 0]['y'])
        return k

    centroids=update(centroids)
    print(centroids)
    """
    # -------------Showing both data points and centoroids ---------------

    plt.scatter(df['x'], df['y'], c=df['color'], cmap='gist_rainbow')
    plt.xlabel('Sepal Length', fontsize=10)
    plt.ylabel('Sepal width', fontsize=10)
    color = {0: 'r', 1: 'g', 2: 'b'}
    for i in range(3):
        plt.scatter(centroids[i][0], centroids[i][1], color=color[i], edgecolors='k')

    plt.show()

    # closest_centroids=df['closest'].copy(deep=True)
    # if closest_centroids.equals(df['closest']):
    #     print('Same')

    while True:
        closest_centroids = df['closest'].copy(deep=True)
        if closest_centroids.equals(df['closest']):
            break
        centroids = update(centroids)
        df = assignment(df, centroids)

    # -------------Showing both data points and centoroids ---------------

    plt.scatter(df['x'], df['y'], c=df['color'], cmap='gist_rainbow')
    plt.xlabel('Sepal Length', fontsize=10)
    plt.ylabel('Sepal width', fontsize=10)
    color = {0: 'r', 1: 'g', 2: 'b'}
    for i in range(3):
        plt.scatter(centroids[i][0], centroids[i][1], color=color[i], edgecolors='k')

    plt.show()

    SL = float(input("Sepal length in cm"))
    SW = float(input("Sepal width in cm"))
    PL = float(input("Petal length in cm"))
    PW = float(input("Petal width in cm"))
    x1 = math.sqrt(SL * PL)
    x2 = math.sqrt(SW * PW)
    dist = 0;
    small = float('inf');
    for i in range(3):
        dist = (math.sqrt((x1 - centroids[i][0]) ** 2 + (x2 - centroids[i][1]) ** 2))

        if (dist < small):
            print(i)
            print(": True")
            small = dist
            p = i
    print(iris_class[p])
    # -------------Showing both data points and centoroids ---------------

    plt.scatter(df['x'], df['y'], c=df['color'], cmap='gist_rainbow')
    plt.xlabel('Sepal Length', fontsize=10)
    plt.ylabel('Sepal width', fontsize=10)
    color = {0: 'r', 1: 'g', 2: 'b'}
    plt.scatter(x1, x2, color='k', edgecolors='k')
    for i in range(3):
        plt.scatter(centroids[i][0], centroids[i][1], color=color[i], edgecolors='k')

    plt.show()


main()

# for i in range(2):
#     str = ""
#     for element in array[0]:
#         str += element
#
#     # search using regex
#     x = re.findall('[0-9]+.[0-9]', str)
#     print(x)
#     new_x = np.array(x)
#     y = new_x.astype(float)
#
#     refined_array = y
#     print(refined_array)