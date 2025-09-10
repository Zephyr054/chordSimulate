from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Lỗi: Không thể chia cho 0"
    return a / b
def average(a, b):
    return (a + b) / 2

server = SimpleJSONRPCServer(('localhost', 8000))
print("JSON-RPC server running on port 8000...")
server.register_function(add, 'add')
server.register_function(subtract, "subtract")
server.register_function(multiply, "multiply")
server.register_function(divide, "divide")
server.register_function(average, "average")
server.serve_forever()
