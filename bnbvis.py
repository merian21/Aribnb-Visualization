import pandas as pd
print()
print('******** DATEEEEEEN *********')
print()
# CSV Dateipfad
filepath = 'listings.csv'

# Laden des Datensatzes mit pandas
data = pd.read_csv(filepath)

# Erste 5 Zeilen zu Testzwecken zeigen
data.head()

# Informationen über den Datensatz erhalten
data.info()

# Beschreibende Statistiken anzeigen
data.describe()

# Anzahl der fehlenden Werte pro Spalte
data.isnull().sum()

# Fehlende Werte werden mit dem Standardwert 0 gefüllt
data_fillna = data.fillna(0)