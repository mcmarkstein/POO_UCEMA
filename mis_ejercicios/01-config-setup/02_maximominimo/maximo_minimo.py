# encontrar la suma maxima y minima de un array tomando solo n-1 elementos del mismo.
# de [1,2,3,4,5]  la suma maxima es 15 y la minima es 10


def mediana(arr):
    # Write your code here
    minimo = sum(arr) - max(arr)
    maximo = sum(arr) - min(arr)
    return [minimo, maximo]


