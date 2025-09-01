import math

distancias = []
for i in range(6):
    km = float(input(f"Digite a distância da viagem {i+1} em km: "))
    distancias.append(km)

total = sum(distancias)

maior = max(distancias)
menor = min(distancias)

media = math.ceil(total / len(distancias))

print("\nResumo das Viagens:")
print(f"Distâncias registradas: {distancias}")
print(f"Distância total: {total} km")
print(f"Maior distância: {maior} km")
print(f"Menor distância: {menor} km")
print(f"Média arredondada para cima: {media} km")
