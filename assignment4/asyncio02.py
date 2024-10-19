import asyncio

# Coroutine for a task
async def task_coroutine(value):
    # Report a message
    print(f'Task {value} is running')
    # Block for a moment
    await asyncio.sleep(1)
    # Report completion
    print(f'Task {value} is completed')

# Define the main coroutine
async def main():
    # Report a message
    print('Main coroutine started')
    # Start many tasks
    tasks = [asyncio.create_task(task_coroutine(i)) for i in range(5)]
    # Get all tasks (excluding the current task)
    all_tasks = [task for task in asyncio.all_tasks() if task is not asyncio.current_task()]
    # Report all tasks
    print(f'Found {len(all_tasks)} tasks running:')
    for task in all_tasks:
        print(f'> {task.get_name()}, {task.get_coro()}')
    # Wait for all tasks to complete
    await asyncio.gather(*tasks)
    print('All tasks completed')

# Start the asyncio program
asyncio.run(main())
