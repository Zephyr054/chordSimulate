import pika

# Kết nối tới RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Đảm bảo queue tồn tại
channel.queue_declare(queue='hello')

# Hàm xử lý khi nhận message
def callback(ch, method, properties, body):
    print(f" [x] Received {body.decode()}")

# Đăng ký consumer
channel.basic_consume(queue='hello',
                      on_message_callback=callback,
                      auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
