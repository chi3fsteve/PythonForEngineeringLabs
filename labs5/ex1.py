import requests
import io
import numpy as np
import matplotlib.pyplot as plt


response = requests.get('https://wp.faculty.wmi.amu.edu.pl/daneX.npy')
response.raise_for_status()
x = np.load(io.BytesIO(response.content))
response = requests.get('https://wp.faculty.wmi.amu.edu.pl/daneY.npy')
response.raise_for_status()
y = np.load(io.BytesIO(response.content))

gridx = np.linspace(min(x), max(x), 11)
gridy = np.linspace(min(y), max(y), 11)

H, xedges, yedges = np.histogram2d(x, y, bins=[gridx, gridy])

