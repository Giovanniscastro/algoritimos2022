from Aluno import Aluno
from AlunoEnsinoMedio import AlunoEnsinoMedio
from AlunoGraduacao import AlunoGraduacao

a = Aluno(13355 , "Ana", "05467.20221")

a.imprimir()

print()
print("---- Aluno EnsinoMedio ----")

aem = AlunoEnsinoMedio(864222, "Giovanni", "6482312.2021", 3)
aem.imprimir()

print()
print("---- Aluno Graduacao ----")

ag = AlunoGraduacao(55644222, "Kellen", "442231.20221", 4)
ag.imprimir()

