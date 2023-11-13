from btest.models import workers, projects, workingOn
w1 = workers(surname='Иванов', name='Иван', otchestvo="Ивановаич",
             pasportNumber=123456, pasportSerie=1234, INN=145635423413,
              birth="1989-12-31", position="Учёный")
w2 = workers(surname='Петров', name='Пётр', otchestvo="Петрович",
             pasportNumber=234567, pasportSerie=2345, INN=245435623415,
              birth="1989-12-31", position="Учёный")
w3 = workers(surname='Смирнов', name='Денис', otchestvo="Денисович",
             pasportNumber=345678, pasportSerie=3456, INN=345567586456,
              birth="1989-12-31", position="Разработчик")
w4 = workers(surname='Денисов', name='Андрей', otchestvo="Петрович",
             pasportNumber=123456, pasportSerie=1234, INN=245635423413,
              birth="1989-12-31", position="Разработчик")
w5 = workers(surname='Иванов5', name='Иван5', otchestvo="Ивановаич5",
             pasportNumber=523456, pasportSerie=5234, INN=545635423413,
              birth="1989-12-31", position="Учёный")
w1.save()
w2.save()
w3.save()
w4.save()
w5.save()

p1 = projects(title='project1',
              satrtDate="2013-12-31",endDate="2089-12-31", price=145635423414564573)
p2 = projects(title='project2',
              satrtDate="2023-12-31",endDate="2035-12-31", price=23563542341534)
p3 = projects(title='project3',
              satrtDate="2025-12-31",endDate="2029-12-31", price=34513542)

p1.save()
p2.save()
p3.save()
wp1 = workingOn (worker = w1,project = p1)
wp2 = workingOn (worker = w1,project = p3)
wp3 = workingOn (worker = w2,project = p1) 
wp4 = workingOn (worker = w3,project = p2) 
wp5 = workingOn (worker = w4,project = p1)


wp1.save()
wp2.save()
wp3.save()