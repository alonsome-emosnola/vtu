from datetime import datetime
import time

def account_reference():
    now = datetime.now()
    current_clock = time.strftime("%H%M", time.localtime())
    return f"ACC_REF|{now.strftime('%Y%m%d')}|{current_clock}|{generate(length_minimal=8, length_maximal=8)}"
