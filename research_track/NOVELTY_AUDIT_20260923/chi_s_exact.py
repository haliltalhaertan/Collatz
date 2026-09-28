"""CP17 collision energy chi_s, exact transfer (float64, no truncation).

X_s = sum_{j=1..s} 3^{j-1} 2^{-S_j} (mod 3^s), A_i iid P(A=a)=2^{-a}, S_j=A_1+..+A_j.
Recursion: X_s = 2^{-A}(1 + 3 X_{s-1}) (mod 3^s), with a fresh A.
2^{-A} mod 3^s depends only on A mod 2*3^{s-1} (2 is a primitive root mod 3^s).
chi_s = 3^s * sum_y p_s(y)^2 ; chi_s = 1 + sum_{j<=s} E_j, E_j = chi_j - chi_{j-1} >= 0.
Usage: python chi_s_exact.py [smax]   (s=16 needs ~2 GB RAM, ~30 s)
"""
import sys, json
import numpy as np


def pow2_table(M, phi):
    p = np.empty(phi, dtype=np.int64); p[0] = 1; k = 1
    while k < phi:
        m = min(k, phi - k); f = int(p[k - 1]) * 2 % M
        p[k:k + m] = (p[:m] * f) % M; k += m
    return p


def run(smax):
    out = []; p_prev = np.array([1.0]); prev = 1.0
    for s in range(1, smax + 1):
        M = 3 ** s; phi = 2 * 3 ** (s - 1)
        pw = pow2_table(M, phi)                       # pw[r] = 2^r mod M
        dlog = np.full(M, -1, dtype=np.int64); dlog[pw] = np.arange(phi)
        Z = (1 + 3 * np.arange(3 ** (s - 1), dtype=np.int64)) % M
        qZ = np.zeros(phi); np.add.at(qZ, dlog[Z], p_prev)
        r = np.arange(phi, dtype=np.float64)
        w = np.where(r > 0, 2.0 ** (-r), 2.0 ** (-phi)) / (1 - 2.0 ** (-phi))  # P(A = r mod phi)
        qX = np.fft.irfft(np.fft.rfft(qZ) * np.conj(np.fft.rfft(w)), n=phi)   # dlog(X) = dlog(Z) - A
        qX[qX < 0] = 0
        chi = M * float((qX * qX).sum())
        out.append({"s": s, "chi": chi, "E": chi - prev, "mass": float(qX.sum())})
        print(json.dumps(out[-1]), flush=True)
        p = np.zeros(M); p[pw] = qX; p_prev = p; prev = chi
    return out


if __name__ == "__main__":
    res = run(int(sys.argv[1]) if len(sys.argv) > 1 else 14)
    json.dump(res, open("chi_s_exact.json", "w", newline="\n"), indent=1)
