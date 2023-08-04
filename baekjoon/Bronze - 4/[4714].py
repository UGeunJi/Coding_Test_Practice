while True:
    f = float(input())
    if f == -1.0:
        break
    
    print(f'Objects weighing {f:.2f} on Earth will weigh {(f * 0.167):.2f} on the moon.')
