import jsonrpclib

server = jsonrpclib.Server('http://localhost:8000')

try:
    print("Kết quả add(5, 3) =", server.add(5, 3))
    print("Kết quả subtract(10, 4) =", server.subtract(10, 4))
    print("Kết quả multiply(6, 7) =", server.multiply(6, 7))
    print("Kết quả divide(8, 2) =", server.divide(8, 2))
    print("Kết quả divide(5, 0) =", server.divide(5, 0))  # test chia 0
    print("Kết quả average(3, 6) =", server.average(3, 6))
except Exception as e:
    print("Lỗi khi gọi RPC:", e)