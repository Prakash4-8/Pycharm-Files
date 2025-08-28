months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December']
# 1. Lambda function calculating kinetic energy Ke = (m*v**2)/2
kinetic_energy = lambda m, v: (m*v**2)/2
print(kinetic_energy(2, 3))