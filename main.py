from data_collector import SampleGenerator
import tasks

sample_generator = SampleGenerator(6, 350, 12)

data = sample_generator.data_collector()

tasks.task1(data)
tasks.task2(data)
tasks.task4(data)
tasks.task5(data)
