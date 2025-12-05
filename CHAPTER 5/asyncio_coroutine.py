import asyncio
from random import randint

# global list to store transitions
transitions = []

async def start_state():
    print('Start State called\n')
    input_value = randint(0, 1)
    await asyncio.sleep(1)

    transitions.append(f'Start State -> input {input_value}')

    if input_value == 0:
        result = await state2(input_value)
    else:
        result = await state1(input_value)

    print('Resume of the Transition:\nStart State calling ' + result)
    print("\n=== Full Transition Path ===")
    for t in transitions:
        print(t)


async def state1(transition_value):
    output_value = f'State 1 with transition value = {transition_value}\n'
    input_value = randint(0, 1)
    await asyncio.sleep(1)

    print('...evaluating...')
    transitions.append(f'State 1 -> input {input_value}')

    if input_value == 0:
        result = await state3(input_value)
    else:
        result = await state2(input_value)

    return output_value + f'State 1 calling {result}'


async def state2(transition_value):
    output_value = f'State 2 with transition value = {transition_value}\n'
    input_value = randint(0, 1)
    await asyncio.sleep(1)

    print('...evaluating...')
    transitions.append(f'State 2 -> input {input_value}')

    if input_value == 0:
        result = await state1(input_value)
    else:
        result = await state3(input_value)

    return output_value + f'State 2 calling {result}'


async def state3(transition_value):
    output_value = f'State 3 with transition value = {transition_value}\n'
    input_value = randint(0, 1)
    await asyncio.sleep(1)

    print('...evaluating...')
    transitions.append(f'State 3 -> input {input_value}')

    if input_value == 0:
        result = await state1(input_value)
    else:
        result = await end_state(input_value)

    return output_value + f'State 3 calling {result}'


async def end_state(transition_value):
    output_value = f'End State with transition value = {transition_value}\n'
    print('...stop computation...')
    transitions.append(f'End State reached -> input {transition_value}')
    return output_value


if __name__ == '__main__':
    print('Finite State Machine simulation with Asyncio Coroutine')
    asyncio.run(start_state())
