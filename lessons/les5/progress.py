from progress.bar import Bar
import time

bar = Bar('Processing', max=20)
for i in range(20):
    time.sleep(1)
    # Do some work
    bar.next()
bar.finish()