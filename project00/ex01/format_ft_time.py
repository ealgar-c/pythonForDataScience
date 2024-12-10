from datetime import datetime
import time

curr = time.time()
actual_date_str = datetime.fromtimestamp(curr).strftime("%b %d %Y")

print(f"Seconds since January 1, 1970: {curr:,.4f} or {curr:.2e} in scientific notation\n{actual_date_str}")
