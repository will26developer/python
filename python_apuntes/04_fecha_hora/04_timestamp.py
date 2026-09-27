from datetime import datetime
import time

start_time: float | int = time.perf_counter()
print(start_time)

for i in range(100000000):
    pass

end_time: float | int = time.perf_counter()
print(end_time)

print(f"Tiempo total transcurrido: {end_time - start_time:.2f} segundos")