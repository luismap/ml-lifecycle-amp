import sys

if len(sys.argv) > 1 and sys.argv[1].lower() == 'false':
  print(f"is intercept {sys.argv}")
  fit_intercept = False
else:
  fit_intercept = True

if len(sys.argv) > 2:
  filter_data = int(sys.argv[2])
  print(filter_data)
  
