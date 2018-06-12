records = "test_user_login,16.0,success\ntest_user_login,1.0,failure\ntest_display_devices,15.3,success\ntest_display_devices,3.1,failure\ntest_user_logout,1.2,success\ntest_show_alerts,10.0,success"

b = records.split('\n')
new_b = []

for i in range(0, len(b)):
    new_b.append(b[i].split(','))

success = {}
failure = {}

for i in new_b:
    for j in i:
        if j == 'success':
            success[i[0]] = success.get('success', 0) + 1
        elif j == 'failure':
            failure[i[0]] = failure.get('failure', 0) + 1

print('Successful tests: ', success)
print('Failure tests: ', failure)

times = {}

for i in new_b:
    for j in i:
        if j == 'success':
            times[i[0]] = (i[1])

print('Times of successful tests: ', times)

names_of_tests = []
times_of_tests = []

for name, time in times.items():
    names_of_tests.append(name)
    times_of_tests.append(time)

time_max = max(times_of_tests)
test_max = times_of_tests.index(time_max)

print('The longest test was ', names_of_tests[test_max], ' and lasted ', time_max, 'seconds.')