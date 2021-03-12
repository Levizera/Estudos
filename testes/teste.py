import io
r = http.request('GET', 'https://example.com', preload_content=Fal)
r.auto_close = False
for line in io.TextIOWrapper(r):
   print(line)