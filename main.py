from for_MS.data_collector import SampleGenerator
from tasks import task_1, task_2, task_4, task_5

sample_generator = SampleGenerator(v=8, sum_limit=12, n=350)

data = sample_generator.data_collector()

task_1(data)
task_2(data)
task_4(data)
task_5(data)
