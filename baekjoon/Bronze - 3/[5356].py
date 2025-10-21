import sys

def next_letter(ch, offset):
    # ch(시작 대문자)로부터 offset만큼 증가한 대문자(래핑 포함)
    return chr((ord(ch) - ord('A') + offset) % 26 + ord('A'))

def main():
    data = sys.stdin.read().strip().splitlines()
    if not data:
        return
    t = int(data[0].strip())
    out_lines = []

    for idx in range(1, 1 + t):
        line = data[idx].strip().split()
        if len(line) != 2:
            continue  # 형식 오류 방지
        a, b = line[0], line[1]

        # 순서 유연 처리: 숫자-문자 또는 문자-숫자
        if a.isdigit():
            n = int(a)
            start = b.upper()
        else:
            start = a.upper()
            n = int(b)

        # n 레벨 출력
        for i in range(1, n + 1):
            ch = next_letter(start, i - 1)
            out_lines.append(ch * i)

        # 삼각형 사이 빈 줄(마지막 제외)
        if idx != t:
            out_lines.append("")

    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()
