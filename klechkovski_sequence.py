def klechkovski(n,l = None):
    
    quantum_hash = {'s': 0, 'p': 1, 'd': 2, 'f': 3}
    reversed_quantum_hash = {v: k for k, v in quantum_hash.items()}
    klechkovski_sequence = []
    if not l:
        l = n - 1 #Sets l to the maximum that the max shell can handle
    for shell in range(1,n + 1):
        for subshell in range(shell):
            if subshell in reversed_quantum_hash:
                label = f"{shell}{reversed_quantum_hash[subshell]}"
                priority = shell + subshell
                klechkovski_sequence.append((priority,shell,label)) #Sort by priority, then by n(if tie like 2p and 3s)
    klechkovski_sequence.sort()
    return klechkovski_sequence
for orbital in klechkovski(3):
    print(orbital[2])