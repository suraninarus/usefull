import memory_profiler as mem_profile
import random
import time

names = ['Kiran','King','John','Corey']
majors = ['Math','Comps','Science']

print ('Memory (Before): {}Mb'.format(mem_profile.memory_usage()))

def people_list(num_people):
    results = []
    for i in range(num_people):
        person = {
                    'id':i,
                    'name': random.choice(names),
                    'major':random.choice(majors)
                  }
        results.append(person)
    return results

def people_generator(num_people):
    for i in range.range(num_people):
        person = {
                    'id':i,
                    'name': random.choice(names),
                    'major':random.choice(majors)
                  }
        yield person

t1 = time.time()
people = people_list(10000000)
t2 = time.time()


# t1 = time.time()
# people = people_generator(10000000)
# t2 = time.time()

print('Memory (After): {}Mb'.format(mem_profile.memory_usage()))
print('Took {} Seconds'.format(t2-t1))