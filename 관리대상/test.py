import subprocess

files = [
    '사업장/1. 사업장등록.py',
    '원료제조물/1. 원료제조물등록.py',
    '공중이용시설/1. 공중이용시설등록.py',
    '도급사업/1. 도급사업등록.py'
]

for _ in range(1):
    for file in files:
        subprocess.run(['python3', file])
