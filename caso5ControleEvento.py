palestra = ["Ana", "Carlos", "Marina"]
workshop = ["Carlos", "João", "Ana"]
mesa_redonda = ["Marina", "João", "Paula"]

set_palestra = set(palestra)
set_workshop = set(workshop)
set_mesa = set(mesa_redonda)

todos = set_palestra & set_workshop & set_mesa

todas_atividades = palestra + workshop + mesa_redonda
participacao_unica = {nome for nome in todas_atividades if todas_atividades.count(nome) == 1}

participantes_unicos = set_palestra | set_workshop | set_mesa

total_distintos = len(participantes_unicos)

print(f"1. Participaram de todas as atividades: {todos if todos else 'Nenhum'}")
print(f"2. Participaram de apenas uma atividade: {participacao_unica}")
print(f"3. Lista de todos os participantes únicos: {participantes_unicos}")
print(f"4. Total de participantes distintos: {total_distintos}")
