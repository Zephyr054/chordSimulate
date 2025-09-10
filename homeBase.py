# Mô phỏng hệ thống phân tán định danh người dùng dùng Home-base
import time
import random
nodes = {
    "A": {"user_1": "Alice_A", "user_2": "Bob_A"},
    "B": {"user_1": "Alice_B", "user_2": "Bob", "user_3": "Charlie_B"},
    "C": {"user_3": "Charlie"}
}

home_base = {
    "user_1": "A",   
    "user_2": "B",   
    "user_3": "C"    
}

def identify_user(user_id):
    
    if user_id not in home_base:
        return f"[ERROR] Không tìm thấy user {user_id}"
     
    delay = random.uniform(0.2, 1.0)
    time.sleep(delay)

    hb = home_base[user_id]
    user_name = nodes[hb].get(user_id, None)
    
    if user_name:
        return f"[OK] Định danh: {user_id} là '{user_name}' tại Home Base {hb}"
    else:
        return f"[ERROR] Không có dữ liệu định danh tại Home Base {hb}"

# ---- Demo ----
print(identify_user("user_1"))
print(identify_user("user_2"))
print(identify_user("user_3"))
print(identify_user("user_999"))
