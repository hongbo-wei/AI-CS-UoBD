# this is a user threads library
import asyncio
# this one is for timing
import time

# this function uses blocking calls to time and is not manages by asyncio
def sleepy_sync():
  time.sleep(1)
  print("Hello")
  time.sleep(1)
  print("World")

def main_sync():
  sleepy_sync()
  sleepy_sync()
  sleepy_sync()

# this function uses non-blocking sleep and is managed by asyncio
# upon calling asyncio.sleep() the thread is suspended by the library and its state and saved. Upon sleeping for 1 second the thread is awaken by the library and its execution continues.
async def sleepy_async():
  await asyncio.sleep(1)
  print("Hello")
  await asyncio.sleep(1)
  print("World")

async def main_async():
  await asyncio.gather(sleepy_async(), sleepy_async(), sleepy_async())

start = time.time()
main_sync()
end = time.time()

print("{:.0f}s".format(end - start))

start = time.time()
asyncio.run(main_async())
end = time.time()

print("{:.0f}s".format(end - start))