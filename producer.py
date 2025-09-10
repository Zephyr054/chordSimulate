import pika

# Kết nối tới RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Tạo queue (nếu chưa tồn tại)
channel.queue_declare(queue='hello')

# Gửi message
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello RabbitMQ!')
print(" [x] Sent 'Hello RabbitMQ!'")

# Đóng kết nối
connection.close()