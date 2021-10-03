import asyncio


@asyncio.coroutine
def slow_operation():
    # yield from suspends execution until
    # there's some result from asyncio.sleep

    yield from asyncio.sleep(1)

    # our task is done, here's the result
    return 'Future is done!'


def got_result(future):
    print(future.result())


# Our main event loop
loop = asyncio.get_event_loop()

# We create a task from a coroutine
task = loop.create_task(slow_operation())

# Please notify us when the task is complete
task.add_done_callback(got_result)

# The loop will close when the task has resolved
loop.run_until_complete(task)