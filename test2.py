import trio
import httpx
import time

URL = "https://makersmarkshop.com/"
NUM_REQUESTS = 10000
MAX_CONCURRENT = 2000  # careful

# Shared results for performance aggregation
success_count = 0
fail_count = 0

async def fire(client):
    global success_count, fail_count
    try:
        r = await client.get(URL)
        if r.status_code == 200:
            success_count += 1
        else:
            fail_count += 1
    except Exception:
        fail_count += 1

async def ultra_runner():
    start = time.perf_counter()
    limits = httpx.Limits(
        max_connections=MAX_CONCURRENT,
        max_keepalive_connections=MAX_CONCURRENT
    )

    async with httpx.AsyncClient(http2=True, limits=limits, timeout=5.0) as client:
        async with trio.open_nursery() as nursery:
            for _ in range(NUM_REQUESTS):
                nursery.start_soon(fire, client)

    elapsed = time.perf_counter() - start
    print(f"\n🧨 Ultra Blast Complete!")
    print(f"✅ Success: {success_count} | ❌ Fail: {fail_count}")
    print(f"⏱️ Time: {elapsed:.2f}s → RPS: {NUM_REQUESTS / elapsed:.2f}")

trio.run(ultra_runner)
