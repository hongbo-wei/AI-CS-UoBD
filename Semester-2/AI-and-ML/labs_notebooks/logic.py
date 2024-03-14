import inspect

# Algorithm 8.1 model-checking of entailment: P ⊨ Q ⇔ M(P) ⊆ M(Q)
def model_check(P,Q):

    sig = inspect.signature(P)
    Nparams = len(sig.parameters)
    Ntruth = 2**Nparams

    # Step 1. Generate all possible combinations of truth values of the parameters, and the given propositions
    models = [[bool(n//(2**p)%2) for p in range(Nparams-1,-1,-1)] for n in range(Ntruth)]
    truthvalP = [P(*vars) for vars in models]
    truthvalQ = [Q(*vars) for vars in models]

    # Step 2. Compute indices of models M(P), M(Q) where P and Q hold
    modelPi = [i for i in range(Ntruth) if truthvalP[i]]
    modelQi = [i for i in range(Ntruth) if truthvalQ[i]]

    # Step 3. Test subset -- of all models where P true, test Q also true, i.e. compute M(P) ⊆ M(Q)
    entails = set(modelPi).issubset(modelQi)

    return models, modelPi, modelQi, entails