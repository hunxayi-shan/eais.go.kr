import re
import json

addresses = [
    "서울특별시 강남구 언주로 332 역삼푸르지오 제101동 제1층 제101호 [역삼동 754-1]",
    "서울특별시 강남구 언주로 332 역삼푸르지오 제101동 제1층 제102호 [역삼동 754-1]",
    "경기도 부천시 부일로 440-13 숲속애가 주건축물제1동 [심곡동 396-9 외 1필지]",
    "인천광역시 부평구 부영로 196 대림아파트 제11동 제1층 제102호 [부평동 64-20 외 2필지]",
    "경기도 부천시 부일로 440-13 숲속애가 주건축물제1동 [심곡동 396-9 외 1필지]",
]

formatted_addresses = []
counter = 0

for address in addresses:
    counter += 1
    match = re.match(
        r"^(.*?)\s?(제\d+동)?\s?(제\d+층)?\s?(제\d+호)?\s?\[(.*?)\]$", address)
    if match:
        print(counter)
        parts = match.groups()
        formatted_address = {
            "Address": parts[0].strip(),
            "Building": ''.join(filter(str.isdigit, parts[1].strip())) if parts[1] else "",
            "Floor": ''.join(filter(str.isdigit, parts[2].strip())) if parts[2] else "",
            "Unit": ''.join(filter(str.isdigit, parts[3].strip())) if parts[3] else "",
            "Neighborhood": parts[4].strip() if parts[4] else ""
        }
        formatted_addresses.append(formatted_address)

with open("formatted_addresses.json", "w", encoding='utf-8') as json_file:
    json.dump(formatted_addresses, json_file, indent=4, ensure_ascii=False)

print("Formatted addresses saved to formatted_addresses.json")
