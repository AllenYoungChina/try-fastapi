from typing import Union, Annotated

from fastapi import BackgroundTasks, FastAPI, Depends

app = FastAPI()


def write_log(message: str):
    with open('log.txt', mode='a') as log:
        log.write(message)


def get_query(background_tasks: BackgroundTasks, q: Union[str, None] = None):
    if q:
        message = f'found query: {q}\n'
        background_tasks.add_task(write_log, message)
    return q


# Using BackgroundTasks also works with the dependency injection system,
# you can declare a parameter of type BackgroundTasks at multiple levels:
# in a path operation function, in a dependency (dependable), in a
# sub-dependency, etc.
@app.post('/send-notifications/{email}')
async def send_notification(
        email: str,
        background_tasks: BackgroundTasks,
        q: Annotated[str, Depends(get_query)]
):
    message = f'message to {email}\n'
    background_tasks.add_task(write_log, message)
    return {'message': 'Message sent'}
