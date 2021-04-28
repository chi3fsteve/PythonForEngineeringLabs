import requests
import io
import numpy as np

response = requests.get('https://wp.faculty.wmi.amu.edu.pl/solve.npz')
response.raise_for_status()
data = np.load(io.BytesIO(response.content))

list = data.files
for i in list:
    print(i)
    print(data[i])
ans = np.linalg.solve(data['A'], data['b'])

print(ans)

print(np.transpose(data['A2']))
print(data['b2'])

ans2 = np.linalg.solve(np.transpose(data['A2']), data['b2'])
