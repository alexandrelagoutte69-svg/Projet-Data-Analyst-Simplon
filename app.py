import plotly.express as px
import pandas as pd

data = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

# Projet Simplon
data['total_sale'] = data['qte'] * data['prix']

figureSalesByCountry = px.pie(data, values='qte', names='region', title='quantité vendue par région')
figureSalesByProduct = px.pie(data, values='qte', names='produit', title='quantité vendue par produit')
figureTotalSalesByProduct = px.pie(data, values='total_sale', names='produit', title='CA par produit')

figureSalesByCountry.write_html('ventes-par-region-pie.html')
figureSalesByProduct.write_html('ventes-par-produit-pie.html')
figureTotalSalesByProduct.write_html('ca-par-produit-pie.html')

# Tests
total_produits = data.groupby("produit")["qte"].sum().reset_index()
figureBarChartSalesByProduct = px.bar(total_produits, x='produit', y='qte')
figureBarChartSalesByProduct.write_html('ventes-par-produit-bar.html')

figureHistoSalesByCountry = px.histogram(data, x='produit', y='qte', color='region', facet_col='region')
figureHistoSalesByCountry.write_html('ventes-produits-par-region-histogram.html')