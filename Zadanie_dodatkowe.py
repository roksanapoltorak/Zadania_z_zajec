records = "test_user_login,14.0,success\ntest_user_login,1.0,failure\ntest_display_devices,15.3,success\ntest_display_devices,3.1,failure\ntest_user_logout,1.2,success\ntest_show_alerts,10.0,success"

b = records.split('\n')
lst = []

for i in range(0, len(b)):
    lst.append(b[i].split(','))

success = {}
failure = {}

for i in lst:
    for j in i:
        if j == 'success':
            success[i[0]] = success.get('success', 0) + 1
        elif j == 'failure':
            failure[i[0]] = failure.get('failure', 0) + 1

print('Successful tests: ', success)
print('Failure tests: ', failure)

times = {}

for i in lst:
    for j in i:
        if j == 'success':
            times[i[0]] = (i[1])

print('Times of successful tests: ', times)

new_list1 = []
new_list = []

for name, time in times.items():
    new_list1.append(name)
    new_list.append(time)

a = max(new_list)
c = new_list.index(a)

print('The longest test was ', new_list1[c], ' and lasted ', a, 'seconds.')