import os
import time

path = "Xenonstck.txt"

ti_c = os.path.getctime(path)
ti_m = os.path.getmtime(path)


c_ti = time.ctime(ti_c)
m_ti = time.ctime(ti_m)

print(f"The file located at the path {path} \
was created at {c_ti} and was "
	f"last modified at {m_ti}")