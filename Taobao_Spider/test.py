from datetime import datetime

now = datetime.now()

specific_time = datetime.strptime(datetime.strftime(datetime.now(), "%Y-%m-%d")+" 23:25:11", '%Y-%m-%d %H:%M:%S')

inteval = specific_time - now

print(now)
print(type(now))

print(datetime.strptime(datetime.now().strftime("%H:%M:%S"), '%H:%M:%S'))
print(type(datetime.strptime(datetime.now().strftime("%H:%M:%S"), '%H:%M:%S')))

print(specific_time)
print(type(specific_time))

print(inteval)
print(type(inteval))
print(inteval.total_seconds().__class__.__name__)