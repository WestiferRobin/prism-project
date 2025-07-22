import asyncio
import json
from aio_pika import connect_robust, IncomingMessage
from db import settings
from src.services.consumer_service import handle_content_job
from src.utils.converters.job_converter import convert_payload_to_content_job
from src.utils.constants import CONTENT_SERVICE_QUEUE, JOB_QUEUE_CONCURRENCY
from src.utils.logger import get_logger

message_queue = asyncio.Queue()
logger = get_logger(__name__)


async def wait_for_rabbitmq(max_retries=10, delay=3):
    for i in range(max_retries):
        try:
            connection = await connect_robust(settings.queue_content_url)
            logger.info("Connected to RabbitMQ")
            return connection
        except Exception as e:
            logger.info(f"Waiting for RabbitMQ... retry {i+1}/{max_retries} - {e}")
            await asyncio.sleep(delay)
    raise RuntimeError("RabbitMQ connection failed after retries")


async def worker(queue):
    while True:
        message: IncomingMessage = await queue.get()
        async with message.process():
            payload = json.loads(message.body.decode())
            content_job = convert_payload_to_content_job(payload)
            await handle_content_job(content_job)
        queue.task_done()


async def start_message_consumers():
    connection = await wait_for_rabbitmq()
    channel = await connection.channel()
    queue = await channel.declare_queue(CONTENT_SERVICE_QUEUE, durable=True)

    async def enqueue_messages():
        async with queue.iterator() as queue_iter:
            async for message in queue_iter:
                await message_queue.put(message)

    for _ in range(JOB_QUEUE_CONCURRENCY):
        asyncio.create_task(worker(message_queue))

    asyncio.create_task(enqueue_messages())
