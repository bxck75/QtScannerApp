%%capture var2
%run -I script2
import sys
orig_stdout = sys.stdout
f = file('out5.txt', 'w')
sys.stdout = f
print var2
stdout = orig_stdout
f.close()