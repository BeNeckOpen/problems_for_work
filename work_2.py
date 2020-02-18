def file_pars():
    f = open('hits.txt', 'r')
    dict_standart = {}
    ip_s = [ip_s.split().pop(1) for ip_s in f]
    for ip in ip_s:
        dict_standart[ip] = dict_standart.get(ip, 0) + 1
    list_d = list(dict_standart.items())
    list_d.sort(key=lambda i: i[1])
    for i in range(5):
        print(list_d[len(list_d) - i - 1][0])


file_pars()
