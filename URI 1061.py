# https://www.urionlinejudge.com.br/judge/en/problems/view/1061
dia_comeco = input().split(" ")
hora_comeco = input().split(" : ")
dia_termino = input().split(" ")
hora_termino = input().split(" : ")

inicio_dia = int(dia_comeco[1])
termino_dia = int(dia_termino[1])

inicio_hora = int(hora_comeco[0])
inicio_minuto = int(hora_comeco[1])
inicio_segundo = int(hora_comeco[2])
inicio_total = (inicio_hora*60*60)+(inicio_minuto*60)+(inicio_segundo)

termino_hora = int(hora_termino[0])
termino_minuto = int(hora_termino[1])
termino_segundo = int(hora_termino[2])
termino_total = (termino_hora*60*60)+(termino_minuto*60)+(termino_segundo)


total_segundos = (termino_total + (termino_dia*24*60*60)) - (inicio_total + (inicio_dia*24*60*60))
resultado_dias = int(total_segundos/24/60/60)
resultado_horas = int((total_segundos - resultado_dias*24*60*60)/60/60)
resultado_minutos = int((total_segundos - (resultado_horas*60*60 + resultado_dias*24*60*60))/60)
resultado_segundos = total_segundos - (resultado_dias*24*60*60 + resultado_horas*60*60 + resultado_minutos*60)

print(f"{resultado_dias} dia(s)")
print(f"{resultado_horas} hora(s)")
print(f"{resultado_minutos} minuto(s)")
print(f"{resultado_segundos} segundo(s)")
