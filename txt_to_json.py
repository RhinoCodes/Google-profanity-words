import json

open("list.json", "w+").write(json.dumps(open("list.txt).read().splitlines), indent=4))
