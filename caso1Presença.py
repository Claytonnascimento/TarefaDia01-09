presencas = {
    "segunda": {"Ana", "Bruno", "Carlos", "Daniela"},
    "terça": {"Ana", "Carlos", "Daniela"},
    "quarta": {"Ana", "Bruno", "Carlos"},
    "quinta": {"Ana", "Bruno", "Daniela"},
    "sexta": {"Ana", "Bruno", "Carlos", "Daniela"}}

presentes_todos = set.intersection(*presencas.values())

presentes_algum_dia = set.union(*presencas.values())
faltaram_algum_dia = presentes_algum_dia - presentes_todos

total_presencas = {}
for dia, alunos in presencas.items():
    for aluno in alunos:
        total_presencas[aluno] = total_presencas.get(aluno, 0) + 1

print("Presentes todos os dias:", presentes_todos)
print("Faltaram em pelo menos 1 dia:", faltaram_algum_dia)
print("Total de presenças por aluno:")
for aluno, qtd in total_presencas.items():
    print(f" - {aluno}: {qtd} presenças")
