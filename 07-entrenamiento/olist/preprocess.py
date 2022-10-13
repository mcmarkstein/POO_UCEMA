import pandas as pd
import numpy as np
from math import radians, sin, cos, asin, sqrt


def transformar_columnas_datetime(orders):
    # transformar a datetime. Una manera de que entre todo el código es usando "\" al final de la línea
    orders['order_delivered_customer_date'] = pd.to_datetime(orders['order_delivered_customer_date']) #se puede hacer de esta manera
    orders.loc[:, 'order_estimated_delivery_date'] = \
        pd.to_datetime(orders['order_estimated_delivery_date'])
    orders.loc[:, 'order_purchase_timestamp'] = \
        pd.to_datetime(orders['order_purchase_timestamp'])
    return orders


def tiempo_de_espera(orders, is_delivered=True):
    # filtrar por entregados y crea la varialbe tiempo de espera
    if is_delivered:
        orders = orders.query("order_status=='delivered'").copy()
    # compute wait time
    orders.loc[:, 'tiempo_de_espera'] = \
        (orders['order_delivered_customer_date'] -
         orders['order_purchase_timestamp']) / np.timedelta64(24, 'h')
    return orders


def manejar_delay(x):
    #tener  solo fechas positivas, por ejemplo cuando estimado llega a uno
    if x > 0:
        return x
    else:
        return 0


def real_vs_esperado(orders, is_delivered=True):
    # filtrar por entregados
    if is_delivered:
        orders = orders[orders['order_status']=='delivered']
    # compute delay vs expected
    orders.loc[:, 'real_vs_esperado'] = \
        (orders['order_delivered_customer_date'] -
         orders['order_estimated_delivery_date']) / np.timedelta64(24, 'h')

    orders.loc[:, 'real_vs_esperado'] = \
        orders['real_vs_esperado'].apply(manejar_delay)
    return orders

def puntaje_de_compra(reviews):
    def es_cinco_estrellas(d):
        if d == 5:
            return 1
        else:
            return 0

    def es_una_estrella(d):
        if d == 1:
            return 1
        else:
            return 0

    reviews.loc[:, 'es_cinco_estrellas'] =\
        reviews['review_score'].apply(es_cinco_estrellas)

    reviews.loc[:, 'es_una_estrella'] =\
        reviews['review_score'].apply(es_una_estrella)

    return reviews[[
    'order_id', 'es_cinco_estrellas', 'es_una_estrella', 'review_score'
]]


def calcular_numero_productos(data):
    data = data
    productos = \
        data['order_items']\
        .groupby('order_id',
                 as_index=False).agg({'order_item_id': 'count'})
    productos.columns = ['order_id', 'number_of_products']
    return productos

def vendedores_unicos(data):
    vendedores = \
        data['order_items']\
        .groupby('order_id')['seller_id'].nunique().reset_index()
    vendedores.columns = ['order_id', 'vendedores_unicos']

    return vendedores

def calcular_precio_y_transporte(data):
    """ calcula el precio total y el precio del transporte"""
    precio_y_transporte = \
        data['order_items']\
        .groupby('order_id',
                 as_index=False).agg({'price': 'sum',
                                      'freight_value': 'sum'})
    precio_y_transporte.columns = ['order_id', 'precio','transporte']

    return precio_y_transporte

def haversine_distance(lon1, lat1, lon2, lat2):
    """
    Computa distancia entre dos pares (lat, lng)
    Ver - (https://en.wikipedia.org/wiki/Haversine_formula)
    """
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    return 2 * 6371 * asin(sqrt(a))

def calcular_distancia_vendedor_comprador(data):
    """ Calcula la distancia entre el vendedor y el comprador
    """
    orders = data['orders']
    order_items = data['order_items']
    sellers = data['sellers']
    customers = data['customers']

    #usar el dataset de geolocalizacion
    # Un zip code puede tener varias lat y lon. groupby puede ser usado con el metodo .first() para quedarte con el primero
    geo = data['geolocation']
    geo = geo.groupby('geolocation_zip_code_prefix',
                      as_index=False).first()

    # Solo usar columnas 'seller_id', 'seller_zip_code_prefix', 'geolocation_lat', 'geolocation_lng'
    sellers_mask_columns = [
        'seller_id', 'seller_zip_code_prefix', 'geolocation_lat', 'geolocation_lng'
    ]

    # mergear vendedores con geolocalizacion
    sellers_geo = sellers.merge(
        geo,
        how='left',
        left_on='seller_zip_code_prefix',
        right_on='geolocation_zip_code_prefix')[sellers_mask_columns]

    # Mergear con compradores
    customers_mask_columns = ['customer_id', 'customer_zip_code_prefix', 'geolocation_lat', 'geolocation_lng']

    customers_geo = customers.merge(
        geo,
        how='left',
        left_on='customer_zip_code_prefix',
        right_on='geolocation_zip_code_prefix')[customers_mask_columns]

    # Mergear en otra tabla compradores y vendedores
    customers_sellers = customers.merge(orders, on='customer_id') \
        .merge(order_items, on='order_id') \
        .merge(sellers, on='seller_id') \
        [['order_id', 'customer_id', 'customer_zip_code_prefix', 'seller_id', 'seller_zip_code_prefix']]

    # Mergear con geolocalizacion de compradores
    matching_geo = customers_sellers.merge(sellers_geo,
                                           on='seller_id') \
        .merge(customers_geo,
               on='customer_id',
               suffixes=('_seller',
                         '_customer'))
    # Remover  na()
    matching_geo = matching_geo.dropna()

    matching_geo.loc[:, 'distance_seller_customer'] = \
        matching_geo.apply(lambda row:
                           haversine_distance(row['geolocation_lng_seller'],
                                              row['geolocation_lat_seller'],
                                              row['geolocation_lng_customer'],
                                              row['geolocation_lat_customer']),
                           axis=1)
    # Una orden puede tener muchos compradores retorna el promedio
    order_distance = \
        matching_geo.groupby('order_id',
                             as_index=False).agg({'distance_seller_customer':
                                                      'mean'})

    return order_distance


def obtener_tablon_primario(data,
                            is_delivered=True,
                            with_calcular_distancia_vendedor_comprador=False):
    orders = data['orders']
    reviews = data['order_reviews']
    precio_y_transporte = calcular_precio_y_transporte(data)
    vendedores = vendedores_unicos(data)
    productos = calcular_numero_productos(data)
    reviews = puntaje_de_compra(reviews)
    orders = real_vs_esperado(orders, is_delivered=True)
    #merge all dataframes in tablon_primario
    tablon_primario = orders.merge(reviews, on='order_id') \
        .merge(precio_y_transporte, on='order_id') \
        .merge(vendedores, on='order_id') \
        .merge(productos, on='order_id')


    # calcular_distancia_vendedor_comprador
    if with_calcular_distancia_vendedor_comprador:
        tablon_primario = tablon_primario.merge(
            calcular_distancia_vendedor_comprador(data), on='order_id')

    return tablon_primario.dropna()